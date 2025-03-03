import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import { useQuery, useMutation } from "react-query";

import Chat from "@/components/Chat";
import Sidebar from "@/components/Sidebar";
import SplitScreen from "@/components/SplitScreen";
import TopBanner from "@/components/TopBanner";
import DarkMagicMode from "@/components/DarkMagicMode";
import EasterEgg from "@/components/EasterEgg";

export default function ChatPage() {
  const router = useRouter();
  const [mode, setMode] = useState("normal");
  const [chatHistory, setChatHistory] = useState([]);
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [isSplitScreen, setIsSplitScreen] = useState(false);

  // Fetch chat history from local storage or database
  const { data: chatHistoryData } = useQuery(
    "chatHistory",
    () => {
      const chatHistoryCookie = document.cookie
        .split("; ")
        .find((row) => row.startsWith("alchemist_chat_history="));
      if (chatHistoryCookie) {
        return JSON.parse(chatHistoryCookie.split("=")[1]);
      } else {
        return [];
      }
    },
    {
      refetchOnWindowFocus: false,
    }
  );

  useEffect(() => {
    if (chatHistoryData) {
      setChatHistory(chatHistoryData);
    }
  }, [chatHistoryData]);

  // Save chat history to local storage or database
  const saveChatHistory = () => {
    const chatHistoryCookie = `alchemist_chat_history=${JSON.stringify(chatHistory)}`;
    document.cookie = chatHistoryCookie;
  };

  // Send prompt to LLM model
  const { mutate: sendPrompt } = useMutation(
    (prompt) => {
      return fetch("/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });
    },
    {
      onSuccess: (response) => {
        if (response.ok) {
          response.json().then((data) => {
            setResponse(data.response);
            saveChatHistory();
          });
        }
      },
    }
  );

  // Handle prompt change
  const handlePromptChange = (event) => {
    setPrompt(event.target.value);
  };

  // Handle send button click
  const handleSendClick = () => {
    if (prompt.trim()) {
      const newChat = {
        role: "user",
        content: prompt,
      };
      setChatHistory([...chatHistory, newChat]);
      setPrompt("");
      sendPrompt(prompt);
    }
  };

  // Handle mode switch
  const handleModeSwitch = () => {
    if (mode === "normal") {
      setMode("dark_magic");
      document.cookie = `alchemist_mode=dark_magic; path=/`;
    } else {
      setMode("normal");
      document.cookie = `alchemist_mode=normal; path=/`;
    }
  };

  // Handle split-screen toggle
  const handleSplitScreenToggle = () => {
    setIsSplitScreen(!isSplitScreen);
  };

  return (
    <div className="flex flex-col h-screen">
      <TopBanner mode={mode} onModeSwitch={handleModeSwitch} />
      <SplitScreen isSplitScreen={isSplitScreen}>
        <Chat
          chatHistory={chatHistory}
          response={response}
          onSendClick={handleSendClick}
          onPromptChange={handlePromptChange}
          onSplitScreenToggle={handleSplitScreenToggle}
        />
        <Sidebar chatHistory={chatHistory} />
      </SplitScreen>
      <DarkMagicMode mode={mode} />
      <EasterEgg />
    </div>
  );
}
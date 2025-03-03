import { useState, useEffect } from "react";

const Chat = ({
  chatHistory,
  response,
  onSendClick,
  onPromptChange,
  onSplitScreenToggle,
}) => {
  const [isTyping, setIsTyping] = useState(false);

  useEffect(() => {
    if (response) {
      setIsTyping(true);
      const typingInterval = setInterval(() => {
        setIsTyping((prevIsTyping) => !prevIsTyping);
      }, 500);
      setTimeout(() => {
        clearInterval(typingInterval);
        setIsTyping(false);
      }, 3000); // Simulate 3 seconds of typing
    }
  }, [response]);

  return (
    <div className="flex-1 p-4">
      <div className="flex flex-col h-full">
        <div className="flex-1 overflow-y-auto">
          {chatHistory.map((message, index) => (
            <div
              key={index}
              className={`mb-4 ${
                message.role === "user" ? "text-right" : "text-left"
              }`}
            >
              <div
                className={`inline-block p-3 rounded-lg ${
                  message.role === "user"
                    ? "bg-blue-500 text-white"
                    : "bg-gray-200"
                }`}
              >
                {message.content}
              </div>
            </div>
          ))}
          {isTyping && (
            <div className="mb-4 text-left">
              <div className="inline-block p-3 rounded-lg bg-gray-200">
                {response}
              </div>
            </div>
          )}
        </div>
        <div className="mt-4">
          <input
            type="text"
            value={prompt}
            onChange={onPromptChange}
            className="w-full p-2 border rounded-md"
            placeholder="Type your prompt here..."
          />
          <button
            onClick={onSendClick}
            className="ml-2 px-4 py-2 bg-blue-500 text-white rounded-md"
          >
            Send
          </button>
          <button
            onClick={onSplitScreenToggle}
            className="ml-2 px-4 py-2 bg-gray-300 rounded-md"
          >
            Toggle Split Screen
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chat;
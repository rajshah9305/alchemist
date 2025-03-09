// frontend/src/components/ChatArea.tsx
import { useState } from 'react';
import { interact } from '../utils/api';
import styles from '../styles/Home.module.css';
import { Interaction } from '../utils/types';

interface ChatAreaProps {
  darkMode: boolean;
  onNewMessage: (interaction: Interaction) => void;
  messages: Interaction[];
}

const ChatArea: React.FC<ChatAreaProps> = ({ darkMode, onNewMessage, messages }) => {
  const [prompt, setPrompt] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!prompt.trim()) return;
    
    setIsLoading(true);
    try {
      const data = await interact(prompt);
      const newInteraction: Interaction = {
        prompt: prompt,
        response: data.response,
        timestamp: new Date().toISOString()
      };
      onNewMessage(newInteraction);
      setPrompt('');
    } catch (error) {
      console.error('Error sending message:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={`${styles.chatArea} ${darkMode ? styles.darkMode : ''}`}>
      <div className={`${styles.chatBox} ${darkMode ? styles.darkMode : ''}`}>
        {messages.length === 0 ? (
          <div className={styles.emptyChat}>Start a new conversation</div>
        ) : (
          messages.map((message, index) => (
            <div key={index} className={styles.messageGroup}>
              <div className={styles.prompt}>{message.prompt}</div>
              <div className={styles.response}>{message.response}</div>
            </div>
          ))
        )}
      </div>
      <form onSubmit={handleSubmit} className={styles.chatForm}>
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Type your prompt here..."
          className={`${styles.chatInput} ${darkMode ? styles.darkMode : ''}`}
          disabled={isLoading}
        />
        <button 
          type="submit" 
          className={`${styles.chatButton} ${darkMode ? styles.darkMode : ''}`}
          disabled={isLoading}
        >
          {isLoading ? 'Sending...' : 'Send'}
        </button>
      </form>
    </div>
  );
};

export default ChatArea;

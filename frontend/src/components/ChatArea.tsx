// frontend/src/components/ChatArea.tsx
import { useState } from 'react';
import { interact } from '../utils/api';
import styles from '../styles/Home.module.css';

interface ChatAreaProps {
  darkMode: boolean;
}

const ChatArea: React.FC<ChatAreaProps> = ({ darkMode }) => {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const data = await interact(prompt);
    setResponse(data.response);
  };

  return (
    <div className={`${styles.chatArea} ${darkMode ? styles.darkMode : ''}`}>
      <div className={styles.chatBox}>
        <div className={styles.prompt}>{prompt}</div>
        <div className={styles.response}>{response}</div>
      </div>
      <form onSubmit={handleSubmit} className={styles.chatForm}>
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Type your prompt here..."
          className={styles.chatInput}
        />
        <button type="submit" className={styles.chatButton}>Send</button>
      </form>
    </div>
  );
};

export default ChatArea;
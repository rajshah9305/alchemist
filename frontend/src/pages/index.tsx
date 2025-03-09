// frontend/src/pages/index.tsx
import { useState, useEffect } from 'react';
import ChatArea from '../components/ChatArea';
import Sidebar from '../components/Sidebar';
import TopBar from '../components/TopBar';
import ToggleButton from '../components/ToggleButton';
import { getMemory } from '../utils/api';
import styles from '../styles/Home.module.css';
import { Interaction } from '../utils/types';

export default function Home() {
  const [memory, setMemory] = useState<Interaction[]>([]);
  const [darkMode, setDarkMode] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchMemory = async () => {
      setIsLoading(true);
      try {
        const data = await getMemory();
        setMemory(data);
        setError(null);
      } catch (err) {
        console.error('Failed to fetch memory:', err);
        setError('Failed to load chat history. Please try refreshing the page.');
      } finally {
        setIsLoading(false);
      }
    };
    fetchMemory();
  }, []);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
    // Apply dark mode to body
    if (!darkMode) {
      document.body.classList.add('darkMode');
    } else {
      document.body.classList.remove('darkMode');
    }
  };

  const handleNewMessage = (interaction: Interaction) => {
    setMemory(prevMemory => [...prevMemory, interaction]);
  };

  return (
    <div className={`${styles.container} ${darkMode ? styles.darkMode : ''}`}>
      <TopBar darkMode={darkMode} />
      <ToggleButton darkMode={darkMode} toggleDarkMode={toggleDarkMode} />
      
      {error && <div className={styles.errorMessage}>{error}</div>}
      
      <div className={styles.main}>
        <Sidebar memory={memory} darkMode={darkMode} />
        <ChatArea 
          darkMode={darkMode} 
          onNewMessage={handleNewMessage} 
          messages={memory}
        />
      </div>
    </div>
  );
}

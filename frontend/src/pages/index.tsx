// frontend/src/pages/index.tsx
import { useState, useEffect } from 'react';
import ChatArea from '../components/ChatArea';
import Sidebar from '../components/Sidebar';
import TopBar from '../components/TopBar';
import ToggleButton from '../components/ToggleButton';
import { getMemory } from '../utils/api';
import styles from '../styles/Home.module.css';

export default function Home() {
  const [memory, setMemory] = useState([]);
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    const fetchMemory = async () => {
      const data = await getMemory();
      setMemory(data);
    };
    fetchMemory();
  }, []);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div className={styles.container}>
      <TopBar darkMode={darkMode} />
      <ToggleButton darkMode={darkMode} toggleDarkMode={toggleDarkMode} />
      <div className={styles.main}>
        <Sidebar memory={memory} />
        <ChatArea darkMode={darkMode} />
      </div>
    </div>
  );
}
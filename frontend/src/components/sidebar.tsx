// frontend/src/components/Sidebar.tsx
import styles from '../styles/Home.module.css';
import { Interaction } from '../utils/types';

interface SidebarProps {
  memory: Interaction[];
  darkMode: boolean;
}

const Sidebar: React.FC<SidebarProps> = ({ memory, darkMode }) => {
  return (
    <div className={`${styles.sidebar} ${darkMode ? styles.darkMode : ''}`}>
      <h2>Chat History</h2>
      <ul className={styles.chatHistory}>
        {memory.map((interaction, index) => (
          <li key={index} className={styles.chatItem}>
            <strong>Prompt:</strong> {interaction.prompt}<br />
            <strong>Response:</strong> {interaction.response}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;

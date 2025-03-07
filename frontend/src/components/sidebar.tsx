// frontend/src/components/Sidebar.tsx
import styles from '../styles/Home.module.css';

interface SidebarProps {
  memory: any[];
}

const Sidebar: React.FC<SidebarProps> = ({ memory }) => {
  return (
    <div className={styles.sidebar}>
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
// frontend/src/components/TopBar.tsx
import styles from '../styles/Home.module.css';

interface TopBarProps {
  darkMode: boolean;
}

const TopBar: React.FC<TopBarProps> = ({ darkMode }) => {
  return (
    <div className={`${styles.topBar} ${darkMode ? styles.darkMode : ''}`}>
      <img
        src={darkMode ? '/dark_magic_logo.png' : '/normal_logo.png'}
        alt="Alchemist Logo"
        className={styles.logo}
      />
      <h1>Alchemist - Powered by Codestral 25.01</h1>
    </div>
  );
};

export default TopBar;
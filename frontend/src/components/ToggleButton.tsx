// frontend/src/components/ToggleButton.tsx
import styles from '../styles/Home.module.css';

interface ToggleButtonProps {
  darkMode: boolean;
  toggleDarkMode: () => void;
}

const ToggleButton: React.FC<ToggleButtonProps> = ({ darkMode, toggleDarkMode }) => {
  return (
    <button
      className={`${styles.toggleButton} ${darkMode ? styles.darkMode : ''}`}
      onClick={toggleDarkMode}
    >
      {darkMode ? 'Normal Mode' : 'Dark Magic Mode'}
    </button>
  );
};

export default ToggleButton;
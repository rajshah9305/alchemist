import { useEffect } from "react";

const DarkMagicMode = ({ mode }) => {
  useEffect(() => {
    if (mode === "dark_magic") {
      document.body.classList.add("dark-magic");
    } else {
      document.body.classList.remove("dark-magic");
    }
  }, [mode]);

  return null;
};

export default DarkMagicMode;
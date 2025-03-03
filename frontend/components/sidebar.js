import { useState, useEffect } from "react";

const Sidebar = ({ chatHistory }) => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  useEffect(() => {
    const sidebarToggle = document.querySelector(".sidebar-toggle");
    sidebarToggle.addEventListener("click", () => {
      setIsSidebarOpen(!isSidebarOpen);
    });
  }, [isSidebarOpen]);

  return (
    <div
      className={`flex-none w-64 bg-gray-800 text-white ${
        isSidebarOpen ? "block" : "hidden"
      }`}
    >
      <div className="p-4">
        <h2 className="text-lg font-bold mb-2">Chat History</h2>
        <ul>
          {chatHistory.map((message, index) => (
            <li key={index} className="mb-2">
              <div className="inline-block p-2 rounded-lg bg-gray-700">
                {message.content}
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Sidebar;
const TopBanner = ({ mode, onModeSwitch }) => {
  return (
    <div className="bg-gray-900 text-white p-2">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Alchemist</h1>
        <button
          onClick={onModeSwitch}
          className="px-4 py-2 bg-gray-700 rounded-md"
        >
          {mode === "normal" ? "Dark Magic Mode" : "Normal Mode"}
        </button>
      </div>
    </div>
  );
};

export default TopBanner;
const EasterEgg = () => {
  const [showEasterEgg, setShowEasterEgg] = useState(false);

  useEffect(() => {
    const handleEasterEgg = () => {
      if (window.location.hash === "#forbidden-code") {
        setShowEasterEgg(true);
      }
    };

    window.addEventListener("hashchange", handleEasterEgg);

    return () => {
      window.removeEventListener("hashchange", handleEasterEgg);
    };
  }, []);

  if (showEasterEgg) {
    return (
      <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-black bg-opacity-75">
        <div className="bg-gray-800 p-4 rounded-md">
          <h2 className="text-2xl font-bold mb-2">Forbidden Code</h2>
          <p className="text-white">
            This is some cursed, funny, or terrifyingly bad code snippet.
          </p>
          <button
            onClick={() => setShowEasterEgg(false)}
            className="mt-4 px-4 py-2 bg-red-500 text-white rounded-md"
          >
            Close
          </button>
        </div>
      </div>
    );
  }

  return null;
};

export default EasterEgg;
import { useEffect } from "react";
import { useRouter } from "next/router";
import { QueryClient, QueryClientProvider } from "react-query";

import "../styles/global.css";

const queryClient = new QueryClient();

export default function App({ Component, pageProps }) {
  const router = useRouter();

  useEffect(() => {
    // Check for mode cookie and set mode
    const modeCookie = document.cookie
      .split("; ")
      .find((row) => row.startsWith("alchemist_mode="));
    if (modeCookie) {
      const mode = modeCookie.split("=")[1];
      if (mode === "dark_magic") {
        document.body.classList.add("dark-magic");
      }
    }
  }, []);

  return (
    <QueryClientProvider client={queryClient}>
      <Component {...pageProps} />
    </QueryClientProvider>
  );
}
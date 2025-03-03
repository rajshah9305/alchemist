// next.config.js
module.exports = {
  reactStrictMode: true, // Enables React's Strict Mode to help identify potential problems in the app
  swcMinify: true,       // Enables the SWC compiler for faster builds and minification
  experimental: {
    appDir: true,        // Use the experimental app directory feature (for Next.js 13+)
  },
  // If you want to use environment variables or customize Webpack, you can add additional configurations:
  // env: {
  //   CUSTOM_KEY: 'value',
  // },
  // webpack(config, { isServer }) {
  //   // Custom webpack config can go here
  //   return config;
  // },
};

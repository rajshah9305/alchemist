# Alchemist Setup Guide for M2 Mac

## Prerequisites
- Docker
- Docker Compose
- Node.js and npm

## Installation
1. Clone the repository: `git clone https://github.com/your-username/alchemist.git`
2. Navigate to the project directory: `cd alchemist`
3. Build the Docker images: `docker-compose build`
4. Start the containers: `docker-compose up`
5. Open your browser and go to `http://localhost:3000` to access Alchemist.

## Usage
- Alchemist is a standalone web application, so you can access it via a browser.
- The frontend is built with Next.js and Tailwind CSS, providing a hacker-themed chat UI.
- The backend is powered by FastAPI, handling user authentication, session storage, and communication with the Codestral 25.01 model.
- The model is hosted locally using vLLM, and you can switch between normal and dark magic modes.
- Enjoy the easter eggs and have fun with your AI coding assistant!

## Contributing
Feel free to contribute to the project by submitting pull requests or opening issues.

## License
This project is licensed under the MIT License.
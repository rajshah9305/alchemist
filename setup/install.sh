setup/install.sh
<>
sh


#!/bin/bash

# Install dependencies for backend
pip install -r requirements.txt

# Build and run Docker containers
docker-compose up --build
setup/README.md
<>
markdown


# Alchemist Setup

## Prerequisites
- Docker
- Docker Compose

## Setup Steps

1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd Alchemist
Build and run the Docker containers:

<>
sh


./setup/install.sh
Access the application:

Frontend: http://localhost:3000
Backend: http://localhost:8000
API Documentation: http://localhost:8000/docs
## Additional Information

For more details, refer to the [API Documentation](http://localhost:8000/docs).
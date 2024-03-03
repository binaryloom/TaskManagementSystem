## Deployment Guide

1. **Download and Install Docker**: If you haven't already, download and install Docker Desktop from the [official website](https://www.docker.com/products/docker-desktop).

2. **Create Deployment Folder**: Make a folder in the desired location where you want to deploy the Task Management System.

3. **Copy Docker Compose File**: Copy the Docker Compose file (`docker-compose.yml`) into the deployment folder you created in step 2.

4. **Create Environment Variables File**: Create a `.env` file in the same directory as the Docker Compose file and paste the following environment variable configurations:

   ```plaintext
   POSTGRES_DB=Wu659S
   POSTGRES_USER=nU4Y12
   POSTGRES_PASSWORD=RBEE5h2s88BnG2VHyMW66DSN
   ```

   Replace `Wu659S`, `nU4Y12`, and `RBEE5h2s88BnG2VHyMW66DSN` with your desired values.

5. **Deploy Using Docker Compose**: Open a terminal or command prompt, navigate to the deployment folder, and run the following command:

   ```bash
   docker-compose up -d
   ```

   This command will start the Docker containers in detached mode, allowing them to run in the background.

6. **Access the Task Management System**: Open a web browser and navigate to [http://127.0.0.1:8001](http://127.0.0.1:8001) to access the Task Management System.

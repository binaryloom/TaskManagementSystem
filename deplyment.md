# Deployment Guide

1. **Download and Install Docker**: If you haven't already, download and install Docker Desktop from the [official website](https://www.docker.com/products/docker-desktop).

2. **Create Deployment Folder**: Make a folder in the desired location where you want to deploy the Task Management System.

3. **Copy Docker Compose File**: Copy and past the section bellow to Docker Compose file (`docker-compose.yml`) into the deployment folder you created in step 2.

   ```yml
   version: "3.7"
   networks:
   tms_net:
     driver: bridge
     name: tms_net

   services:
   lb_server:
     image: haproxy:2.7
     container_name: lb_server
     hostname: lb_server
     restart: unless-stopped
     volumes:
       - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
     networks:
       - tms_net
     ports:
       - 8001:80
     depends_on:
     tms_server:
       condition: service_healthy

   tms_server:
     image: ghcr.io/binaryloom/taskmanagementsystem:main
     container_name: tms_server
     hostname: tms_server
     restart: unless-stopped
     networks:
       - tms_net
     depends_on:
     db_server:
       condition: service_healthy
     environment:
     APP_DB_HOST: db_server
     APP_DB_DATABASE: ${POSTGRES_DB}
     APP_DB_USER: ${POSTGRES_USER}
     APP_DB_PASSWORD: ${POSTGRES_PASSWORD}
     healthcheck:
     test: curl -f http://localhost/healthcheck
     interval: 3s
     timeout: 2s
     retries: 10
     start_period: 5s

   db_server:
     image: postgres:latest
     container_name: db_server
     hostname: db_server
     restart: unless-stopped
     networks:
       - tms_net
     volumes:
       - ./db_data:/var/lib/postgresql/data
     ports:
       - 5432:5432
     environment:
     POSTGRES_DB: ${POSTGRES_DB}
     POSTGRES_USER: ${POSTGRES_USER}
     POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
     healthcheck:
     test: pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}
     interval: 10s
     timeout: 5s
     retries: 3
   ```

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

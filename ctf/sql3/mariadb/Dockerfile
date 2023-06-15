# Use the latest version of the MariaDB base image
FROM mariadb:latest
# Copy the database.sql file to the /docker-entrypoint-initdb.d/ directory in the container
# This will automatically execute the database.sql file
COPY ./database.sql /docker-entrypoint-initdb.d/  
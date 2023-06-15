# Use the Python 3 base image with Alpine Linux 3.17
FROM python:3-alpine3.17

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy the requirements.txt file to the /app directory in the container
COPY ./requirements.txt /app/requirements.txt

# Install the Python dependencies specified in requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the contents of the ./flask directory to /app/flask in the container
COPY ./flask ./app/flask

# Set the working directory to /app/flask
WORKDIR /app/flask/

# Set the entrypoint for the container to be the "python" command
ENTRYPOINT [ "python" ]

# Set the default command to run the "__init__.py" file
CMD ["crypto3.py"]
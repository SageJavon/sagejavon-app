# Use an official Python runtime as a parent image, specifically the slim version to keep the image size down
FROM python:3.11-slim

# Set the working directory to /app inside the container
WORKDIR /sagejavon-app

# Copy the current directory contents into the container at /app
COPY . /sagejavon-app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Define the command to run on container start. This script starts the Flask application.
CMD ["python", "app.py"]
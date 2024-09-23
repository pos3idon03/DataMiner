# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables (if needed)
# ENV VARIABLE_NAME=value

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "integration.py"]



# Use Python base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt to container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app files to the container
COPY . /app

# Expose port 80 for FastAPI app
EXPOSE 80

# Command to start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

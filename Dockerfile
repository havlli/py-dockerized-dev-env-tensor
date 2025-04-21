# Use official TensorFlow GPU image as base
FROM tensorflow/tensorflow:latest-gpu

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Copy requirements file for additional packages
COPY requirements.txt .

# Upgrade pip and install additional Python packages
# No need for apt-get install for python/pip as they exist
# Assume base image has necessary build tools for these packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Default command (useful for exec, overridden by docker-compose)
CMD ["bash"] 
# Use a specific Python version for consistency
FROM python:3.10

# Install system dependencies that may be required by Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory in the container
COPY requirements.txt /app/

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the working directory
COPY . /app

# Expose the default Django port
EXPOSE 8000

# Define the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

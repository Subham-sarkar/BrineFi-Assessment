# Use python 3.10 parent image
FROM python:3.10-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the application files and data into the container
COPY scripts/ /app
COPY data/ /app/data

# Install dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Run the application
CMD ["python", "/app/app.py"]


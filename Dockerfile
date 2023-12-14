# Use an official Python runtime as a parent image
FROM python:3.12.0

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run file.py first, and then app.py
CMD ["sh", "-c", "python file.py && python app.py"]

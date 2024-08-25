# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY servers/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files
COPY servers/app.py .

EXPOSE 5000

# Command to run both Flask apps using gunicorn
CMD ["sh", "-c", "gunicorn -w 2 -b 0.0.0.0:5000 app:app"]

# docker build -t flask-app .
# docker run  -storage-opt size=2G -p 5000:5000 flask-app

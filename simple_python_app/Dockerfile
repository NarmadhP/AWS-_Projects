#Base image
# Use a lightweight Python image
FROM python:3.8-slim
# Set the working directory in the container to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy the into container at /app
COPY . .
# expose flask port
EXPOSE 5000

# set environment variables
ENV FLASK_APP=app.py

# Run the application:
CMD [ "python", "app.py" ]

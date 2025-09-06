# Use a Python base image
FROM python:3.9-slim-buster

# Define build arguments for AWS credentials
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

# Set environment variables from build arguments
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}

# Set the working directory inside the container
WORKDIR /app

# Install requests
RUN pip install requests
RUN pip install boto3

# (Optional) Copy your application code into the container
COPY  src/*.py /app

# (Optional) Define the command to run your application
 CMD ["python", "get_positions.py"]

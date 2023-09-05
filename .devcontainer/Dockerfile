# Use an official Ubuntu runtime as the base image
FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port that Streamlit will run on
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "chat.py"]

# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Install fortune-mod, cowsay, git, and other dependencies
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay git netcat-openbsd

# Set the working directory to /app
WORKDIR /app

# Copy the wisecow.sh file from the current directory to /app
COPY wisecow.sh .

# Provide execute permission to the script
RUN chmod +x wisecow.sh

# Add the paths to fortune-mod and cowsay to the PATH environment variable
ENV PATH="/usr/games:$PATH"

# Expose the port that the script will use
EXPOSE 4499

# Run the script with prerequisites check when the container launches
CMD ["./wisecow.sh"]

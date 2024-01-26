# Using official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Installing fortune-mod, cowsay, git, and other dependencies
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay git netcat-openbsd

# Setting the working directory to /app
WORKDIR /app

# Cloning the wisecow repository
RUN git clone https://github.com/nyrahul/wisecow.git .

# Providing execute permission to the script
RUN chmod +x wisecow.sh

# Exposing the port that the script will use
EXPOSE 4499

# Setting PATH to include /usr/games where fortune and cowsay binaries are located
ENV PATH="/usr/games:${PATH}"

# Runing the script when the container launches
CMD ["./wisecow.sh"]

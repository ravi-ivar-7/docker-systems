# Base image
FROM ubuntu:20.04

# Install dependencies as root
USER root
RUN apt-get update && \
    apt-get install -y curl wget gnupg sudo python3 python3-pip

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Create necessary directories and set permissions
RUN mkdir -p /config /cache /local /project /bash_history && \
    chown -R 1000:1000 /config /cache /local /project /bash_history

# Create a non-root user
ARG USERNAME=user1
RUN useradd -ms /bin/bash $USERNAME

# Add the non-root user to sudoers
RUN echo "$USERNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Expose the port on which code-server will run
EXPOSE 8080

# Set environment variables to redirect cache, config, and local directories
ENV XDG_CACHE_HOME=/cache
ENV XDG_CONFIG_HOME=/config
ENV XDG_DATA_HOME=/local

# Set the working directory to /project
WORKDIR /project

# Set the user to a non-root user
USER $USERNAME

# Link .bash_history to the external directory
RUN ln -s /bash_history/.bash_history /home/$USERNAME/.bash_history

# Start code-server with password
CMD ["sh", "-c", "code-server --bind-addr 0.0.0.0:8080 --auth password --disable-telemetry --user-data-dir /project/.vscode"]

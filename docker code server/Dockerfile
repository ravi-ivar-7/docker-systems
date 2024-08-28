# Base image
FROM ubuntu:20.04

# Define build-time arguments
ARG MAIN_DIR=project

# Install dependencies
USER root
RUN apt-get update && \
    apt-get install -y curl wget gnupg sudo python3 python3-pip openssl

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Create a non-root user
RUN useradd -ms /bin/bash user1

# Use the ARG variable to create necessary directories and set permissions
RUN mkdir -p /home/$MAIN_DIR /certs && \
    chown -R user1:user1 /home /certs && \
    chmod -R 755 /home /certs

# Add the non-root user to sudoers
RUN echo "user1 ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Expose the HTTPS port
EXPOSE 8443

# Set the working directory
WORKDIR /home

# Switch to non-root user
USER user1

# Start code-server with HTTPS
CMD ["sh", "-c", "code-server --bind-addr 0.0.0.0:8443 --auth password --disable-telemetry --user-data-dir /home"]

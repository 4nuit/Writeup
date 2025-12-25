FROM alpine:latest

# Set working directory
WORKDIR /challenge/

# Install dependencies
RUN apk add --no-cache bash socat

# Copy ressources
COPY jail.sh /challenge/
COPY entrypoint.sh /challenge/

# Write flag
COPY flag.txt /flag.txt
RUN chmod 755 /flag.txt
RUN mv /flag.txt /flag.txt

# Set permissions
RUN chmod 755 /challenge/jail.sh /challenge/entrypoint.sh

# Copy binaries to root bin
RUN mkdir -p /root/bin/
RUN cp /bin/cat /root/bin/

# Expose port
ENTRYPOINT ["/challenge/entrypoint.sh"]

# Use the official MongoDB image from Docker Hub
FROM mongo:latest

# Set environment variables (optional)

# Create a directory for MongoDB data (if not using volumes)
# RUN mkdir -p /data/db

# Expose MongoDB default port
EXPOSE 27017

# Health check (optional)
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD mongosh --eval "db.adminCommand('ping')"

# You can add initialization scripts by mounting them to /docker-entrypoint-initdb.d/
# or copy them directly (less flexible)
# COPY init.js /docker-entrypoint-initdb.d/

# Command to run MongoDB (the base image already has this)
CMD ["mongod"]
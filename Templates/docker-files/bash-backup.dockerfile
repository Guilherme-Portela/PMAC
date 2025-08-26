# Dockerfile para Bash - backup
FROM debian:stable-slim
WORKDIR /scripts
COPY . .
CMD ["bash", "script.sh"]

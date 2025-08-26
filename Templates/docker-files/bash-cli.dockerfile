# Dockerfile para Bash - cli
FROM debian:stable-slim
WORKDIR /scripts
COPY . .
CMD ["bash", "script.sh"]

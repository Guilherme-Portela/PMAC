# Dockerfile para Bash - deploy
FROM debian:stable-slim
WORKDIR /scripts
COPY . .
CMD ["bash", "script.sh"]

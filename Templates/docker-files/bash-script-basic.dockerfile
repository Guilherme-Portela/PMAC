# Dockerfile para Bash - script-basic
FROM debian:stable-slim
WORKDIR /scripts
COPY . .
CMD ["bash", "script.sh"]

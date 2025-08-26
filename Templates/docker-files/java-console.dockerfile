# Dockerfile para Java - console
FROM openjdk:21-slim
WORKDIR /app
COPY . .
CMD ["java", "Main"]

# Dockerfile para Java - library
FROM openjdk:21-slim
WORKDIR /app
COPY . .
CMD ["java", "Main"]

# Dockerfile para Java - maven
FROM openjdk:21-slim
WORKDIR /app
COPY . .
CMD ["java", "Main"]

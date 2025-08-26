# Dockerfile para Java - spring
FROM openjdk:21-slim
WORKDIR /app
COPY . .
CMD ["java", "Main"]

# Dockerfile para Java - unit-test
FROM openjdk:21-slim
WORKDIR /app
COPY . .
CMD ["java", "Main"]

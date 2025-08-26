# Dockerfile para C - library
FROM gcc:13
WORKDIR /src
COPY . .
RUN gcc -o main main.c
CMD ["./main"]

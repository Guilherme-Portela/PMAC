# Dockerfile para C - makefile
FROM gcc:13
WORKDIR /src
COPY . .
RUN gcc -o main main.c
CMD ["./main"]

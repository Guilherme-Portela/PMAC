# Dockerfile para C++ - console
FROM gcc:13
WORKDIR /src
COPY . .
RUN g++ -o main main.cpp
CMD ["./main"]

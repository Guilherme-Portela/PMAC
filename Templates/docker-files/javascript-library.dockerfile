# Dockerfile para JavaScript - library
FROM node:20-slim
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]

# Dockerfile para JavaScript - vite
FROM node:20-slim
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]

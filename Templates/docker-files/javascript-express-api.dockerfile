# Dockerfile para JavaScript - express-api
FROM node:20-slim
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]

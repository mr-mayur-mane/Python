FROM node:22-alpine

WORKDIR /app

COPY /app ./

RUN npm install

COPY . .

EXPOSE 3000

CMD["node", "src/index.js"]
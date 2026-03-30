FROM node:22-alpine

WORKDIR /app

COPY /app ./

RUN node install --production

COPY . .

EXPOSE 3000

CMD ["node", "src/index.js"]
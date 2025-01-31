FROM node:20

WORKDIR my-app

COPY . .

RUN npm install

CMD ["npm", "run", "dev"]
FROM node:20

<<<<<<< HEAD
WORKDIR my-app

COPY . .

RUN npm install

CMD ["npm", "run", "dev"]
=======
WORKDIR /my-app/

# Copy package.json and package-lock.json first to install dependencies
COPY package*.json ./

RUN npm install

# Copy the rest of the application code
COPY . .

EXPOSE 5173

CMD [ "npm", "run", "dev" ]
>>>>>>> db50b89 (added)

# Use Node.js as the base image
FROM node:20

# Set the working directory
WORKDIR /myapp

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port Vite uses (default: 5173)
EXPOSE 5173

# Run the application
CMD ["npm", "run", "dev"]

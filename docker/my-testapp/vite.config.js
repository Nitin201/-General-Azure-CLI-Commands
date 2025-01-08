import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Ensure the server binds to all interfaces for Docker
    port: 5173      // Optional: specify the port
  }
});

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  build: {
    outDir: 'dist',  // Carpeta de salida para el build
    emptyOutDir: true,
  },
  server: {
    proxy: {
      '/api': 'http://backend:5000',  // Proxy para el backend
    },
  },
});
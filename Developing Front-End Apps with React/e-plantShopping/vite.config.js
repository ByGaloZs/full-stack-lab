import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  base: '/full-stack-lab/Developing%20Front-End%20Apps%20with%20React/e-plantShopping',
  plugins: [react()],
});

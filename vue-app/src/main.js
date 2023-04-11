import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';

const app = createApp(App)

app.use(router)
app.mount('#app')

import 'bootstrap/dist/js/bootstrap.js';
import './assets/styles/main.scss'
import '../src/assets/styles/user-form.scss'
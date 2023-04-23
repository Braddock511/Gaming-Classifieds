import { createApp } from 'vue'
import App from './App.vue'
import VueCookies from 'vue-cookies'
import router from './router'
import store from './store.js'
import 'bootstrap/dist/css/bootstrap.css'

const app = createApp(App)

app.use(store)
app.use(router)
app.use(VueCookies)
app.mount('#app')

import 'bootstrap/dist/js/bootstrap.js'
import './assets/styles/main.scss'
import '../src/assets/styles/user-form.scss'
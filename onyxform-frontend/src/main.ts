import { createApp } from "vue";
import App from "./App.vue";
import router from './router'; // Correctly import your router instance
import './style.css'


const app = createApp(App);
app.use(router); // Register the router
app.mount("#app");

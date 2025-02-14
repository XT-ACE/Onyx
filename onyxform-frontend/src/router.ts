import { createRouter, createWebHistory } from 'vue-router';
import SignupForm from './components/SignupForm.vue';
import qrcode from './components/qrcode.vue';
import Profile from './components/profile.vue';


const routes = [
    { path: '/', component: SignupForm },
    { path: '/qrcode/:id', component: qrcode }, 
    { path: '/profile/:id', component: Profile },
];



const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

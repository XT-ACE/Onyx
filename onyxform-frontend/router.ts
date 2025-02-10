import { createRouter, createWebHistory } from 'vue-router';
import SignupForm from './src/components/SignupForm.vue';
import qrcode from './src/components/qrcode.vue';
import Profile from './src/components/profile.vue';


const routes = [
    { path: '/', component: SignupForm },
    { path: '/qrcode/:id', component: qrcode }, // Update this line
    { path: '/profile/:id', component: Profile },
];


const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

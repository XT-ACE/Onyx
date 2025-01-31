import { createRouter, createWebHistory } from 'vue-router';
import SignupForm from './components/SignupForm.vue';


const routes = [
    { path: '/signup', component: SignupForm },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

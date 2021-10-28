import main from "@/pages/main";
import {createRouter, createWebHistory} from "vue-router";
import postPage from "@/pages/postPage";
import about from "@/pages/about";
import postIdPage from "@/pages/postIdPage"

const routes = [
    {
        path: '/',
        component: main
    },
    {
        path: '/posts',
        component: postPage
    },
    {
        path: '/about',
        component: about
    },
    {
        path: '/posts/:id',
        component: postIdPage
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})
//
export default router;
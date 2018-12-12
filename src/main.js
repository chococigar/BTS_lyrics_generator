import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'

Vue.use(VueRouter) //tell vue to use the router


import HelloArmy from './components/HelloArmy'
import LyricsGen from './components/LyricsGen'

const routes = [

        {
            path: '/',
            component: HelloArmy
        }, {
            path: '/lyricsgen',
            component: LyricsGen
        }

    ] // define routes

const router = new VueRouter({
    routes,
    mode: 'history' //look into later
})

//Vue.config.productionTip = false // ???

new Vue({
        el: '#app',
        template: '<App/>',
        components: {
            App
        },
        router,
        render: h => h(App),
    }).$mount('#app') // mount the router to app
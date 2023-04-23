import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ListingView from '../views/ListingView.vue'
import ShoppingCartView from '../views/ShoppingCartView.vue'
import SearchView from '../views/SearchView.vue'
import ProductView from '../views/ProductView.vue'
import BuyView from '../views/BuyView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/listing',
      name: 'listing',
      component: ListingView
    },
    {
      path: '/shopping-cart',
      name: 'shopping-cart',
      component: ShoppingCartView
    },
    {
      path: '/search-view',
      name: 'search-view',
      component: SearchView
    },
    {
      path: '/product',
      name: 'prodcut',
      component: ProductView
    },
    {
      path: '/buy',
      name: 'buy',
      component: BuyView
    }
  ]
})

export default router

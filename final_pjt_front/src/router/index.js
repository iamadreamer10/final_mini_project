import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

import SignupView from '@/views/SignupView.vue'
import LoginView from '@/views/LoginView.vue'
import ProfileView from '@/views/ProfileView.vue'

// import CreateView from '@/views/CreateView.vue'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import UpdateView from '@/views/UpdateView.vue'

import BankView from '@/views/BankView.vue'
import DepositsView from '@/views/DepositsView.vue'
import SavingsView from '@/views/SavingsView.vue'

import MapView from '@/views/MapView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
import ExchangeView from '@/views/ExchangeView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // homeView component
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },

    // SignupView 컴포넌트 생성
    {
      path: '/signup',
      name: 'SignupView',
      component: SignupView,
    },
    // LoginView 컴포넌트 생성
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView,
    },
    
    // ProfileView 컴포넌트 생성
    // User의 id값을받아와야 하지 않나? -> 이후 구현하기
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView,
    },
    // ExchangeView 컴포넌트 생성
    // 환율 계산기
    {
      path: '/exchange',
      name: 'ExchangeView',
      component: ExchangeView,
    },

    // BankView 컴포넌트 생성
    // 특정 은행에 대한 정보
    {
      path: '/bank',
      name: 'BankView',
      component: BankView
    },
    { 
      path: '/deposits',
      name : 'DepositsView',
      component: DepositsView,
    },
    {
      path: '/savings',
      name: 'SavingsView',
      component: SavingsView,
    },
    // 금융 상품 정보 자세히 보기
    {
      path: '/productdetails/:id',
      name: 'ProductDetailView',
      component: ProductDetailView,
    },
    
    // ArticleView 컴포넌트 생성
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView,
    },
    // 게시글의 id값을 params로 받는 DetailView 컴포넌트 생성
    {
      path: '/article/:id',
      name: 'DetailView',
      component: DetailView
    },
    // 게시글 생성하는 CreateView 컴포넌트 생성
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    // 게시글 수정하는 UpdateView 컴포넌트 생성
    {
      path: '/update/:id',
      name: 'UpdateView',
      component: UpdateView
    },
    // 근처 은행을 검색하는 MapView 컴포넌트 생성
    {
      path: '/map',
      name: 'MapView',
      component: MapView
    },

  ]
})

export default router

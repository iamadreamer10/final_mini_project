import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {

  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000' // drf에 요청을 보내기 위한 url 주소

  const user = ref(null)
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const articles = ref([])

  const deposits = ref([])
  const depositsOptions = ref([])
  const savings = ref([])
  const savingsOptions = ref([])
  
  const financialProducts = ref([])
  // 사용자가 등록한 금융상품
  const joinProducts = ref([])

  // 추천 알고리즘을 위한 반응형 변수
  const ageList = ref([])
  const moneyList = ref([])
  const salaryList = ref([])
  
  // 사용자 관련 기능
  // DRF에 회원가입 요청
  const signUp = function (payload) {
    // payload에 입력받는 순서 확인하고 재작성 진행
    const { username, password1, password2, nickname, age, money, salary } = payload
    
    axios({
      method: 'post',
      // dj-rest-auth에서 회원가입할 때 사용하는 url
      url: `${API_URL}/dj-rest-auth/registration/`,
      data: {
        // key 이름 확실하게 지키기
        username, password1, password2, nickname, age, money, salary
      }
    })
    // post 요청 성공
    .then((response) => {
      const password = password1
      const payload = { username, password }
      logIn(payload)
    }) 
    .catch((error) => {
      console.log('회원가입 과정에서 에러 발생')
      console.log(error)
    })
  }
  
  // DRF에 로그인 요청
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/login/`,
      data: {
        username, password
      }
    })
    .then((response) => {
      token.value = response.data.key
      console.log(response.data)
      // 로그인 성공시, token값을 부여받고 홈페이지로 이동
      router.push({ name: 'HomeView' })
    })
    .catch((error) => {
      console.log('로그인 과정에서 에러가 발생했습니다.')
      console.log(error)
    })
  }
  // DRF에 로그아웃 요청
  const logOut = function () {
    
    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/logout/`,
    })
    .then((response) => {
      token.value = null
      router.push({ name: 'HomeView' })
    })
    .catch((error) => {
        console.log('로그아웃 과정에서 에러가 발생했습니다.')
        console.log(error)
      })
  }
  
  // DRF에 사용자 조회 요청
  const profile = function () {
    axios({
      method: 'get',
      // accounts.urls 확인해보기
      url: `${API_URL}/api/v1/accounts/profile/`,
      // 유저 정보 가져올 때 토큰값이 필요한가?
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      // console.log(response.data)
      user.value = response.data
      // user.value.id = response.data.id
      if (user.value.financial_products) {
        financialProducts.value = user.value.financial_products.split(',')
        joinProducts.value = []
        financialProducts.value.forEach((financialProduct) => {
          deposits.value.forEach((element) => {
            if(element['fin_prdt_cd'] === financialProduct){
              const cd = element['fin_prdt_cd']
              const nm = element['fin_prdt_nm']
              const joinProduct = [cd, nm]
              joinProducts.value.push(joinProduct)
            }
          });
          savings.value.forEach((element) => {
            if(element['fin_prdt_cd'] === financialProduct){
              const cd = element['fin_prdt_cd']
              const nm = element['fin_prdt_nm']
              const joinProduct = [cd, nm]
              joinProducts.value.push(joinProduct)
            }
          })
        })
      } else {

        joinProducts.value = []
      }})
    .catch((error) => {
      console.log(error)
    })
   }
    
    
  // 금융상품 관련 기능
  const getDeposits = function () {
    axios({
      method: 'get', 
      url: `${API_URL}/api/v1/financial_products/get_deposits/`,
      
    })
    .then((response) => {
      // console.log(response.data)
      deposits.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  
  const getDepositsOptions = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/financial_products/get_deposits_options/`,
      
    })
    .then((response) => {
      depositsOptions.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  // 금융상품 관련 기능
  const getSavings = function () {
    axios({
      method: 'get', 
      url: `${API_URL}/api/v1/financial_products/get_savings/`,
      
    })
    .then((response) => {
      // console.log(response.data)
      savings.value = response.data
      
    })
    .catch((error) => {
      console.log(`error는 ${error}`)
    })
  }
  
  const getSavingsOptions = function () {
    axios({
      method: 'get', 
      url: `${API_URL}/api/v1/financial_products/get_savings_options/`,
      
    })
    .then((response) => {
      // console.log(response.data)
      savingsOptions.value = response.data
      
    })
    .catch((error) => {
      console.log(`error는 ${error}`)
    })
  }
  
  // 게시글 관련 기능
  // DRF에 article 조회 요청
  const getArticles = function () {
    axios({
      method: 'get',
      // articles.urls 확인해보기
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        // 토큰 인증
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      articles.value = response.data
    })
    .catch((error) => {
      console.log('articles 조회 과정에서 error 발생')
      console.log(error)
    })
  }

  // 추천상품 관련 기능
  const recommendAge = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/financial_products/recommend_age/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
    .then((response) => {
      // console.log(response.data)
      ageList.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
    
  }

  const recommendMoney = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/financial_products/recommend_money/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
    .then((response) => {
      // console.log(response.data)
      moneyList.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
    
  }

  const recommendSalary = function() { 
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/financial_products/recommend_salary/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
    .then((response) => {
      // console.log(response.data)
      salaryList.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
    
  }

  return { articles, user, joinProducts, financialProducts, API_URL, token, isLogin, ageList, moneyList, salaryList, signUp, logIn, logOut, profile, getArticles, getDeposits, getSavings, getDepositsOptions, getSavingsOptions, deposits, depositsOptions, savings, savingsOptions, recommendAge, recommendMoney, recommendSalary}
}, { persist: true })

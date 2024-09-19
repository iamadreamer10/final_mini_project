<!-- App.vue -->
<!-- App.vue에서 구성할 내용 -->
<!-- 로그인이 되어있을 경우? home,  -->
<template>
  <header>
      <!-- 로고 이미지 또는 텍스트를 여기에 추가 -->
      <nav v-if="!store.isLogin">
        <p>해당 서비스를 이용하고 싶을 경우, 회원가입 또는 로그인을 진행해 주세요.</p>
        <!-- <RouterLink :to="{ name: 'HomeView' }">Home</RouterLink> | -->
        <RouterLink :to="{ name: 'SignupView' }">회원가입</RouterLink>|
        <!-- 로그인이 되어있는 경우는 LogoutView로 연결하고 싶음(이후 구현해보기) -->
        <!-- 로그인이 되어있는 경우는 본인 프로필 페이지로 이동 가능한 링크 보이게 -->
        <RouterLink :to="{ name: 'LoginView' }"> 로그인</RouterLink>
      </nav>
      <nav v-else>
        <RouterLink :to="{ name: 'HomeView' }">홈으로</RouterLink>
        <!-- <RouterLink :to="{ name: 'BankView' }">BankView</RouterLink> |
          <RouterLink :to="{ name: 'ArticleView' }">ArticleView</RouterLink> |
          <RouterLink :to="{ name: 'ProfileView' }">ProfileView</RouterLink> -->
        </nav>
        <div>
          <h3>
          효율적인 자산 관리를 위한 첫 걸음을 내딛어보세요!
        </h3>
      </div>
  </header>
  <div>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useRoute } from 'vue-router'
// 현재 로그인이 되어있는 상태인지를 파악하기 위해 useCounterStore 모듈 불러오기
import { useCounterStore } from '@/stores/counter'


const store = useCounterStore()
const route = useRoute()

// console.log(route)
// console.log(store.isLogin)
// console.log(store.token)

</script>

<style scoped>
  header {
    background-color: rgb(97, 151, 212);
    color: #fff; /* 흰색 글씨 */
    font-family: 'Your-Preferred-Font', sans-serif; /* 원하는 글꼴 지정 */
    padding: 10px; /* 내부 여백 설정 */
  }

  nav p {
    margin-bottom: 10px; /* 문단 아래 여백 설정 */
  }

  nav a {
    color: #fff; /* 흰색 글씨 */
    margin-right: 10px; /* 각 링크 사이 여백 설정 */
    text-decoration: none; /* 링크 밑줄 제거 */
  }

  nav a:hover {
    text-decoration: underline; /* 링크에 마우스 호버 시 밑줄 표시 */
  }
</style>

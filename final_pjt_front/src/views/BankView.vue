<!-- views/BankView.vue -->
<template>
  <header>
    <h1>금융상품 비교</h1>
    <nav class="navbar">
      <div class="nav-container">
        <div class="nav-links">
          <RouterLink :to="{ name: 'DepositsView' }" class="nav-link">예금 상품 목록</RouterLink>
          <RouterLink :to="{ name : 'SavingsView' }" class="nav-link">적금 상품 목록</RouterLink>
        </div>
      </div>
    </nav>
  </header>
  <RouterView/>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

// onMounted(() => {
//   axios({
//     method: 'get',
//     url: `${store.API_URL}/api/v1/financial_products/save_deposits/`
//   })
//   .then((response) => {
//     console.log(response)
//   })
//   .catch((error) => {
//     console.log(error)
//   })

//   axios({
//     method: 'get',
//     url: `${store.API_URL}/api/v1/financial_products/save_savings/`
//   })
//   .then((response) => {
//     console.log(response)
//   })
//   .catch((error) => {
//     console.log(error)
//   })
// })


</script>

<style scoped>

h1 {
  color: rgb(41, 92, 150);
}
.navbar {
  background-color: rgb(97, 151, 212); /* 신한은행 웹사이트와 유사한 파란색 배경색 */
  color: #ffffff; /* 흰색 텍스트 */
  padding: 10px 0; /* 상하로 10px 간격 */
}

.nav-container {
  max-width: 1200px; /* 최대 너비 */
  margin: 0 auto; /* 가운데 정렬 */
  display: flex; /* 자식 요소들을 수평으로 배치 */
  justify-content: space-between; /* 자식 요소 사이의 간격을 최대화하여 배치 */
  align-items: center; /* 수직으로 가운데 정렬 */
}

.nav-links {
  display: flex; /* 자식 요소들을 수평으로 배치 */
  margin-left: 20px; /* 왼쪽 여백 추가 */
}

.nav-link {
  color: #ffffff; /* 흰색 텍스트 */
  font-family: 'Arial', sans-serif; /* 원하는 글씨체로 변경 */
  margin-right: 10px; /* 각 링크 사이 간격 조정 */
  text-decoration: none; /* 기본 링크 밑줄 제거 */
}
</style>
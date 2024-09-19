<!-- views/ProfileView.vue -->

<template>
  <div class="profile-container">
    <h1 class="highlighted-heading">내 프로필</h1>
    <div v-if="user != null">
      <h3 class="highlighted-heading">{{ user.username }}님의 프로필 페이지 입니다.</h3>
      <p>닉네임 : {{ user.nickname }}</p>
      <p>나이 : {{ user.age }}</p>
      <p>자산 : {{ user.money }}</p>
      <p>소득 : {{ user.salary }}</p>
      <hr>
      <div>
        <h2 class="highlighted-heading">가입 상품 목록</h2>
        <div v-for="joinProduct in store.joinProducts" :key="joinProduct.id">
          <p>{{ joinProduct[1] }} 
          <button @click.prevent="deleteProduct(joinProduct[0])" class="product-button">해당 상품 해지</button></p>
        </div>
        <hr>
      </div>
    </div>
     <Cart/>
  </div>
</template>

<script setup>
// 특정 유저의 프로필 페이지 -> 해당 유저 pk값이 있을 거임
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import Cart from '@/components/Cart.vue'
const store = useCounterStore()
const user = ref(null)

const deleteProduct = (product) => {
  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/financial_products/put_product/`,
    data: {
      financial_products: product
    },
    headers: {
        Authorization: `Token ${store.token}`
      }
  })
  .then((response)=> {
    console.log('첫번째 then', response)

    return store.user
  })
  .then((response) => {
    console.log('두번째 then', response)
    user.value = response
    console.log('두번째 then uservalue ', user.value)
    store.profile()
  })
  .catch((error) => {
    console.log(error)
  })
}
// console.log(store.isLogin)
// console.log(store.user)
onMounted(() => {
  store.profile()
  user.value = store.user

})
</script>

<style scoped>
  .profile-container {
    background-color: white;
    padding: 20px;
    color: black;
  }

  .highlighted-heading {
    color: rgb(41, 92, 150);
  }

  .product-button {
    background-color: rgb(97, 151, 212);
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
  }
</style>
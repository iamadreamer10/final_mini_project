<template>
  <h2 class="cart-header">관심 목록</h2>
  <div v-if="cartItems != null" class="cart-list">
    <div v-for="product in cartItems" :key="product.fin_prdt_cd" class="cart-item">
      <!-- {{ product }} -->
      <p class="product-name">상품명 : {{ product.fin_prdt_nm }}</p>
      <p>은행 : {{ product.kor_co_nm }}</p>
      <p>상품코드 : {{ product.fin_prdt_cd }}</p>
      <button @click="goDetail(product)" class="detail-button">상세페이지로 이동</button>
      <button @click.prevent="removeCart(product)" class="remove-button">장바구니에서 삭제</button>
      <button @click.prevent="addProduct(product)" class="add-button">해당 상품 가입</button>
      <hr>
    </div>
  </div>

  <div v-else>
    <p>현재 관심 목록이 없습니다.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'; 

const store = useCounterStore()
const router = useRouter()
const user = ref(null)
const cartItems = ref(null)
cartItems.value = JSON.parse(localStorage.getItem('cart'))

const goDetail = (product) => {
  console.log(product)
  router.push(`/productdetails/${product.fin_prdt_cd}`)
}


const removeCart = (product) => {

  // 2. 삭제할 아이템 index 검색
  const itemIdx = cartItems.value.findIndex((item) => item.fin_prdt_cd === product.fin_prdt_cd)

  // 3. 데이터 삭제
  cartItems.value.splice(itemIdx, 1)

  // 4. 삭제된 데이터를 기준으로 데이터를 반영
  localStorage.setItem('cart', JSON.stringify(cartItems.value))

  // string 형태로 보내는 방법
  // console.log(cartItems.value)
  // const financialProducts = ref([])
  // cartItems.value.forEach((element) => {
  //   financialProducts.value.push(element.fin_prdt_cd)
  // })
  // const financialProductsString = financialProducts.value.join(',')

}

const addProduct = (product) => {
  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/financial_products/put_product/`,
    data: {
      financial_products: product['fin_prdt_cd']
    },

    headers: {
        Authorization: `Token ${store.token}`
      }
  })
  .then((response)=> {
    console.log(response)
    store.profile()
    user.value = store.user
    // removeCart()
  })
  .catch((error) => {
    console.log(error)
  })
  removeCart(product)
}
</script>

<style scoped>
  .cart-header {
    color: rgb(41, 92, 150);
  }

  .cart-list {
    margin-top: 20px;
  }

  .cart-item {
    background-color: white;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 15px;
  }

  .product-name {
    font-weight: bold;
  }

  .add-button,
  .detail-button,
  .remove-button,
  add-button {
    background-color: rgb(97, 151, 212);
    color: white;
    padding: 8px 12px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-right: 10px;
  }

  .add-button:hover,
  .detail-button:hover,
  .remove-button:hover,
  add-button:hover {
    background-color: #2c3e50;
  }
</style>
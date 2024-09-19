<template>
    <tr>
      <td class="table-cell">{{  product.kor_co_nm   }}</td>
      <td class="table-cell"> 
        <RouterLink :to="{ name: 'ProductDetailView', params : { id : product.fin_prdt_cd } }" class="link-style">
          {{ product.fin_prdt_nm }}
        </RouterLink>
      </td>
      <td class="table-cell">{{ product.intr_rate['6개월'] }}</td>
      <td class="table-cell">{{ product.intr_rate['12개월'] }}</td>
      <td class="table-cell">{{ product.intr_rate['24개월'] }}</td>
      <td class="table-cell">{{ product.intr_rate['36개월'] }}</td>
      <td class="table-cell">
        <button @click="addCart(product)" class="button-style">관심목록 추가</button>
      </td>
    </tr>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router'

const props = defineProps({
  product: Object
})

const store = useCounterStore()
const router = useRouter()


const addCart = (product) => {
  // 여러 데이터 저장하기
  // 현재 localStorage 에 저장된 데이터 가져오기
  // 만약 없다면 비어있는 리스트로 초기화
  const existingCart = JSON.parse(localStorage.getItem('cart')) || []

  // 중복된 제품이 있는지 확인
  const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.fin_prdt_cd === product.fin_prdt_cd)

  // 중복이 아니라면 추가
  if(!isDuplicate) {
    alert('해당 상품을 관심목록에 추가합니다')
    existingCart.push(product)
  } else {
    alert('이미 관심목록에 포함된 상품입니다.')
  }

  // 수정된 카트 데이터를 localStorage 에 저장
  localStorage.setItem('cart', JSON.stringify(existingCart))

  // router.push({name: 'ProfileView'})
}
</script>

<style scoped>
.table-cell {
  padding: 10px;
  text-align: center;
  font-family: 'Arial', sans-serif; /* 원하는 글꼴로 변경 */
}

.link-style {
  text-decoration: none;
  color: #2c3e50; /* 링크 색상을 변경 */
  font-weight: bold;
}

.button-style {
  background-color: #3498db; /* 버튼 배경색을 변경 */
  color: #fff; /* 버튼 텍스트 색상을 변경 */
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.button-style:hover {
  background-color: #2980b9; /* 마우스 오버 시 배경색 변경 */
}
</style>
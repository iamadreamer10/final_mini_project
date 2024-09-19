<template>
  <div>
    <table class="styled-table">
      <thead>
        <tr>
          <th>은행명</th>
          <th>금융상품명</th>
          <th>6개월 이자율</th>
          <th>12개월 이자율</th>
          <th>24개월 이자율</th>
          <th>36개월 이자율</th>
          <th>비고</th>
        </tr>
      </thead>
      <tbody>
        <SavingsItem v-for="product in productInfoList" 
          :key="product.fin_prdt_cd"
          :product="product"
          />
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
import SavingsItem from '@/components/SavingsItem.vue';

const store = useCounterStore()
const products = ref(null)
const options = ref(null)
const productInfoList = ref([])

onMounted(() => {
  products.value = store.savings
  options.value = store.savingsOptions
  products.value.forEach((product) => {
    const productInfo = {
      fin_prdt_cd: product.fin_prdt_cd,
      fin_prdt_nm: product.fin_prdt_nm, 
      kor_co_nm: product.kor_co_nm,
      etc_note: product.etc_note,
      join_member: product.join_member,
      join_way: product.join_way,
      spcl_cnd: product.spcl_cnd,
      intr_rate: ref({})
      }
    options.value.forEach((option) => {
      if (option.fin_prdt_cd === product.fin_prdt_cd) {
        const term = option['save_trm'] + '개월'
        const value = option['intr_rate'] 
        if (value === -1 ){
          productInfo.intr_rate.value[term] = '없음'
        } else {
          productInfo.intr_rate.value[term] = value + '%'
        }
      } 
    })
    productInfoList.value.push(productInfo) 
  })
})
</script>

<style scoped>

.styled-table {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 18px;
  text-align: left;
}

.styled-table th,
.styled-table td {
  padding: 12px 15px;
  border-bottom: 1px solid #ddd;
  text-align: center;
}

.styled-table th {
  background-color: rgb(97, 151, 212);
  color: white;
}
</style>
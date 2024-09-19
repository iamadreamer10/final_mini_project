<template>
  <tr>
    <td class="table-cell">{{ article.id }}</td>
    <td class="table-cell"> {{ productName }}</td>
    <td class="table-cell"> {{ article.title }}</td>
    <td class="table-cell">{{ article.user.username }}</td>
    <td class="table-cell">
      <RouterLink :to="{ name: 'DetailView', params: { id : article.id } }"
       :article="article"
       class="link-style">
        <button class="button-style">상세 보기</button>
      </RouterLink>
    </td>
  </tr>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

// ArticleList로부터 받은 props 사용
const props = defineProps({
  article: Object
})

const store = useCounterStore()
const productName = ref(null)


const articleItem = function () {
  store.deposits.forEach((element) => {
    if(element['fin_prdt_cd'] === props.article.deposit){
      productName.value = element['fin_prdt_nm']
    }
  });
  store.savings.forEach((element) => {
    if(element['fin_prdt_cd'] === props.article.saving){
      productName.value = element['fin_prdt_nm']
    }
  })
}

onMounted(() => {
  store.getDeposits()
  store.getSavings()
  articleItem()
})



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
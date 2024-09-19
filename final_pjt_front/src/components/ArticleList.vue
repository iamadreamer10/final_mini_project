<template>
  <div>
    <table class="styled-table">
      <thead>
        <tr>
          <th>게시글 번호</th>
          <th>금융상품명</th>
          <th>제목</th>
          <th>작성자</th>
          <th>비고</th>
        </tr>
      </thead>
      <!-- v-for로 각 Article들에 대한 기능 구현 -->
      <tbody>
        <ArticleItem
        v-for="article in store.articles"
        :key="article.id"
        :article="article"
        />  
      </tbody>
    </table>
 


  </div>
</template>

<script setup>
// 앞의 부모한테 받아온 props 사용할거
// 또 ArticleDetail에 내려주기
import ArticleItem from '@/components/ArticleItem.vue'
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue';
const store = useCounterStore()

onMounted(() => {
  store.getArticles()
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
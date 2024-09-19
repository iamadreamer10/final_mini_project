<!-- views/ArticleView.vue -->
<template>
  <div>
    <h1>게시판</h1>  
    <RouterLink :to="{ name: 'CreateView'}" class="link-style">
      <button class="button-style">게시글 생성</button>
    </RouterLink>
    
    <!-- 게시글 검색은 어떻게..? -->
    <ArticleList />
  </div>
</template>

<script setup>
// 특정 금융 상품(어떤 은행에서 출시한 금융 상품)에 대한 게시글 관련 View
// 해당 금융 상품을 받아서, 해당 값을 외래 키로 받는 게시글들을 모아오기
// ArticleList component로 넘겨주기
import ArticleList from '@/components/ArticleList.vue'
</script>

<style scoped>
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

h1 {
  color: rgb(41, 92, 150);
}
.button-style:hover {
  background-color: #2980b9; /* 마우스 오버 시 배경색 변경 */
}
</style>
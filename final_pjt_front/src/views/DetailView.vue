<template>
  <div class="container">
    <div v-if="articleInfo">
      <table>
      <thead>
        <tr>
          <th>제목</th>
          <th>{{ articleInfo.title }}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>작성자</td>
          <td>{{ authorInfo.nickname }}</td>
        </tr>
        <tr>
          <td>상품명</td>
          <td>{{ productName }}</td>
        </tr>
        <tr>
          <td>작성일</td>
          <td>{{ articleInfo.created_at }}</td>
        </tr>
        <tr>
          <td>수정일</td>
          <td>{{ articleInfo.updated_at }}</td>
        </tr>
        <tr>
          <td>내용</td>
          <td>{{ articleInfo.content }}</td>
        </tr>
        <!-- 추가적인 속성과 내용 행을 필요에 따라 추가할 수 있습니다. -->
      </tbody>
  </table>
  <p>
    <!-- {{ authorInfo.username }}
    {{ store.user.username }} -->
    <div v-if="authorInfo.username == store.user.username">
      <RouterLink :to="{name: 'UpdateView', params: { id: articleInfo.id }}">
        <button class="update-button">게시글 수정</button>
      </RouterLink>
      <button @click="deleteArticle" class="remove-button">게시글 삭제</button>
    </div>
      </p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const props = defineProps({
  article: Object
})


const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const articleInfo = ref(null)
const productName = ref(null)
const authorInfo = ref(null)

onMounted(() => {
  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    console.log(response.data)
    articleInfo.value = response.data
    // console.log(typeof(articleInfo.value.user))
    if (articleInfo.value.deposit === null) {
      store.getSavings()
      store.savings.forEach((element) => {
      if (element['fin_prdt_cd'] === articleInfo.value.saving) {
        productName.value = element['fin_prdt_nm']
        }
      })  
    } else if (articleInfo.value.saving === null) {
      store.getDeposits()
      store.deposits.forEach((element) => {
        if(element['fin_prdt_cd'] === articleInfo.value.deposit) {
          productName.value = element['fin_prdt_nm']
        }
      })
    }
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/accounts/${articleInfo.value.user}/`
      })
        .then((response) => {
          // console.log(response.data)
          authorInfo.value = response.data
          console.log(authorInfo.value)
          console.log(store.user)
        })
        .catch((error) => {
          console.log(error)
        })
      })
  .catch((error) => {
    console.log(error)
  })

})


const deleteArticle = function () {
  axios({
    method: 'delete',
    // article_id값을 넘겨주기
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
        Authorization: `Token ${store.token}`
      }
  })
    .then((response) => {
      console.log(response)
      // DetailView에서 다시 ArticleView로 넘어가기
      router.push({ name : 'ArticleView'})
    })
    .catch((error) => {
      console.log(error)
      alert('다른 사용자의 게시글은 삭제할 수 없습니.')
    })
}
</script>

<style scoped>
  .container {
    background-color: rgb(255, 255, 255);
    padding: 20px;
    color: black;
    
  }

  .form-container {
    color: white;
    border: 1px rgb(97, 151, 212);
  }

  .comment-section {
    color: white;
  }

  table {
      border-collapse: collapse;
      width: 100%;
    }

  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }

  th {
    background-color: #f2f2f2;
  }



  .update-button,
  .remove-button,
  remove-button {
    background-color: rgb(97, 151, 212);
    color: white;
    padding: 8px 12px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-right: 10px;
  }

  .remove-button:hover,
  .update-button:hover,
  remove-button:hover {
    background-color: #2c3e50;
  }
</style>
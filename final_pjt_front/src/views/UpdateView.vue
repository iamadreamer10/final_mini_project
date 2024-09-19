<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle" class="article-form">
      <div>
        <label for="title">제목</label>
        <input id="title" v-model.trim="title" class="input-field" required>
      </div>
      <div>
        <label for="content">내용</label>
        <textarea id="content" v-model.trim="content" class="input-field" required></textarea>
      </div>
      <input type="submit" value="게시글 작성" class="submit-button">
    </form>
  </div>
</template>

<script setup>
import axios, { AxiosHeaders } from 'axios';
import { useCounterStore } from '@/stores/counter';
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()

console.log('route: ', route)
console.log('router: ',router)

const title = ref(null)
const content = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url : `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    // console.log(response.data)    
    title.value = response.data.title
    content.value = response.data.content
  })
})

const updateArticle = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization : `Token ${store.token}`
    },
    data: {
      title: title.value,
      content: content.value,
    }
  })
    .then((response) => {
      console.log(response)
      // router
      router.push({ name: 'DetailView', params: { id: route.params.id } })
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>

<style scoped>
  h1 {
    color: rgb(41, 92, 150);
  }
    .article-form {
    background-color: #e5f1fa;
    padding: 20px;
    border-radius: 10px;
    color: #000000;
  }

  label {
    display: block;
    margin-bottom: 5px;
  }

  .input-field {
    margin-bottom: 15px;
    padding: 10px;
    border-radius: 5px;
    width: calc(100% - 20px);
    box-sizing: border-box;
  }

  textarea {
    resize: vertical;
  }

  .submit-button {
    background-color: #fff;
    color: #3498db;
    padding: 10px;
    border: none;
    cursor: pointer;
    border-radius: 5px;
  }
</style>
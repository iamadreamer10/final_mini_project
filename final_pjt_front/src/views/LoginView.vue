<!-- views/LogInView.vue -->
<template>
  <h1 class="login-header">로그인</h1>
  <div class="login-container">
    <!-- form태그를 통해 사용자 입력 받기 -->
    <!-- 아이디, 비밀번호 등 html 상에서 한글이 자연스러운 단어는 한글로 보이게(label값이) -->
    <form @submit.prevent="login" class="login-form">
      <!-- 아이디 -->
      <div class="form-group">
        <label for="username">아이디  </label>
        <!-- v-model로 연결 -->
        <div>
          <input type="username" id="username" v-model.trim="username">
        </div>
      </div>
      <!-- 비밀번호 -->
      <div class="form-group">
        <label for="password">비밀번호  </label>
        <!-- v-model로 연결 -->
        <div>
          <input type="password" id="password" v-model.trim="password">
        </div>
      </div>
      <input type="submit" value="로그인" class="login-button">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const login = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  const hasNullValue = Object.values(payload).some(value => value === null) 

  if (hasNullValue) {
    alert('회원가입에 필요한 모든 내용을 작성해 주세요.') 
    } else {
      store.logIn(payload)
    }
}
</script>

<style scoped>
  .login-header {
    color: rgb(59, 130, 211);
  }

  .login-container {
    max-width: 400px;
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .login-form {
    display: flex;
    flex-direction: column;
  }

  .form-group {
    margin-bottom: 15px;
    font-weight: bold;
  }

  .login-button {
    background-color: rgb(97, 151, 212);
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

</style>
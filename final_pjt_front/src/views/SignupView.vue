<!-- views/SignupView.view -->
<template>
  <h1>회원가입</h1>
  <div>
    <!-- form태그를 통해 사용자 입력 받기 -->
    <!-- 아이디, 비밀번호 등 html 상에서 한글로 보이게(label값이) -->
    <!-- form 태그에 @submit.prevent로 연결 (뭐 연결할까? 프로필 페이지?) -->
    <form @submit.prevent="signup" class="styled-form">
      <!-- 아이디 -->
      <div class="form-group">
        <label for="username">아이디</label>
        <!-- v-model로 연결 -->
        <input type="username" id="username" v-model.trim="username">
      </div>
      <!-- 비밀번호 -->
      <div class="form-group">
        <label for="password1">비밀번호 </label>
        <!-- v-model로 연결 -->
        <input type="password1" id="password1" v-model.trim="password1">
      </div>
      <!-- 비밀번호 확인 -->
      <!-- password1과 password2가 틀릴 경우 어떻게 할까요? -->
      <div class="form-group"> 
        <label for="password2">비밀번호 재입력</label>
        <!-- v-model로 연결 -->
        <input type="password2" id="password2" v-model.trim="password2">
      </div>
      <!-- 회원 닉네임 -->
      <div class="form-group">
        <label for="nickname">닉네임</label>
        <input type="nickname" id="nickname" v-model.trim="nickname">
      </div>
      <div class="form-group">
        <label for="age">나이</label>
        <input type="age" id="age" v-model.trim="age">
      </div>
      <div class="form-group">
        <label for="money">보유 자산 </label>
        <input type="money" id="money" v-model.trim="money">
      </div>
      <!-- 연소득 -->
      <div class="form-group">
        <label for="salary">연소득 </label>
        <!-- v-model로 연결 -->
        <input type="salary" id="salary" v-model.trim="salary">
      </div>
      <input type="submit" value="회원가입" class="styled-button">
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

// Define reactive variables
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)

console.log(username.value)
// onMounted hook
onMounted(() => {
  // You can perform any initialization logic here if needed
})

// signup function
const signup = function() {
  // Define payload inside the signup function
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
  }
  const hasNullValue = Object.values(payload).some(value => value === null) 

  if (hasNullValue) {
    alert('회원가입에 필요한 모든 내용을 작성해 주세요.')
  } else {  
    // if (username)
    // Call store.signUp with the payload
    store.signUp(payload)}

}
</script>

<style scoped>
  .styled-form {
  max-width: 400px; /* Set your desired maximum width */
  /* margin: auto; Center the form on the page */
  background-color: rgb(225, 235, 243);
  padding: 20px;
  border-radius: 8px;
  color: rgb(19, 12, 87);
  font-weight: bold;
  }

  .styled-form label {
    display: block;
    margin-bottom: 5px;
  }

  .styled-form input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border-radius: 8px;
  }

  .form-group {
    margin: 15px;
    
  }

  .styled-button {
    background-color: rgb(97, 151, 212);
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  .background {
    background-color: white;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  label {
    display: inline-block;
    width: 120px; /* Adjust the label width as needed */
  }

  input {
    width: calc(100% - 130px); /* Adjust the input width as needed */
  }
</style>
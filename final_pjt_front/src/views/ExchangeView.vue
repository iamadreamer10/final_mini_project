<template>
  <div>
    <h1 >환율 계산기</h1>
  </div>
  <div>
    <div class="exchange-container">
      <div class="input-container">
        <label for="">국가 선택</label>
        <select v-model="current" class="select-box">
          <option v-for="foreignCurrent in foreignCurrents" :key="foreignCurrent.cur_info"> {{ foreignCurrent.cur_info }}</option>
        </select>
      </div>
      <div>
        <label for="">값 입력</label>
        <input type="text" id="foreign-current" v-model="inputValue" class="text-input">
      </div>
    </div>
    <button @click.prevent="exchange(current, inputValue)" class="calculate-button">환율 계산</button>
  </div>
  <div>
    <h3 v-if="won" class="result-text">
      계산 결과:  {{ won }} 원 입니다.
    </h3>
    <h3 v-else class="result-text">
      값을 입력해주세요!!
    </h3>
  </div>

</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  const store = useCounterStore()
  const foreignCurrents = ref(null)
  const current = ref(null)
  const won = ref(null)
  const inputValue = ref(null)
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/exchange_rates/`
    })
    .then((response) => {
      // console.log(response.data)
      foreignCurrents.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  })

  const exchange = function(current, val) {
    if (isNaN(val) || val === null) {
      alert('숫자를 기입해 주세요.');
      inputValue.value = null;
      return;
    }
    foreignCurrents.value.forEach((element) => {
      if (element.cur_info === current) {
        // console.log(element)
        won.value = ((val*element.bkpr)/element.unit).toLocaleString()
        }
      })
  }
</script>

<style scoped> 
  h1 {
    color: rgb(41, 92, 150);
  }

  body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f5f5f5;
  }

  label {
    color: #0e4268;
    margin: 10px;
    font-weight: bold;
  }
  /* 섹션 타이틀 스타일 */
  .section-title {
    color: #333;
    margin-bottom: 10px;
  }

  .exchange-container {
    background-color: #c4def0;
    border-radius: 8px;
    padding: 20px;
    max-width: 400px; /* 최대 너비를 조절 */
    margin-bottom: 10px;
  }

  .input-container {
    display: flex;
    gap: 10px;
    justify-content: flex-end; /* 오른쪽 정렬 추가 */
    margin-bottom: 20px;
  }

  /* 선택 박스 스타일 */
  .select-box,
  .text-input {
    padding: 10px;
    font-size: 14px;
    flex: 1;
  }

  /* 계산 버튼 스타일 */
  .calculate-button {
    padding: 8px 16px;
    background-color: #3498db;
    color: #fff;
    border: none;
    cursor: pointer;
    font-size: 14px;
    border-radius: 5px;
  }

  /* 계산 결과 텍스트 스타일 */
  .result-text {
    color: #333;
  }
</style>
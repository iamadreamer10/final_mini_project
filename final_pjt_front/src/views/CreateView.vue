<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle" class="article-form">
      <div>
        <label for="title">제목</label>
        <input type="title" id="title" v-model.trim="title" class="input-field">
      </div>
      <div>
        <label for="content">내용</label>
        <textarea id="content" v-model.trim="content" class="input-field"></textarea>
      </div>
      <!-- <label for="">상품 종류</label> -->
      <select v-model="select" class="input-field">
        <option value="예금">예금</option>
        <option value="적금">적금</option>
      </select>
      <!-- <label for="">상품 이름</label> -->
      <div v-if="select==='예금'">
        <!-- v-if로 현재 적금에 대한 게시글인지 예금에 대한 게시글인지 -->
        <select v-model="selectedDeposit" id="product-options" class="input-field"> 
          <option v-for="deposit in depositNameList">
              {{ deposit[1]  + '(' + deposit[0] + ')'  }}
          </option>
        </select>
      </div>
      <div v-else>
        <select v-model="selectedSaving" id="product-options" class="input-field"> 
          <option v-for="saving in savingNameList">
              {{ saving[1] + '(' + saving[0] + ')'}}
          </option>
        </select>
      </div>
      <input type="submit" value="게시글 작성" class="submit-button">
    </form>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter';
  import axios from 'axios'
  import { useRouter } from 'vue-router'

  // 필요한 내용
  const router = useRouter()
  
  const store = useCounterStore()

  // 게시글 제목, 내용
  const title = ref(null)
  const content = ref(null)

  // 예금/적금 선택
  const select = ref(null)
  
  // 예금상품 목록
  const depositNameList = ref([])
  const selectedDeposit = ref('')
  
  // 적금상품 목록
  const savingNameList = ref([])
  const selectedSaving = ref('')

  onMounted(() => {
    store.getDeposits()
    store.getSavings()
  })  
  
  store.deposits.forEach((element) => {
    depositNameList.value.push([element['fin_prdt_cd'], element['fin_prdt_nm']])
  });
  
  store.savings.forEach((element) => {
    savingNameList.value.push([element['fin_prdt_cd'], element['fin_prdt_nm']])
  })

  const deposit = ref(null)
  const saving = ref(null)

  const createArticle = function () {
    let regex = /\(([\w-]+)\)/;  // 괄호 안의 숫자, 알파벳, 대시를 포함하는 문자열을 캡처하는 정규표현식   
    
    if (selectedDeposit.value === '') {
      let match2 = selectedSaving.value.match(regex)
      saving.value = match2[1]
    } 
    if (selectedSaving.value === '') {
      let match1 = selectedDeposit.value.match(regex)
      deposit.value = match1[1]
    }

    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/articles/`,
      data: {
        title: title.value,
        content: content.value,
        deposit: deposit.value,
        saving: saving.value,
      },
      headers: {
          Authorization:`Token ${store.token}`
        }
      })
      .then((res) => {
        title.value = null
        content.value = null
        deposit.value = null
        saving.value = null
        select.value = null
        selectedDeposit.value = null
        selectedSaving.value = null
        
        router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
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
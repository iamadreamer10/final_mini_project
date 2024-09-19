<!-- views/HomeView.vue -->
<template>
  <div>
    <nav class="navbar">
      <div class="nav-container">
        <div v-if="store.isLogin" class="nav-links-container">
          <div class="nav-links">
            <RouterLink :to="{ name: 'BankView' }" class="nav-link">금융상품 비교</RouterLink> 
            <RouterLink :to="{ name : 'ArticleView' }" class="nav-link">게시글 작성</RouterLink> 
            <RouterLink :to="{ name : 'MapView'}" class="nav-link">지도 검색</RouterLink> 
            <RouterLink :to="{ name : 'ProfileView'}" class="nav-link">내 프로필</RouterLink>
            <RouterLink :to="{ name : 'ExchangeView'}" class="nav-link">환율 계산기</RouterLink>
          </div>
          <div class="logout-container">
            <form @submit.prevent="store.logOut" class="logout-form">
              <button class="logout-button">로그아웃</button>
            </form>
          </div>
        </div>
      </div>
    </nav>
    <RouterView/>

    <!-- 수정한 부분 시작 -->
    <div v-if="store.isLogin">
    <!-- </Recommend> -->
    <h3>비슷한 나이대의 사용자 추천 목록</h3>
    <ol>
      <li v-for="item in recommendedAgeList2" :key="item.key">
        <RouterLink :to="{ name: 'ProductDetailView', params : { id : item.key }}">{{ item.value }}</RouterLink>
      </li>
    </ol>
    <hr>
    <h3>비슷한 자산의 사용자 추천 목록</h3>
    <ol>
      <li v-for="item in recommendedMoneyList2" :key="item.key">
        <RouterLink :to="{ name: 'ProductDetailView', params : { id : item.key }}">{{ item.value }}</RouterLink>
      </li>
    </ol>
    <hr>
    <h3>비슷한 연봉의 사용자 추천 목록</h3>
    <ol>
      <li v-for="item in recommendedSalaryList2" :key="item.key">
        <RouterLink :to="{ name: 'ProductDetailView', params : { id : item.key }}">{{ item.value }}</RouterLink>
      </li>
    </ol>
  </div>
  <hr>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'

const store = useCounterStore()
store.deposits.forEach((element) => {
})
// const depositObjList = ref(null)
// const savingObjList = ref(null)

const recommendedAgeList = ref([])
const recommendedMoneyList = ref([])
const recommendedSalaryList = ref([])

onMounted(() => {
  store.getDeposits
  store.getSavings
  // depositObjList.value = store.deposits
  // savingObjList.value = store.savings
  store.recommendAge()
  store.recommendMoney()
  store.recommendSalary()
})

// 객체를 원소로 하는 배열을 value 값 기준으로 정렬
const sortByValue = function (list) {
  return list.sort((a, b) => b.value - a.value)
}
const orderedRecommendedList = function(list) {
  return sortByValue(list)
}

// 객체를 리스트로 변환
const toList = function (obj) {
  return Object.keys(obj).map(key => ({ key, value: obj[key] })) 
}
recommendedAgeList.value = orderedRecommendedList(toList(store.ageList))
recommendedMoneyList.value = orderedRecommendedList(toList(store.moneyList))
recommendedSalaryList.value = orderedRecommendedList(toList(store.salaryList))

store.deposits.forEach((element) => {
  // console.log(element.fin_prdt_nm)
})

const recommendedAgeList2 = ref([])
const recommendedMoneyList2 = ref([])
const recommendedSalaryList2 = ref([])

recommendedAgeList.value.forEach((element1) => {
  store.deposits.forEach((element2) => {
    if (element1.key == element2.fin_prdt_cd) {
      recommendedAgeList2.value.push({ 'key': element1.key, 'value' : element2.fin_prdt_nm })
    }
  })
  store.savings.forEach((element2) => {
    if (element1.key == element2.fin_prdt_cd) {
      recommendedAgeList2.value.push({ 'key': element1.key, 'value' : element2.fin_prdt_nm })
    }
  })  
})

recommendedMoneyList.value.forEach((element1) => {
  store.deposits.forEach((element2) => {
    if (element1.key == element2.fin_prdt_cd) {
      recommendedMoneyList2.value.push({ 'key': element1.key, 'value' : element2.fin_prdt_nm })
    }
  })
  store.savings.forEach((element2) => {
    if (element1.key == element2.fin_prdt_cd) {
      recommendedMoneyList2.value.push({ 'key': element1.key, 'value' : element2.fin_prdt_nm })
    }
  })  
})

recommendedSalaryList.value.forEach((element1) => {
  store.deposits.forEach((element2) => {
    if (element1.key == element2.fin_prdt_cd) {
      recommendedSalaryList2.value.push({ 'key': element1.key, 'value' : element2.fin_prdt_nm })
    }
  })
  store.savings.forEach((element2) => {
    if (element1.key == element2.fin_prdt_cd) {
      recommendedSalaryList2.value.push({ 'key': element1.key, 'value' : element2.fin_prdt_nm })
    }
  })  
})

</script>

<style>
.navbar {
  background-color: rgb(97, 151, 212); /* 파란색 배경색 */
  color: #ffffff; /* 흰색 텍스트 */
  padding: 10px 0; /* 상하로 10px 간격 */
}

.nav-links-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}


.nav-container {
  max-width: 1200px; /* 최대 너비 */
  margin: 0 auto; /* 가운데 정렬 */
  display: flex; /* 자식 요소들을 수평으로 배치 */
  justify-content: space-between; /* 자식 요소 사이의 간격을 최대화하여 배치 */
  align-items: center; /* 수직으로 가운데 정렬 */
}

.nav-links {
  display: flex; /* 자식 요소들을 수평으로 배치 */
  margin-left: 20px; /* 왼쪽 여백 추가 */
}

.nav-link {
  color: #ffffff; /* 흰색 텍스트 */
  font-family: 'Arial', sans-serif; /* 원하는 글씨체로 변경 */
  margin-right: 10px; /* 각 링크 사이 간격 조정 */
  text-decoration: none; /* 기본 링크 밑줄 제거 */
}

.logout-form {
  margin: 0; /* 폼의 기본 마진 제거 */
}

.logout-container {
  margin-left: auto;
}

.logout-button {
  background-color: #ffffff; /* 흰색 배경색 */
  color: #004884; /* 파란색 텍스트 */
  border: none; /* 테두리 제거 */
  padding: 8px 15px; /* 내부 패딩 조정 */
  cursor: pointer; /* 포인터로 나타내어 클릭 가능하도록 설정 */
  font-family: 'Arial', sans-serif; /* 원하는 글씨체로 변경 */
  border-radius: 20px; /* 버튼의 둥근 테두리 반경 설정 */
}

.user-info {
  margin-top: 20px; /* 유저 정보와 내용 간격 조정 */
}
</style>
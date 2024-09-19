<template>
  <div>
    <h1>상품 소개</h1>
    <table>
      <thead>
        <tr>
          <th>상품명</th>
          <th>{{ fin_prdt_nm }}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>상품 코드</td>
          <td>{{ fin_prdt_cd  }}</td>
        </tr>
        <tr>
          <td>금융회사명</td>
          <td>{{ kor_co_nm }}</td>
        </tr>
        <tr>
          <td>가입 대상</td>
          <td>{{ join_member }}</td>
        </tr>
        <tr>
          <td>가입 방법</td>
          <td>{{ join_way }}</td>
        </tr>
        <tr>
          <td>우대 조건</td>
          <td>{{ spcl_cnd }}</td>
        </tr>
        <tr>
          <td>기타 유의사항</td>
          <td>{{ etc_note }}</td>
        </tr>
        <!-- 추가적인 속성과 내용 행을 필요에 따라 추가할 수 있습니다. -->
      </tbody>
    </table>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter' 
  import { useRoute } from 'vue-router'
  import axios from 'axios'

  const store = useCounterStore()
  const route = useRoute()
  const fin_prdt_cd = ref(null)
  const fin_prdt_nm = ref(null)
  const kor_co_nm = ref(null)
  const etc_note = ref(null)
  const join_member = ref(null)
  const join_way = ref(null)
  const spcl_cnd = ref(null)


  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/financial_products/get_product_detail/${route.params.id}/`
    })
      .then((response) => {
        console.log(response)
        const product = response.data
        fin_prdt_cd.value = product.fin_prdt_cd
        fin_prdt_nm.value = product.fin_prdt_nm
        kor_co_nm.value = product.kor_co_nm
        etc_note.value = product.etc_note
        join_member.value = product.join_member
        join_way.value = product.join_way
        spcl_cnd.value = product.spcl_cnd
        
      })
      .catch((error) => {
        console.log(error)
      })
  })
</script>

<style scoped>
  h1 {
    color: rgb(41, 92, 150);
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
</style>
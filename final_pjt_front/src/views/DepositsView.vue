
<template>
  <h1>예금상품 비교</h1>
  <DepositList />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
import DepositList from '@/components/DepositList.vue'
const store = useCounterStore()


onMounted(() => {
  store.getDeposits()
  store.getDepositsOptions()
})

</script>

<style scoped>
  table, tr, td {
    border: 1px solid;
  }
</style>
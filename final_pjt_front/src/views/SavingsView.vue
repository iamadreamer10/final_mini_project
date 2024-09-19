<!-- views/BankView.vue -->
<template>
    <h1>적금상품 비교</h1>
    <SavingsList/>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
import SavingsList from '@/components/SavingsList.vue';

const store = useCounterStore()


onMounted(() => {
  store.getSavings()
  store.getSavingsOptions()
})

</script>

<style scoped>
  table, tr, td {
    border: 1px solid;
  }
</style>
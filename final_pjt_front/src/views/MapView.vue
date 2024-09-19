<template>
  <div>
    <h1 class="map-header">내 주변 은행 찾기</h1>  
  </div>
  <KakaoMap/>

</template>

<script setup>
import KakaoMap from '@/components/KakaoMap.vue';
</script>

<style scoped>
  .map-header {
    text-align: center;
    color: rgb(41, 92, 150);
  }
</style>
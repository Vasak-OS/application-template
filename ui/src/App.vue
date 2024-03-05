<script setup lang="ts">
import { inject, onMounted } from 'vue';
import { WindowFrame } from '@vasakgroup/vue-libvasak';
import HelloWorld from './components/HelloWorld.vue';

const $vsk: any = inject('vsk');

onMounted(() => {
  $vsk.loadUIConfig();
});
</script>

<template>
  <WindowFrame title="Application Template" image="https://os.vasak.net.ar/img/logo.svg">
    <div class="flex">
      <HelloWorld />
    </div>
  </WindowFrame>
</template>

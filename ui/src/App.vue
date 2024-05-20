<script setup lang="ts">
import { inject, onMounted } from 'vue';
import { WindowFrame } from '@vasakgroup/vue-libvasak';
import HelloWorld from '@/components/HelloWorld.vue';
import type { VSK } from '@/types/VSK';

const $vsk: VSK = inject('vsk') as VSK;

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

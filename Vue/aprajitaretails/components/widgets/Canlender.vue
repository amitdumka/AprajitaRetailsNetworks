<template>
  <CalendlyPopupWidget v-bind="options" :root-element="rootElement" />

  <!-- Can be any element -->
  <div ref="rootElement" />
</template>

<script lang="ts" setup>
const rootElement = ref()
const options = {
  url: 'https://calendly.com/YOUR_LINK/30min',
  text: 'Schedule time with me',
}
</script>

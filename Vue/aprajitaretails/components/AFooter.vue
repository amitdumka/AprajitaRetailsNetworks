<script setup lang="ts">
const links = [{
  label: 'Aprajita Retails',
  to: 'https://www.aprajitaretails.in/'
}, {
  label: 'About Us',
  to: 'https://www.aprajitaretails.in/about-us'
}, {
  label: 'Contact Us',
  to: 'https://www.aprajitaretails/contact-us'
}]

// const config=[{
//   wrapper: 'relative',
//   top: {
//     wrapper: '',
//     container: 'py-8 lg:py-12'
//   },
//   bottom: {
//     wrapper: '',
//     container: 'py-8 lg:py-4 lg:flex lg:items-center lg:justify-between lg:gap-x-3',
//     left: 'flex items-center justify-center lg:justify-start lg:flex-1 gap-x-1.5 mt-3 lg:mt-0 lg:order-1',
//     center: 'mt-3 lg:mt-0 lg:order-2 flex items-center justify-center',
//     right: 'lg:flex-1 flex items-center justify-center lg:justify-end gap-x-1.5 lg:order-3'
//   }
// }]

</script>

<template>
  <UFooter :links="links">
    <template #left>
      Copyright © {{ new Date().getFullYear() }}, build by Amit Kumar
    </template>

    <template #right>
      <UButton icon="i-simple-icons-x" color="gray" variant="ghost" to="https://x.com/amitdumka" target="_blank" />
      <UButton icon="i-simple-icons-facebook" color="gray" variant="ghost" to="https://facebook.com/aprajitaretails" target="_blank" />
      <UButton icon="i-simple-icons-github" color="gray" variant="ghost" to="https://github.com/nuxt/nuxt" target="_blank" />
    </template>
  </UFooter>
</template>


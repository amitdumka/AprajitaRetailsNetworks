// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  //extends: [process.env.NUXT_UI_PRO_PATH || '@nuxt/ui-pro'],
  extends:['./modules/ui-nxt'],
  modules: [
    '@nuxt/ui',
    '@nuxt/fonts',
    '@vueuse/nuxt'
  ],
  ui: {
    icons: ['heroicons', 'simple-icons'],
    safelistColors: ['primary', 'red', 'orange', 'green']
  },
  devtools: {
    enabled: true
  }
})

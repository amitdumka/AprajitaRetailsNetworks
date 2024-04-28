// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  //extends: [process.env.NUXT_UI_PRO_PATH || '@nuxt/ui-pro'],
  extends:['./modules/ui-nxt'],
  modules: [
    '@nuxt/ui',
    '@nuxt/fonts',
    //'@productdevbook/chatwoot',
    'nuxt-snackbar',
    '@vueform/nuxt',
    // 'nuxt-primevue',
    //'@vueform/builder-nuxt',
    //'nuxt-calendly',
    //'@samk-dev/nuxt-vcalendar',
    //'@nuxtjs/supabase',
    '@pinia/nuxt',
    '@vueuse/nuxt'
  ],
  ui: {
    icons: ['heroicons', 'simple-icons'],
    safelistColors: ['primary', 'red', 'orange', 'green']
  },
  devtools: {
    enabled: true
  },
  build: {
    transpile: ['@syncfusion']
  },
  // chatwoot: {
  //   init: {
  //     websiteToken: 'b6BejyTTuxF4yPt61ZTZHjdB'
  //   },
  //   settings: {
  //     locale: 'en',
  //     position: 'left',
  //     launcherTitle: 'Hello Chat',
  //     // ... and more settings
  //   },
  //   // If this is loaded you can make it true, https://github.com/nuxt-modules/partytown
  //   partytown: false,
  // },
//   primevue: {
//     /* Options */
// }

})

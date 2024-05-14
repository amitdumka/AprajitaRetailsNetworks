// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  //extends: [process.env.NUXT_UI_PRO_PATH || '@nuxt/ui-pro'],
  extends: ['./modules/ui-nxt'],
  modules: ['@nuxt/ui', '@nuxt/fonts',
    'nuxt-snackbar', '@vueform/nuxt', // 'nuxt-primevue',
    //'@vueform/builder-nuxt',
    //'nuxt-calendly',
    '@samk-dev/nuxt-vcalendar', //'@nuxtjs/supabase',
    '@sidebase/nuxt-auth',
    '@pinia/nuxt',
    '@vueuse/nuxt'],

  ui: {
    icons: ['heroicons', 'simple-icons'],
    safelistColors: ['primary', 'red', 'orange', 'green']
  },
  devtools: {
    enabled: true
  },

  build: {
    transpile: ['@syncfusion','jsonwebtoken']

  },

  experimental: {
    renderJsonPayloads: true
  },
  auth: {
    provider: {
      type: 'local',
      endpoints: {
        getSession: { path: '/user' }
      },
      pages: {
        login: '/auth/LoginPage'
      },
      token: {
        signInResponseTokenPointer: '/token/accessToken'
      },
      sessionDataType: { id: 'string', email: 'string', name: 'string', role: '\'admin\' | \'guest\' | \'account\'', subscriptions: '{ id: number, status: \'ACTIVE\' | \'INACTIVE\' }[]' }
    },
    session: {
      // Whether to refresh the session every time the browser window is refocused.
      enableRefreshOnWindowFocus: true,

      // Whether to refresh the session every `X` milliseconds. Set this to `false` to turn it off. The session will only be refreshed if a session already exists.
      enableRefreshPeriodically: 5000
    },
    globalAppMiddleware: {
      isEnabled: true
    }
  },
  routeRules: {
    '/with-caching': {
      swr: 86400000,
      auth: {
        disableServerSideAuth: true
      }
    }
  }
})

import { createResolver } from '@nuxt/kit'
const { resolve } = createResolver(import.meta.url)

export default defineNuxtConfig({
  alias: { '#ui-nxt': resolve('./') },
  components: [
    { path: '#ui-nxt/components', prefix: 'U', pathPrefix: false }
  ],
  css: [
    '#ui-nxt/assets/css/main.css',
    '#ui-nxt/assets/css/scrollbars.css'
  ],
  vite: {
    optimizeDeps: {
      include: ['vue3-smooth-dnd']
    }
  }
})

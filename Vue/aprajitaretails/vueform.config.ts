// vueform.config.(js|ts)

import en from '@vueform/vueform/locales/en'
import vueform from '@vueform/vueform/dist/vueform'
//import tailwind from '@vueform/vueform/dist/tailwind'
//import tailwindMaterial from '@vueform/vueform/dist/tailwind-material'
import { defineConfig } from '@vueform/vueform'
// You might place these anywhere else in your project
import '@vueform/vueform/dist/vueform.css'

export default defineConfig({
  theme: vueform,
  //theme: tailwind,
  //theme: tailwindMaterial,
  locales: { en },
  locale: 'en',

})


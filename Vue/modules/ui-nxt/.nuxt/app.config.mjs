
import { updateAppConfig } from '#app/config'
import { defuFn } from 'defu'

const inlineConfig = {
  "nuxt": {
    "buildId": "bcd042f1-61bd-4a3c-bea2-a3ba132ccf83"
  }
}

// Vite - webpack is handled directly in #app/config
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    updateAppConfig(newModule.default)
  })
}

import cfg0 from "C:/DevArea/AprajitaRetailsNetworks/Vue/aks-ui/app.config.ts"

export default /*@__PURE__*/ defuFn(cfg0, inlineConfig)

import { defineStore } from 'pinia'
export const useUserLocalStore = defineStore('userLocal', () => {

  const user = ref({})
  function setUser(usr) {
    user.value = usr
  }

  // Resetting State
  function $reset() {
    user.value = {}
  }

  return { user, setUser, $reset }
},
  {
    persist: {
      storage: persistedState.localStorage
    }
  }
)

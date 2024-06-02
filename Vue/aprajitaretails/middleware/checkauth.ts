// import { useAuthLocalStore } from '~/stores/authLocalStore'
// import { useUserLocalStore } from '~/stores/userLocal'

// export default defineNuxtRouteMiddleware(async (_to, _from) => {
//   const authStore = useAuthLocalStore()
//   const userStore = useUserLocalStore()
//   const baseUrl = 'http://localhost:8000/api/account/'
//   const csrfToken = useCookie('csrftoken')
//   const response = await $fetch(baseUrl + 'checkauth/', {
//     method: 'GET',
//     headers: {
//       'Content-Type': 'application/json',
//       'X-CSRFToken': csrfToken.value,
//     },
//     credentials: 'include',
//   })

//   if (!response.isAuthenticated) {
//     authStore.setAuthenticated(false)
//     authStore.$reset()
//     userStore.$reset()
//     return navigateTo('/auth/LoginPage', { replace: true })
//   }

// })

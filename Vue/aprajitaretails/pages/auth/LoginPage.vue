<script setup lang="ts">

const { signIn, token, data, status, lastRefreshedAt } = useAuth()

console.log(data, status, lastRefreshedAt, token)
definePageMeta({
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/'
  }
})
definePageMeta({
  layout: 'auth'
})
const title = 'Aadwika Fashion'
const icon = 'i-heroicons-lock-closed'
//const description = 'Login to your account'
const buttonLable = 'Login'
const buttonIcon = 'i-heroicons-arrow-right-20-solid'


useSeoMeta({
  title: 'Login'
})

const fields = [{
  name: 'email',
  type: 'text',
  label: 'User Name',
  placeholder: 'Enter your username'
}, {
  name: 'password',
  label: 'Password',
  type: 'password',
  placeholder: 'Enter your password'
}]

const validate = (state: any) => {
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Email is required' })
  if (!state.password) errors.push({ path: 'password', message: 'Password is required' })
  return errors
}

const providers = [{
  label: 'Continue with GitHub',
  icon: 'i-simple-icons-github',
  color: 'white' as const,
  click: () => {
    console.log('Redirect to GitHub')
    //:providers="providers"

  }
}]

async function onSubmit(data: any) {
  console.log('Submitted', data)
  console.log(data.email, data.password)

  const { error, url } = await signIn({ username: data.email, password: data.password }, { callbackUrl: '/' })
  if (error) {
    alert('Not able to Login, Error: '+error)
    console.log(error)
  } else {

    return navigateTo(url, { external: true })
  }


}
</script>

<!-- eslint-disable vue/multiline-html-element-content-newline -->
<!-- eslint-disable vue/singleline-html-element-content-newline -->
<template>
  <UCard class="max-w-sm w-full mx-auto mt-16 center bg-white/75  dark:bg-white/5 backdrop-blur">
    <UAuthForm :fields="fields" :validate="validate" :title="title" align="top" :icon="icon"
      :ui="{ base: 'text-center', footer: 'text-center' }"
      :submit-button="{ trailingIcon: buttonIcon, label: buttonLable }" @submit="onSubmit">
      <template #description>
        Don't have an account? <NuxtLink to="/signup" class="text-primary font-medium">Sign up</NuxtLink>.
      </template>

      <template #password-hint>
        <NuxtLink to="/" class="text-primary font-medium">Forgot password?</NuxtLink>
      </template>
      <template #footer>
        By signing in, you agree to our <NuxtLink to="/" class="text-primary font-medium">Terms of Service</NuxtLink>.
      </template>
    </UAuthForm>
  </UCard>
</template>

<script lang="ts">
async function test(username: string, password: string) {
  console.log(username, password)
  const todo
    = await $fetch('http://localhost:8000/api/clients/', {
        method
          : 'GET',

      })

  return todo

}
</script>

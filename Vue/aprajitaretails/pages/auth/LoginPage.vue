<script setup lang="ts">
import type { FormError } from '#ui/types'
import { ref } from 'vue'
import { definePageMeta, useAuth } from '#imports'

const { signIn, token, data, status, lastRefreshedAt } = useAuth()


definePageMeta({
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/'
  }
})
const title = 'Aadwika Fashion'
const icon = 'i-heroicons-lock-closed'


const fields = [{
  name: 'username',
  type: 'text',
  label: 'User Name',
  placeholder: 'Enter your username'
}, {
  name: 'password',
  label: 'Password',
  type: 'password',
  placeholder: 'Enter your password'
}, {
  name: 'remember',
  label: 'Remember me',
  type: 'checkbox'
}]

const validate = (state: any) => {
  const errors: FormError[] = []
  if (!state.username) errors.push({ path: 'username', message: 'Username is required' })
  if (!state.password) errors.push({ path: 'password', message: 'Password is required' })
  return errors
}

const providers = [{
  label: 'Continue with GitHub',
  icon: 'i-simple-icons-github',
  color: 'white' as const,
  click: () => {
    console.log('Redirect to GitHub')
  }
}]

async function onSubmit(dataForm: any) {
  console.log('Submitted', dataForm)
  signIn({ username: dataForm.username, password: dataForm.password })
}
</script>

<!-- eslint-disable vue/multiline-html-element-content-newline -->
<!-- eslint-disable vue/singleline-html-element-content-newline -->
<template>
  <UCard class="max-w-sm w-full mx-auto center">
    <UAuthForm :fields="fields" :validate="validate" :providers="providers" :title="title" align="top" :icon="icon"
      :ui="{ base: 'text-center', footer: 'text-center' }" @submit="onSubmit">
      <template #description>
        Don't have an account? <NuxtLink to="/" class="text-primary font-medium">Sign up</NuxtLink>.
      </template>

      <template #password-hint>
        <NuxtLink to="/" class="text-primary font-medium">Forgot password?</NuxtLink>
      </template>
      <!-- <template #validation>
        <UAlert color="red" icon="i-heroicons-information-circle-20-solid" title="Error signing in" />
      </template> -->
      <template #footer>
        By signing in, you agree to our <NuxtLink to="/terms" class="text-primary font-medium">Terms of Service
        </NuxtLink>.
      </template>
    </UAuthForm>
  </UCard>
</template>


<!-- function useAuthApi(arg0: string, arg1: string, formData: any): { data: any; pending: any; error: any; refresh: any }|PromiseLike<{ data: any; pending: any; error: any; refresh: any }> {
  throw new Error('Function not implemented.')
} -->

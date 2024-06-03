import { useFetch } from 'nuxt/app'
export default async function authDjango(username: any, password: any) {
 // throw new Error('Function not implemented.')
  //TODO: Write the Django auth logic here
  const { data, pending, error, refresh } = await useFetch('http://localhost:8000/login/jwt/', {
     async onRequest({ request, options }) {
  //     // Set the request headers
       options.headers = {
         ...options.headers,
         'Content-Type': 'application/json',
       },
         options.method = 'POST',
         options.body = {username: username, password: password}
     },
     onResponseError({ request, response, options }) {
       // Handle the response errors

     }
   })
   return { data, pending, error, refresh }
}


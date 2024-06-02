import { useFetch } from 'nuxt/app'

export default async (username: string, password: string) => {

  const { data, pending, error, refresh } = await useFetch('http://localhost:8000/login/jwt/', {
    async onRequest({ request, options }) {
      // Set the request headers
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



// const {data, error} =await loginTest(ldata.email, ldata.password)

//   if (error) {
//     alert('You have made a terrible mistake while entering your credentials')
//   } else {
//     alert('Login Successful')
//     alert(data)

//     console.log(data, error)

//   }

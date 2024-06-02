/* eslint-disable @typescript-eslint/no-unused-vars */
export default async (serverURL: string, method: 'POST', credentials: any) => {
  serverURL = 'http://localhost:8000/'
  const { data, pending, error, refresh } = await useFetch(serverURL+'login/jwt/', {
    async onRequest({ request, options }) {

      // let csrfToken = useCookie('csrftoken')
      // if(csrfToken.value === undefined){
      //   await useFetch(serverURL + 'csrf_cookie/', { credentials: 'include' })
      //   csrfToken = useCookie('csrftoken')
      // }
      // Set the request headers
      options.headers = {
        ...options.headers,
        'Content-Type': 'application/json',
        //'X-CSRFToken': csrfToken.value
      },
        //options.credentials = 'include',
        options.method = method,
        options.body = credentials

    },
    onRequestError({ request, options, error }) {
      // Handle the request errors
    },
    onResponse({ request, response, options }) {
      // Process the response data
      localStorage.setItem('token', response._data.token)
    },
    onResponseError({ request, response, options }) {
      // Handle the response errors

    }
  })
  return { data, pending, error, refresh }

}

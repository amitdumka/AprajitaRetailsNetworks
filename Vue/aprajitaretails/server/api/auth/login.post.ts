import { createError, eventHandler, readBody } from 'h3'
import { z } from 'zod'
import { sign } from 'jsonwebtoken'
import authDjango from './authDjango'

const refreshTokens: Record<number, Record<string, any>> = {}
//TODO: this SECRET need to paramaterize
export const SECRET = 'dummy'


//TODO: Handle the login request pass it to Django and check the credentials
export default eventHandler(async (event) => {
  // const result = z.object({ username: z.string().min(1), password: z.literal('admin') }).safeParse(await readBody(event))
  // if (!result.success) {
  //   throw createError({ statusCode: 403, statusMessage: 'Unauthorized, hint: try `admin` as password' })
  // }

  const result = z.object({ username: z.string().min(1), password: z.string().min(5) }).safeParse(await readBody(event))
  if(!result.success) {
    throw createError({ statusCode: 403, statusMessage: 'Unauthorized, hint: username & password cirteria doesnt match' })
  }

  // TODO : Write the Django login logic here
  const { data, pending, error, refresh } = await authDjango(result.data.username, result.data.password)
  if(error) {
    throw createError({ statusCode: 403, statusMessage: 'Unauthorized, hint: username & password cirteria doesnt match' })
  }
 
  //TODO: this need to be paramaterized and should be fetched from Django
  const expiresIn = 1500
  //const refreshToken = Math.floor(Math.random() * (1000000000000000 - 1 + 1)) + 1

  const refreshToken = data?.token
  const { username } = result.data
  const user = {
    username,
    picture: 'https://github.com/nuxt.png',
    name: 'User ' + username
  }

  const accessToken = sign({ ...user, scope: ['test', 'user'] }, SECRET, { expiresIn })
  refreshTokens[refreshToken] = {
    accessToken,
    user
  }

  return {
    token: {
      accessToken,
      refreshToken
    }
  }
})

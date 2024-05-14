declare module "@auth/core/types" {
  interface Session {
    user?: User
  }
  interface User {
    role: string, 
    storeCode: string
  }
}

export {}

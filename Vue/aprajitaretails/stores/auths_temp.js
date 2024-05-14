// /**
//  * This store is used for storing the user information.
//  * Author: Amit Kumar
//  * Date: 29/04/2024
//  */

// import { defineStore ,acceptHMRUpdate } from 'pinia'

// export const useAuth = defineStore('auth', {

//   id: 'auth',
//   state: () => ({

//     user: {
//       isAuthenicated: false,
//       name: '',
//       email: '',
//       token: '',
//       storeCode: '',
//       clientCode: '',
//       groupCode: '',
//       role: '',
//     },
//     testing: true,
//   }),
//   getters: {

//       clientDetail(){
//         return {
//           storeCode: this.user.storeCode,
//           clientCode: this.user.clientCode,
//           groupCode: this.user.groupCode
//         }
//       },
//       userDetail(){
//         return {name:this.user.name,role: this.user.role}
//       },
//       authDetail(){
//         return {name:this.user.name,role: this.user.role, isAuthenicated: this.user.isAuthenicated,
//         token: this.user.token
//         }
//       }
//   },
//   actions: {

//     defaultStore(){
//       const userInfo={
//         name: 'Aadwika Fashion',
//         email: 'admin@aadwikafashion.in',
//         token: 'xyba5689hhjhds98dasd',
//         storeCode: 'AFD',
//         clientCode: 'AFD',
//         groupCode: 'MBO',
//         role: 'admin',
//       }
//       this.setUser(userInfo)
//     },
//     enableTesing(){
//         if(this.testing){
//           this.defaultStore()
//         }
//     },
//     initStore() {
//       this.user.isAuthenicated = false
//       //TODO: Remove in prodoction or user link is created.
//       if(this.testing){
//         this.defaultStore()
//       }
//       else if (localStorage.getItem('token')) {
//         this.user.token = localStorage.getItem('token')
//         this.user.name = localStorage.getItem('name')
//         this.user.email = localStorage.getItem('email')
//         this.user.role = localStorage.getItem('role')

//         this.user.storeCode = localStorage.getItem('storeCode')
//         this.user.clientCode = localStorage.getItem('clientCode')

//         this.user.groupCode = localStorage.getItem('groupCode')
//       }

//     },
//     setUser(userInfo) {
//       this.user.token=userInfo.token
//       this.user.isAuthenicated=true
//       this.user.role=userInfo.role
//       this.user.name=userInfo.name
//       this.user.email=userInfo.email
//       this.user.storeCode=userInfo.storeCode
//       this.user.clientCode=userInfo.clientCode
//       this.user.groupCode=userInfo.groupCode

//       localStorage.setItem('token', userInfo.token)
//       localStorage.setItem('name', userInfo.name)
//       localStorage.setItem('email', userInfo.email)
//       localStorage.setItem('role', userInfo.role)
//       localStorage.setItem('storeCode', userInfo.storeCode)
//       localStorage.setItem('clientCode', userInfo.clientCode)
//       localStorage.setItem('groupCode', userInfo.groupCode)
//     },
//     removeUser() {
//       this.user.token=null
//       this.user.isAuthenicated=false
//       this.user.role=null
//       this.user.name=null
//       this.user.email=null
//       localStorage.setItem('token', '')
//       localStorage.setItem('name', '')
//       localStorage.setItem('email', '')
//       localStorage.setItem('role', '')
//       localStorage.setItem('storeCode', '')
//       localStorage.setItem('clientCode', '')
//       localStorage.setItem('groupCode', '')
//     },


//     // async fetchUsers() {
//     //   const { data, error } = await useFetch('/api/users')
//     //   if (error) {
//     //     console.log(error)
//     //     return
//     //   }
//     //   this.users = data.value
//     // },
//   },
// })

// if (import.meta.hot) {
//   import.meta.hot.accept(acceptHMRUpdate(useAuth, import.meta.hot))
// }

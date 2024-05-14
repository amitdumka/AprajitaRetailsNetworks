// import { defineStore ,acceptHMRUpdate } from 'pinia'


// export const useBasicData = defineStore('basicData', {
//   // id: 'basicData',
//   state: () => ({
//     clients: [],
//     groups:[],
//     stores: [],
//     employees: [],
//     transcations: [],
//     posMachines: [],
//   }),
//   actions: {

//     async updateBasicData(basicData){

//       if(basicData!=null){

//         this.clients =  basicData.clients?.basicData.clients
//         this.groups = basicData.groups?.basicData.groups
//         this.stores = basicData.stores?.basicData.stores
//         this.employees = basicData.employees?.basicData.employees
//         this.transcations = basicData.transcations?.basicData.transcations
//         this.posMachines = basicData.posMachines?.basicData.posMachines
//         console.log('Basic data is store')
//       }
//     },
//      async fetchBasicData() {
//        const { data, error } = await useFetch('/api/basicData')
//        if (error) {
//          console.log(error)
//          return
//        }
//        this.basicData ( data.value)
//      },
//   },
// })



export default async function (api: string) {
  const baseURL = process.env.AR_Server ? process.env.AR_Server : 'http://127.0.0.1:8000/'
  const { data, error } = await useAsyncData('api', () => $fetch(`${baseURL}${api}`))
  if (error) {
    console.log(error)
    return { data, error, success: false, isError: true }

  }
  return { data, error, success: true, isError: false }

}


async function basicList(adv: boolean) {
  const baseURL = process.env.AR_Server ? process.env.AR_Server : 'http://127.0.0.1:8000/'

  const { data: baseListData, pending } = await useAsyncData('cart-discount', async () => {
    const [storeList, groupList, clientList, employeeList] = await Promise.all([
      $fetch(`${baseURL}/storelist`),
      $fetch(`${baseURL}/groupList`),
      $fetch(`${baseURL}/clientList`),
      $fetch(`${baseURL}/employeeList`)

      // adv?$fetch(`${baseURL}/transcationtypes`):null,
      // adv?$fetch(`${baseURL}/posList`):null,
      // $fetch(`${baseURL}/advClientList`),
      // $fetch(`${baseURL}/advEmployeeList`),


    ])

    return { storeList, groupList, clientList, employeeList }
  })
}

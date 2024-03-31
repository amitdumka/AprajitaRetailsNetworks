
export type Status = 'active' | 'inactive'|'closed'

export interface Client{
  id: number
  name: string
  email: string
  city:string
  address:string
  pan:string
  gstin:string
  phone:string
  status: Status
  location: string
}

export interface StoreGroup{
  id:string
  name:string
  client:Client
  status: Status
  location: string
  city:string
  address:string
  email:string
  phone:string
}

export interface Store{
  id:string
  name:string
  group:StoreGroup
  status: Status
  location: string
  city:string
  address:string
  email:string
  phone:string
  client:Client
}

export type Gender='male'|'female'|'transgender'
export type EmpType = 'owner' | 'storemanger'|'salesman'|'housekeeping'|'accountant'|'admin'|'others'

export interface Employee{
  id:string
  firstName:string
  lastName:string
  empType:EmpType
  dateofBirth:Date
  fatherName:string
  spouseName:string
  gender:Gender
  store:Store
  status: Status
  location: string
  city:string
  address:string
  email:string
  phone:string
  client:Client
  group:StoreGroup
}

export type AttType = 'present' | 'absent'|'halfday'|'paidleave'|'casualleave'|'sickleave'|'other'|'paidholiday'
export interface Attendance{
  id:string
  emp:Employee
  date:Date
  attType:AttType
  entryTime:string
  remarks:string
  client:Client
  group:StoreGroup
  store:Store


}


export type SalaryType= 'netSalary'| 'salaryadvance'| 'incentive'| 'bonus'| 'special'| 'other'

export interface SalaryPayment{
  id:string
  emp:Employee
  date:Date
  salaryType:SalaryType
  amount:number
  remarks:string
  paymentDetails:string
  paymentMode:string
  client:Client
  group:StoreGroup
  store:Store
}

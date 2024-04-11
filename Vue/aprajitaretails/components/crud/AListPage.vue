<!-- Record Listing Page Components -->
<script setup lang="ts">
//import { Client, StoreGroup, Store } from "~/types"
import { GridComponent as EjsGrid, ColumnsDirective as EColumns, ColumnDirective as EColumn } from '@syncfusion/ej2-vue-grids'
const page = ref(1)
// rest of your code
//const ui = { container: 'lg:sticky top-2' }
//const cardUI = { rounded: 'rounded-lg', shadow: 'shadow', header: { padding: 'px-8 sm:px-6 , sm:pb-0, sm:pt-0' }, body: { padding: 'p-1 sm:p-2' } }
</script>

<template>
  <UDashboardSection :orientation="orientation">
    <UDashboardCard :title="title" :description="subTitle" :links="[{ label: 'Add', color: 'green', trailingIcon: 'i-heroicons-plus-20-solid' }]">
      <ejs-grid :dataSource="entities" :allowPaging='true' :allowSorting='true' :allowResizing='true' height="height" width="width" />
      <UPagination v-model="page" :page-count="5" :total="entities.length" />
    </UDashboardCard>
  </UDashboardSection>
</template>

<script lang="ts">
const data = [
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  },
  {
    OrderID: 10249, CustomerID: 'TOMSP', EmployeeID: 6, ShipCountry: 'Germany', Freight: 11.61
  },
  {
    OrderID: 10250, CustomerID: 'HANAR', EmployeeID: 4, ShipCountry: 'Brazil', Freight: 65.83
  }
]
export default {
  props: {
    height: {
      type: Number,
      required: false,
      default: () => 400
    },
    width: {
      type: Number,
      required: false,
      default: () => 1140
    },
    orientation: {
      type: String,
      required: false,
      default: () => 'vertical'
    },
    title: {
      type: String,
      required: true,
      default: () => ''
      //Employees
    },
    subTitle: {
      type: String,
      required: false,
      default: () => 'Sub titile is missing!'
      //Employees
    },
    appLink: {
      type: String,
      required: true,
      default: () => ''
      //Main Route or it cloud be passed for other routes
      //like /hrms/employees
    },
    apiURL: {
      type: String,
      required: true,
      //API Base URl to fetch data from server
      //like https://www.aprajitaretails.in/api/v1/employees/
    },
    entityName: {
      type: String,
      required: true,
      default: () => ''
      //for exmple Employee ie. className
    },
    allowEdit: {
      type: Boolean,
      required: false,
      default: () => false
    },
    allowDelete: {
      type: Boolean,
      required: false,
      default: () => false
    },
    // clients: {
    //   type: Array as PropType<Client[]>,
    //   default: () => []
    // },
    // groups: {
    //   type: Array as PropType<StoreGroup[]>,
    //   default: () => []
    // },
    // stores: {
    //   type: Array as PropType<Store[]>,
    //   default: () => []
    // },
    entities: {
      type: Array as PropType<any[]>,
      default: () => data
    },
  }
}
</script>
<style>
/* @import "./node_modules/@syncfusion/ej2-base/styles/tailwind-dark.css";
@import "../aprajitaretails/node_modules/@syncfusion/ej2-buttons/styles/tailwind-dark.css";
@import "../aprajitaretails/node_modules/@syncfusion/ej2-calendars/styles/tailwind-dark.css";
@import "../aprajitaretails/node_modules/@syncfusion/ej2-dropdowns/styles/tailwind-dark.css";
@import "../aprajitaretails/node_modules/@syncfusion/ej2-inputs/styles/tailwind-dark.css";
@import "../aprajitaretails/node_modules/@syncfusion/ej2-navigations/styles/tailwind-dark.css";
@import "../aprajitaretails/node_modules/@syncfusion/ej2-popups/styles/tailwind-dark.css";
@import "../aprajitaretails/node_modules/@syncfusion/ej2-splitbuttons/styles/tailwind-dark.css"; */
 @import "../aprajitaretails/node_modules/@syncfusion/ej2-vue-grids/styles/tailwind-dark.css"; 
/* https://www.smashingmagazine.com/2020/01/data-components-vue-js/ */
</style>

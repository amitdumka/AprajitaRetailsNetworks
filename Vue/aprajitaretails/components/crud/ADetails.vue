<script setup>
const columns = [{
  key: 'Field',
  label: ' '
}, {
  key: 'Value',
  label: ' '
},]
const people = [
  { Field: 'id', Value: 1 },
  { Field: 'name', Value: 'Lindsay Walton' },
  { Field: 'title:', Value: 'Front-end Developer' },
  { Field: 'email:', Value: 'lindsay.walton@example.com' },
  { Field: 'role:', Value: 'Member' }
]
</script>
<template>
  <UDashboardSection :orientation="orientation">
    <UCard>
      <template #header>
        <h5>Employee Details</h5>
      </template>
      <UTable :columns="columns" :rows="people" />
      <template #footer>
        <UButton>Back</UButton>
      </template>
    </UCard>
  </UDashboardSection>
</template>

<script>
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

  }
}
</script>

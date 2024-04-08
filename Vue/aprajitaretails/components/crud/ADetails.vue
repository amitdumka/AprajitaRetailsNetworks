<script setup>
const columns = [{
  key: 'Field',
  label: ''
}, {
  key: 'Value',
  label: ''
},]
const xc = [
  { Field: 'id', Value: 1 },
  { Field: 'name', Value: 'Lindsay Walton' },
  { Field: 'title:', Value: 'Front-end Developer' },
  { Field: 'email:', Value: 'lindsay.walton@example.com' },
  { Field: 'role:', Value: 'Member' }
]

const cardUI = { rounded: 'rounded-lg', shadow: 'shadow', header: { padding: 'px-8 sm:px-6 , sm:pb-0, sm:pt-0' }, body: { padding: '' } }

</script>
<template>
  <UDashboardSection :orientation="orientation">
    <UCard :ui="cardUI">
      <template #header>
        <h3 class="text-2xl text-gray-900 dark:text-white">{{ title }}</h3>
        <h5 class="ml-2 text-gray-900 dark:text-primary"> {{ subTitle }} </h5>
      </template>
      <table class="table">
        <tbody>
          <tr v-for="(value, key) in entity" :key="key" class="row">
            <td class="key-column">{{ key }} </td>
            <td class="value-column">{{ value }}</td>
          </tr>
        </tbody>
      </table>
      <template #footer>
        <UButton label="Back" variant="ghost" @click="goBack" />
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
    entity: {
      type: Object,
      required: false,
      default: () => { }
    },


  }
  , methods: {
    goBack() {
      this.$router.go(-1)
    },
    convertObjectToArray(obj) {
      return Object.keys(obj).map(key => ({ [key]: obj[key] }))
    },
    createNewRow() {
      const dd = this.convertObjectToArray(this.entity)
      console.log(dd)
      return dd
    }
  },
}
</script>


<style scoped>
.table {
  width: 100%;
  /* Make the table span the full width */
  border-collapse: collapse;
  /* Remove space between table cells */
}

.key-column {
  width: 12%;
  /* Adjust as needed */
  padding: 10px;
  /* Adjust as needed */
  color: rgb(180, 165, 165);
  /* Text color is grey */

}

.value-column {
  width: 50%;
  /* Adjust as needed */
  padding: 10px;
  /* Adjust as needed */
  color: lightslategrey;
  /* Text color is grey */
}

.row {
  border-bottom: 0.1px solid rgba(211, 211, 211, 0.127);
  /* Add a thin horizontal grid line */
  margin-bottom: 10px;
  /* Add a margin between rows */
}
</style>

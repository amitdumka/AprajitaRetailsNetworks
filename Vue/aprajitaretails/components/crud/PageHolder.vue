<!-- This Main Page will be used as Dashboard. -->
<script setup lang="ts">

// const items = [[{
//   label: 'Reports',
//   icon: 'i-heroicons-paper-airplane',
//   to: '/core/clients/reports'
// }, {
//   label: 'New Client',
//   icon: 'i-heroicons-user-plus',
//   to: '/core/clients/new'
// }]]

</script>

<template>
  <UDashboardPage>
    <UDashboardPanel grow collapsible>
      <UDashboardNavbar :title="title">
        <template #right>
          <UDropdown v-if="enableMenu" :items="menuItems">
            <UButton icon="i-heroicons-bars-3" size="md" class="ml-1.5 rounded-full" />
          </UDropdown>
        </template>
      </UDashboardNavbar>
      <slot />
    </UDashboardPanel>
  </UDashboardPage>
</template>

<script lang="ts">
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
      required: false,
      default: () => ''
    },
    apiURL: {
      type: String,
      required: false,
      default: () => ''
      //API Base URl to fetch data from server
      //like https://www.aprajitaretails.in/api/v1/employees/
    },
    returnRoute: {
      type: String,
      required: false,
      default: () => ''
    },
    menuItems: {
      type: Array,
      required: false,
      default: () => []
    },
    enableMenu: {
      type: Boolean,
      required: false,
      default: () => true
    }
  }
}

</script>


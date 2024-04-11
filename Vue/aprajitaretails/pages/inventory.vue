<script setup lang="ts">
const links = [[{
    label: 'Clients',
    icon: 'i-heroicons-user-circle',
    to: '/core/clients',
    exact: true
  }, {
    label: 'Stores',
    icon: 'i-heroicons-user-group',
    to: '/core/stores'
  }, {
    label: 'Store Groups',
    icon: 'i-heroicons-bell',
    to: '/core/storegroups'
  }], [{
    label: 'Store Settings',
    icon: 'i-heroicons-book-open',
    to: '/hrms/payrollsettings',
  }, {
    label: 'Customers',
    icon: 'i-heroicons-credit-card',
    to: '/hrms/ledgers',
  }]]
</script>

<template>
  <UDashboardPage>
    <UDashboardPanel grow>
      <UDashboardNavbar title="Inventory" />

      <UDashboardToolbar class="py-0 px-1.5 overflow-x-auto">
        <UHorizontalNavigation :links="links" />
      </UDashboardToolbar>

      <NuxtPage />
    </UDashboardPanel>
  </UDashboardPage>
</template>

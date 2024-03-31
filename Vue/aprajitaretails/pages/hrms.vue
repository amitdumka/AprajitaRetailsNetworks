<script setup lang="ts">
const links = [[{
    label: 'Employees',
    icon: 'i-heroicons-user-circle',
    to: '/hrms',
    exact: true
  }, {
    label: 'Attendnaces',
    icon: 'i-heroicons-user-group',
    to: '/hrms/attendances'
  }, {
    label: 'Salary Payments',
    icon: 'i-heroicons-bell',
    to: '/hrms/salarypayments'
  }], [{
    label: 'Payroll Settings',
    icon: 'i-heroicons-book-open',
    to: '/hrms/payrollsettings',
  }, {
    label: 'Ledgers',
    icon: 'i-heroicons-credit-card',
    to: '/hrms/ledgers',
  }]]
</script>

<template>
  <UDashboardPage>
    <UDashboardPanel grow>
      <UDashboardNavbar title="HRMS" />

      <UDashboardToolbar class="py-0 px-1.5 overflow-x-auto">
        <UHorizontalNavigation :links="links" />
      </UDashboardToolbar>

      <NuxtPage />
    </UDashboardPanel>
  </UDashboardPage>
</template>

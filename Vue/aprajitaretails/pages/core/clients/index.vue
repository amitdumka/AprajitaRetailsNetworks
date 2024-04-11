<!-- This Main Page will be used as Dashboard. -->
<script setup lang="ts">
const items = [[{
  label: 'Reports',
  icon: 'i-heroicons-paper-airplane',
  to: '/core/clients/reports'
}, {
  label: 'New Client',
  icon: 'i-heroicons-user-plus',
  to: '/core/clients/EditClients'
}]]

const data = {
  OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
}
</script>

<template>
  <CrudPageHolder title="Clients" :menu-items="items">
    <UDashboardPanelContent>
      <CrudADetails title="Employees" entityName="Employee" subTitle="Details of Employee" :entity="data" />
    </UDashboardPanelContent>
  </CrudPageHolder>
</template>

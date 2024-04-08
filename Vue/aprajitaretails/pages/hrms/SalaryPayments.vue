<script setup lang="ts">
  import ADetails from '~/components/crud/ADetails.vue'
  const data =   {
    OrderID: 10248, CustomerID: 'VINET', EmployeeID: 5, ShipCountry: 'France', Freight: 32.38
  }
</script>

<template>
  <UDashboardPanel :resizable="{ min: 200 }" grow collapsible>
    <UDashboardPanelContent>
      <ADetails title="Employees" entityName="Employee" subTitle="Details of Employee" :entity="data" />
    </UDashboardPanelContent>
  </UDashboardPanel>
</template>


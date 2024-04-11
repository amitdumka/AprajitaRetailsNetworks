<script setup>
  import AListPage from '~/components/crud/AListPage.vue'
</script>

<template>
  <UDashboardPanel :resizable="{ min: 200 }" grow collapsible>
    <UDashboardPanelContent class="pb-24" grow>
      <AListPage title="Employees" sub-title="List of Employees" :api-u-r-l="api / employees" :entity-name="Employee" />
    </UDashboardPanelContent>
    <AFooter />
  </UDashboardPanel>
</template>
<!--
// import "@syncfusion/ej2-base/styles/material.css";
// import "@syncfusion/ej2-buttons/styles/material.css";
// import "@syncfusion/ej2-calendars/styles/material.css";
// import "@syncfusion/ej2-dropdowns/styles/material.css";
// import "@syncfusion/ej2-inputs/styles/material.css";
// import "@syncfusion/ej2-navigations/styles/material.css";
// import "@syncfusion/ej2-popups/styles/material.css";
// import "@syncfusion/ej2-splitbuttons/styles/material.css";
// import "@syncfusion/ej2-vue-grids/styles/material.css";
//https://ej2.syncfusion.com/vue/documentation/grid/getting-started-vue?_gl=1*1v5jtm9*_ga*NTgxNjE0NDI0LjE3MTE2MTc4Nzc.*_ga_41J4HFMX1J*MTcxMTk2Nzg3NC43LjEuMTcxMTk3MDA4OC4wLjAuMA.. -->



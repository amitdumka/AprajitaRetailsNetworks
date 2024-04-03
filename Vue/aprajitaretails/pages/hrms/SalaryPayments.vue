<script setup lang="ts">
  import ADetails from '~/components/crud/ADetails.vue'
</script>

<template>
  <UDashboardPanel :resizable="{ min: 200 }" grow collapsible>
    <UDashboardPanelContent>
      <!-- <ADetailPage :title="title" :description="subTitle" /> class="p-0 pb-24 divide-y divide-gray-200 dark:divide-gray-800"-->
     <ADetails />
    </UDashboardPanelContent>
  </UDashboardPanel>
</template>

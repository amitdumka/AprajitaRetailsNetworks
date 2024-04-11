<!-- This Main Page will be used as Dashboard. -->
<script setup lang="ts">


const items = [[{
  label: 'Store Group',
  icon: 'i-heroicons-paper-airplane',
  to: '/inbox'
}, {
  label: 'New Group',
  icon: 'i-heroicons-user-plus',
  to: '/users'
}]]

 </script>

<template>
  <UDashboardPage>
    <UDashboardPanel grow collapsible>
      <UDashboardNavbar title="Store Groups">
        <template #right>
          <UDropdown :items="items">
            <UButton icon="i-heroicons-bars-3" size="md" class="ml-1.5 rounded-full" />
          </UDropdown>
        </template>
      </UDashboardNavbar>
      <UDashboardPanelContent>
        <div class="grid lg:grid-cols-2 lg:items-start gap-8 mt-8">
          Your Content Goes Here
        </div>
      </UDashboardPanelContent>
    </UDashboardPanel>
  </UDashboardPage>
</template>

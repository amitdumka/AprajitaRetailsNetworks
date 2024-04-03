<script setup lang="ts">
const route = useRoute()
const appConfig = useAppConfig()
const { isHelpSlideoverOpen } = useDashboard()

const links = [{
  id: 'home',
  label: 'Home',
  icon: 'i-heroicons-home',
  to: '/',
  tooltip: {
    text: 'Home',
    shortcuts: ['G', 'H']
  }
}, {
  id: 'inbox',
  label: 'Inbox',
  icon: 'i-heroicons-inbox',
  to: '/inbox',
  badge: '4',
  tooltip: {
    text: 'Inbox',
    shortcuts: ['G', 'I']
  }
}, {
  id: 'users',
  label: 'Users',
  icon: 'i-heroicons-user-group',
  to: '/users',
  tooltip: {
    text: 'Users',
    shortcuts: ['G', 'U']
  }
}, {
  id: 'settings',
  label: 'Settings',
  to: '/settings',
  icon: 'i-heroicons-cog-8-tooth',
  defaultOpen: route.path.startsWith('/settings'),
  children: [{
    label: 'General',
    to: '/settings',
    exact: true
  }, {
    label: 'Members',
    to: '/settings/members'
  }, {
    label: 'Notifications',
    to: '/settings/notifications'
  }],
  tooltip: {
    text: 'Settings',
    shortcuts: ['G', 'S']
  }
}]

const footerLinks = [{
  label: 'Invite people',
  icon: 'i-heroicons-plus',
  to: '/settings/members'
}, {
  label: 'Help & Support',
  icon: 'i-heroicons-question-mark-circle',
  click: () => isHelpSlideoverOpen.value = true
}]

const groups = [{
  key: 'links',
  label: 'Go to',
  commands: links.map(link => ({ ...link, shortcuts: link.tooltip?.shortcuts }))
}, {
  key: 'code',
  label: 'Code',
  commands: [{
    id: 'source',
    label: 'View page source',
    icon: 'i-simple-icons-github',
    click: () => {
      window.open(`https://github.com/nuxt-ui-pro/dashboard/blob/main/pages${route.path === '/' ? '/index' : route.path}.vue`, '_blank')
    }
  }]
}]

//Menu Sections
const coreMenu = [{
  id: 'core',
  label: 'Store',
  icon: 'i-heroicons-user-group',
  to: '/core',
  defaultOpen: route.path.startsWith('/core'),
  children: [{
    label: 'Clients',
    to: '/core',
    exact: true
  }, {
    label: 'Store Groups',
    to: '/core/storegroups',
    exact: true
  }, {
    label: 'Stores',
    to: '/core/stores',
    exact: true
  }, {
    label: 'Ledgers',
    to: '/hrms/ledgers',
    exact: true
  }],
  tooltip: {
    text: 'Core Menu',
    shortcuts: ['S', 'C']
  }

}]
const accoutingMenu = [{
  id: 'accounting',
  label: 'Accounting',
  icon: 'i-heroicons-user-group',
  to: '/accounting',
  defaultOpen: route.path.startsWith('/accounting'),
  children: [{
    label: 'Vouchers',
    to: '/core',
    exact: true
  }, {
    label: 'Cash Vouchers',
    to: '/accounting/cashvouchers',
    exact: true
  }, {
    label: 'Notes',
    to: '/accouting/Notes',
    exact: true
  }, {
    label: 'Journals',
    to: '/accountinhg/journals',
    exact: true
  }],
  tooltip: {
    text: 'Accounting Menu',
    shortcuts: ['S', 'A']
  }

}, {
  id: 'banking',
  label: 'Banking',
  icon: 'i-heroicons-user-group',
  to: '/banking',
  defaultOpen: route.path.startsWith('/banking'),
  children: [{
    label: 'Bank Accounts',
    to: '/banking',
    exact: true
  }, {
    label: 'Vendor Accounts',
    to: '/banking/vendoraccounts',
    exact: true
  }, {
    label: 'Banks',
    to: '/banking/banks',
    exact: true
  }, {
    label: 'Cheques',
    to: '/banking/cheques',
    exact: true
  }],
  tooltip: {
    text: 'Banking Menu',
    shortcuts: ['S', 'B']
  }
}
]
const hrmsMenu = [{
  id: 'hrms',
  label: 'HRMS',
  icon: 'i-heroicons-user-group',
  to: '/hrms',
  defaultOpen: route.path.startsWith('/hrms'),
  children: [{
    label: 'Employees',
    to: '/hrms',
    exact: true
  }, {
    label: 'Attendances',
    to: '/hrms/attendances',
    exact: true
  }, {
    label: 'Salary Payments',
    to: '/hrms/salarypayments',
    exact: true
  }, {
    label: 'Ledgers',
    to: '/hrms/ledgers',
    exact: true
  }],
  tooltip: {
    text: 'HRMS',
    shortcuts: ['H', 'E']
  }

}]

const defaultColors = ref(['green', 'teal', 'cyan', 'sky', 'blue', 'indigo', 'violet'].map(color => ({ label: color, chip: color, click: () => appConfig.ui.primary = color })))
const colors = computed(() => defaultColors.value.map(color => ({ ...color, active: appConfig.ui.primary === color.label })))
</script>

<template>
  <UDashboardLayout width="w-full">
    <UDashboardPanel :width="250" :resizable="{ min: 200, max: 300 }" collapsible>
      <UDashboardNavbar class="!border-transparent" :ui="{ left: 'flex-1' }">
        <template #left>
          <TeamsDropdown />
        </template>
      </UDashboardNavbar>

      <UDashboardSidebar width="w-full">
        <template #header>
          <UDashboardSearchButton />
        </template>

        <!-- TODO: make this all sub menu collapsed or closed rather than open -->
        <UDashboardSidebarLinks :links="links" />

        <UDivider />
        <UDashboardSidebarLinks :links="coreMenu" />
        <UDashboardSidebarLinks :links="accoutingMenu" />
        <UDivider />
        <UDashboardSidebarLinks :links="hrmsMenu" />

        <!-- <UDashboardSidebarLinks :links="inventoryMenu" /> -->
        <!-- <UDashboardSidebarLinks :links="posMenu" /> -->
        <!-- <UDashboardSidebarLinks :links="ledgerMenu" /> -->
        <!-- <UDashboardSidebarLinks :links="booksMenu" /> -->
        <UDivider />
        <!-- TODO: Enable these components based on our requriments and context -->
        <!-- <UDashboardSidebarLinks :links="[{ label: 'Colors', draggable: true, children: colors }]" @update:links="colors => defaultColors = colors" /> -->

        <div class="flex-1" />

        <!-- <UDashboardSidebarLinks :links="footerLinks" /> -->

        <UDivider class="sticky bottom-0" />
        <!-- ~/components/UserDropdown.vue -->
        <template #footer>
          <UserDropdown />
        </template>
      </UDashboardSidebar>
    </UDashboardPanel>

    <slot />

    <!--  TODO: implement this for a better experience our context /> -->
    <!-- ~/components/HelpSlideover.vue -->
    <!-- <HelpSlideover /> -->
    <!-- ~/components/NotificationsSlideover.vue -->
    <!-- <NotificationsSlideover /> -->

    <ClientOnly>
      <LazyUDashboardSearch :groups="groups" />
    </ClientOnly>
  </UDashboardLayout>
</template>

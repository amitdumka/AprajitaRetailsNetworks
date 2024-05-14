<!-- This Main Page will be used as Dashboard. -->
<script setup lang="ts">
import { sub } from 'date-fns'
import type { Period, Range } from '~/types'

const { isNotificationsSlideoverOpen } = useDashboard()
const { signIn, signOut, session, status, cookies } = useAuth()

async function check() {
  try {
    await signIn('credentials', {
      redirect: false,
      username: 'admin',
      password: 'admin'
    })
    // eslint-disable-next-line no-console
    console.log('SignIn', session.value?.user)
  }
  catch (error) {
    // eslint-disable-next-line no-console
    console.log(`Error SignIn: ${error}`)
  }
}
const items = [[{
  label: 'New mail',
  icon: 'i-heroicons-paper-airplane',
  to: '/inbox'
}, {
  label: 'New user',
  icon: 'i-heroicons-user-plus',
  to: '/users'
}]]

const range = ref<Range>({ start: sub(new Date(), { days: 14 }), end: new Date() })
const period = ref<Period>('daily')
</script>

<template>
  <UDashboardPage>
    <UDashboardPanel grow collapsible>
      <UDashboardNavbar title="Home">
        <template #right>
          <UTooltip text="Notifications" :shortcuts="['N']">
            <UButton color="gray" variant="ghost" square @click="isNotificationsSlideoverOpen = true">
              <UChip color="red" inset>
                <UIcon name="i-heroicons-bell" class="w-5 h-5" />
              </UChip>
            </UButton>
          </UTooltip>
          <UButton color="gray" variant="ghost" square @click="signIn(`credentials`)">
            <UIcon name="i-heroicons-user" class="w-5 h-5" />
          </UButton>

          <UDropdown :items="items">
            <UButton icon="i-heroicons-plus" size="md" class="ml-1.5 rounded-full" />
          </UDropdown>
        </template>
      </UDashboardNavbar>

      <UDashboardToolbar>
        <template #left>
          <!-- ~/components/home/HomeDateRangePicker.vue -->
          <HomeDateRangePicker v-model="range" class="-ml-2.5" />

          <!-- ~/components/home/HomePeriodSelect.vue -->
          <HomePeriodSelect v-model="period" :range="range" />
        </template>
      </UDashboardToolbar>

      <UDashboardPanelContent>
        <!-- ~/components/home/HomeChart.vue -->
        <!-- <HomeChart :period="period" :range="range" /> -->

        <div class="grid lg:grid-cols-2 lg:items-start gap-8 mt-8">
          <!-- ~/components/home/HomeSales.vue -->
          <HomeSales />
          <!-- ~/components/home/HomeCountries.vue -->
          <HomeCountries />
        </div>
      </UDashboardPanelContent>
    </UDashboardPanel>
  </UDashboardPage>
</template>

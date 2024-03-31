import { createSharedComposable } from '@vueuse/core'

// Routes and Router Configuration 
const _useDashboard = () => {
  const route = useRoute()
  const router = useRouter()
  const isHelpSlideoverOpen = ref(false)
  const isNotificationsSlideoverOpen = ref(false)

  // Defining Shortcut Key for Route
  defineShortcuts({
    'g-h': () => router.push('/'),
    'g-i': () => router.push('/inbox'),
    'g-u': () => router.push('/users'),
    'g-s': () => router.push('/settings'),
    'h-e': () => router.push('/hrms'),
    '?': () => isHelpSlideoverOpen.value = true,
    n: () => isNotificationsSlideoverOpen.value = true
  })

  watch(() => route.fullPath, () => {
    isHelpSlideoverOpen.value = false
    isNotificationsSlideoverOpen.value = false
  })

  return {
    isHelpSlideoverOpen,
    isNotificationsSlideoverOpen
  }
}

export const useDashboard = createSharedComposable(_useDashboard)

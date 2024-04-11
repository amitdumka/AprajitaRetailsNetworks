<template>
  <CrudPageHolder :title="title" :enable-menu="false">
    <UDashboardPanelContent class="pb-24" grow>
      <UCard :ui="cardUI">
        <Vueform v-bind="form" />
      </UCard>
    </UDashboardPanelContent>
  </CrudPageHolder>
</template>
<script>
const cardUI = { rounded: 'rounded-lg', shadow: 'shadow', header: { padding: 'px-8 sm:px-6 , sm:pb-0, sm:pt-0' }, body: { padding: '' } }

export default {
  props: {
    form: {
      type: Object,
      default: undefined,
      required: true
    },
    title: {
      type: String,
      default: undefined,
      required: true
    }
  },
  

}
</script>

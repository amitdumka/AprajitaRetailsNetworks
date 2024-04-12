<template>
  <CrudPageHolder :title="title" :enable-menu="false">
    <UDashboardPanelContent class="pb-24" grow>
      <UCard :ui="cardUI">
        <Vueform v-bind="form" :float-placeholders="true" methord="post" @response="handleResponse" />
      </UCard>
    </UDashboardPanelContent>
  </CrudPageHolder>
</template>
<script>
const cardUI = { rounded: 'rounded-lg', shadow: 'shadow', header: { padding: 'px-8 sm:px-6 , sm:pb-0, sm:pt-0' }, body: { padding: '' } }
//const columns={ container: 12, label: 4, wrapper: 8 }
// :columns="{
//   xs: { container: 12, label: 12, wrapper: 12 },
//   sm: { container: 12, label: 4, wrapper: 12 },
//   md: 12,
//   lg: { container: 12, label: 2, wrapper: 12 }
// }" ...
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
    },
    handleResponse: {
      type: Function,
      default: undefined,
      required: true
    },
    prepare:{
      type: Function,
      default: undefined,
      required: true
    }
  },



}
</script>

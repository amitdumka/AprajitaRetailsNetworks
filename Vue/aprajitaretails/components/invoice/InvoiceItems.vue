<template>
  <div>
    Invoice Item List use UTable Here to dislay the invoice items addded.
    Plus show add or remove button so it can added or cancle on fly.
  </div>
</template>
<script>
export default{
  name: 'InvoiceItems',
  props: {
    items: {
      type: Array,
      default: undefined
    }
  }

}
</script>


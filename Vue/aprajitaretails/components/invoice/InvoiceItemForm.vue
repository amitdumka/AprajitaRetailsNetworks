<template>
  <div>
    Enttry Form . Here In One Row There will entry form for barcode, rate, quantity, discount, tax, amount
    Singe row or liner form inline form 
  </div>
</template>

<script>
export default {
  name: 'InvoiceItemForm',
  props: {
    barcode: {
      type: String,
      default: undefined
    },
    rate: {
      type: Number,
      default: undefined
    },
    quantity: {
      type: Number,
      default: undefined
    },
    discount: {
      type: Number,
      default: undefined
    },
    tax: {
      type: Number,
      default: undefined
    },
    amount: {
      type: Number,
      default: undefined
    }

  }
}
</script>

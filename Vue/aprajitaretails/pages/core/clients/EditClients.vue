<template>
  <CrudEditForm title="Client" :form="form" />
</template>

<script>

export default {
  setup() {
    const form = ref({
      size: 'sm',
      displayErrors: true,
      schema: {
        page_title: {
          type: 'static',
          content: 'Create Client',
          tag: 'h3',
        },
        divider: {
          type: 'static',
          tag: 'hr',
        },
        clientName: {
          type: 'text',
          rules: [
            'required',
            'max:255',
          ],
          placeholder: 'Client Name',
          fieldName: 'ClientName',
          description: 'Client Name will appear on invoices.',
        },
        clienAddress: {
          type: 'text',
          rules: [
            'required',
            'max:255',
          ],
          placeholder: 'Client Address',
          fieldName: 'ClientAddress',
          description: 'Client Address will appear on invoices.',
        },
        clientCity: {
          type: 'text',
          rules: [
            'required',
            'max:255',
          ],
          placeholder: 'Client City',
          fieldName: 'ClientName',
          description: 'Client Name will appear on invoices.',
        },
        email: {
          type: 'text',
          inputType: 'email',
          rules: [
            'required',
            'max:255',
            'email',
          ],
          placeholder: 'Email',
          fieldName: 'Email',
          description: 'You will receive a confirmation letter to this email.',
        },

        cleintPhone: {
          type: 'text',
          rules: [
            'required',
            'min:10',
            'max:14',
          ],
          placeholder: 'Phone Number',
          fieldName: 'ClientPhone',
          description: 'CLient Phone Number will appear on invoices.',
        },

        container: {
          type: 'group',
          schema: {
            register: {
              type: 'button',
              size:'sm',
              buttonLabel:'Create client',
              full:false,
              submits:true,
              columns: {
                container: 4,
                label: 4,
                wrapper: 4,
              },

            },
            back: {
              type: 'text',
              type: 'button',
              buttonLabel:'Back',
              full:false,
              size:'sm',
              submits:false,
              onclick: 'goBack',
              columns: {
                container: 3,
                label: 3,
                wrapper: 3,
              },
            },
          },
        },
      }

    })
    return {
      form,
    }
  },
  methods:{
    goBack() {
      this.$router.go(-1)
    },
  }
}
</script>

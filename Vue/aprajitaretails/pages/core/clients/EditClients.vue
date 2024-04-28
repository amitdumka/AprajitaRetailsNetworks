<template>
  <CrudEditForm title="Client" :form="form" :handle-response="handleResponse" :prepare="prepare" />
</template>

<script>
const handleResponse = (response, form$) => {
  console.log(response) // axios response
  console.log(response.status) // HTTP status code
  console.log(response.data) // response data

  console.log(form$) // <Vueform> instance
}
const prepare = async (form$) => {
  // eslint-disable-next-line no-useless-catch
  try {
    this.$router.go(-1)
    console.log(form$)
  } catch (error) {
    throw error // cancels form submit
  }
}
const onSubmit = (event) => {
  // Do something with data
}
const countryList = ['India', 'Sri Lank', 'USA', 'Japan', 'China', 'Bhutan', 'Nepal', 'Australia', 'UK']
export default {
  setup() {
    const form = ref({
      size: 'sm',
      displayErrors: false,
      showSubmitButton: true,
      showCancelButton: true,
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
          fieldName: 'Name',
          description: 'Client Name will appear on invoices.',
        },


        clienAddress: {
          type: 'textarea',
          rules: [
            'required',
            'max:255',
          ],
          //label: 'Client Address',
          placeholder: 'Client Address',
          fieldName: 'Address',
          description: 'Client Address will appear on invoices.',
        },

        container_State: {
          type: 'group',
          schema: {
            clientZipCode: {
              type: 'text',
              rules: [
                'required',
                'max:8',
              ],
              full: false,
              columns: {
                container: 3,
                label: 1,
                wrapper: 4,
              },
              placeholder: 'Zip Code',
              fieldName: 'ZipCode',
              description: 'Client Zip Code will appear on invoices.',
            },
            clientCity: {
              type: 'text',
              rules: [
                'required',
                'max:255',
              ],
              full: false,
              columns: {
                container: 3,
                label: 1,
                wrapper: 6,
              },
              placeholder: 'Client City',
              fieldName: 'City',
              description: 'Client Name will appear on invoices.',
            }, state: {
              type: 'text',
              columns: {
                container: 3,
                label: 1,
                wrapper: 6,
              },
              full: false,
              placeholder: 'State',
              fieldName: 'State',
              description: 'CLient State will appear on invoices.',

            },
            country: {
              type: 'select',
              columns: {
                container: 3,
                label: 1,
                wrapper: 6,
              },
              full: false,
              search: true,
              inputType: 'search',
              autocomplete: 'enabled',
              placeholder: 'Country',
              fieldName: 'Country',
              description: 'CLient Country will appear on invoices.',
              items: countryList,

            },
          }
        },
        start_endDate: {
          type: 'group',
          schema: {
            startDate: {
              type: 'date',
              rules: [
                'required',
              ],
              columns: {
                container: 6,
                label: 3,
                wrapper: 8,
              },
              full: false,
              placeholder: 'Start Date',
              fieldName: 'StartDate',
              description: 'Client Start Date will appear on invoices.',
            },
            endDate: {
              type: 'date',
              rules: [
                'nullable',
              ],
              columns: {
                container: 6,
                label: 3,
                wrapper: 8,
              },
              full: false,
              placeholder: 'End Date',
              fieldName: 'EndDate',
              description: 'Client Start Date will appear on invoices.',
            },
          }
        },

        container_Contact: {
          type: 'group',
          schema: {
            email: {
              type: 'text',
              inputType: 'email',
              rules: [
                'required',
                'max:255',
                'email',
              ],
              columns: {
                container: 6,
                label: 3,
                wrapper: 8,
              },
              full: false,
              placeholder: 'Email',
              fieldName: 'Email',
              description: 'You will receive a confirmation letter to this email.',
            },

            clientPhone: {
              type: 'text',
              full: false,
              columns: {
                container: 6,
                label: 3,
                wrapper: 8,
              },
              rules: [
                'required',
                'min:10',
                'max:14',
              ],
              placeholder: 'Phone Number',
              fieldName: 'Phone',
              description: 'Client Phone Number will appear on invoices.',
            },

          }
        },

        container_Tax: {
          type: 'group',
          schema: {
            clientPan: {
              type: 'text',
              rules: [
                'required',
                'max:255',

              ],
              full: false,
              columns: {
                container: 6,
                label: 3,
                wrapper: 8,
              },
              placeholder: 'PAN Number',
              fieldName: 'PANNumber',
              description: 'Client PAN number is requried.',
            },
            clientGSTIN: {
              type: 'text',
              rules: [
                'required',
                'max:255',

              ],
              full: false,
              columns: {
                container: 6,
                label: 3,
                wrapper: 8,
              },
              placeholder: 'GSTIN ',
              fieldName: 'GSTIN',
              description: 'Client GSTIN  is requried.',
            },

          }
        },
        contactPerson: {
          type: 'text',
          full: false,
          columns: {
            container: 6,
            label: 3,
            wrapper: 8,
          },
          rules: [
            'min:5',
            'max:255',
          ],
          placeholder: 'Contact Person',
          fieldName: 'ContactPerson',
          description: 'Contact Person will appear on invoices.',
        },
        // clientStatus: {
        //   type: 'text',
        //   full: false,
        //   columns: {
        //     container: 6,
        //     label: 3,
        //     wrapper: 8,
        //   },
        //   rules: [
        //     'min:5',
        //     'max:255',
        //   ],
        //   placeholder: 'Client Status',
        //   fieldName: 'ClientStatus',
        //   description: 'Status of Client.',
        // },
        remarks: {
          type: 'text',
          full: false,
          columns: {
            container: 6,
            label: 3,
            wrapper: 8,
          },
          rules: [

            'max:255',
          ],
          placeholder: 'Remarks',
          fieldName: 'Remarks',
          description: 'Remarks about client',
        },
        status: {
          type: 'checkbox',
          full: false,
          columns: 6,
          text: 'Active',
          before: 'Client Status',
          placeholder: 'Client Status',
          fieldName: 'Active',
          description: 'Client active or inactive.',
        },

        container_Button: {
          type: 'group',
          schema: {
            register: {
              type: 'button',
              size: 'sm',
              buttonLabel: 'Create client',
              full: false,
              submits: true,
              align: 'center',
              columns: 2,

            },
            back: {

              type: 'button',
              buttonLabel: 'Back',
              full: false,
              size: 'sm',
              columns: 1,
              danger: true,
              onclick() {
                this.$router.go(-1)
              },

            },
            reset: {

              type: 'button',
              buttonLabel: 'Reset',
              full: false,
              size: 'sm',
              submits: false,
              resets: true,
              columns: 1,
              secondary: true,
            },
            clear: {

              type: 'button',
              buttonLabel: 'Clear',
              secondary: true,
              full: false,
              size: 'sm',
              submits: false,
              resets: true,
              columns: 1,
            },

          },
        },
      }

    })
    return {
      form,
    }
  },
  methods: {
    goBack() {
      this.$router.go(-1)
    },

  }
}

</script>

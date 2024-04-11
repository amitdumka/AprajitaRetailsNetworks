<script>
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
  setup() {
    const form = ref({
      size: 'sm',
      displayErrors: true,
      schema: {
        page_title: {
          type: 'static',
          content: 'Employee',
          tag: 'h1',
        },
        divider: {
          type: 'static',
          tag: 'hr',
        },
        container: {
          type: 'group',
          schema: {
            first_name: {
              type: 'text',
              placeholder: 'First name',
              columns: {
                container: 6,
                label: 12,
                wrapper: 12,
              },
              fieldName: 'First name',
              rules: [
                'required',
                'max:255',
              ],
            },
            last_name: {
              type: 'text',
              placeholder: 'Last name',
              columns: {
                container: 6,
                label: 12,
                wrapper: 12,
              },
              fieldName: 'Last name',
              rules: [
                'required',
                'max:255',
              ],
            },
          },
          description: 'Make sure it matches your legal name',
        },
        birthday: {
          type: 'date',
          placeholder: 'Birthday',
          fieldName: 'Birthday',
          rules: [
            'required',
          ],
          description: 'Your birthday is not visible others.',
          displayFormat: 'MMMM Do, YYYY',
        }, email: {
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
        register: {
          type: 'button',
          submits: true,
          buttonLabel: 'Create account',
          full: false,
          size: 'sm',
        },

      }

    })
    return {
      form,
    }
  }

})
</script>

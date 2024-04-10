<template>
  <UDashboardPanel :resizable="{ min: 200 }" grow collapsible>
    <UDashboardPanelContent class="pb-24">
      <Vueform v-bind="vueform" />
    </UDashboardPanelContent>

  </UDashboardPanel>
</template>

<script>
import { ref } from 'vue'

export default {
  setup(props, context) {
    const vueform = ref({
      size: 'sm',
      displayErrors: false,
      schema: {
        reservation_title: {
          type: 'static',
          content: 'Payroll Settings',
          description: 'Emails you receive after making a reservation. This includes invitations to review the properties you stayed in.',
          tag: 'h2',
        },
        divider: {
          type: 'static',
          tag: 'hr',
        },
        p: {
          type: 'static',
          content: 'Enable payroll',
          description: 'Email reminders for your upcoming booking with all the info you\'ll need.',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        upcoming: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
          default: true,
        },
        reservation_divider_1: {
          type: 'static',
          tag: 'hr',
        },
        p_1: {
          type: 'static',
          content: 'Enable Leaves',
          description: 'Emails inviting you to leave a review about the property you stayed at.',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        review: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
        },
        reservation_divider_2: {
          type: 'static',
          tag: 'hr',
        },
        p_2: {
          type: 'static',
          content: 'Send payslip over email',
          description: 'Other product deals and upgrades in your confirmation emails.',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        offers: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
          default: true,
        },
        reservation_divider_3: {
          type: 'static',
          tag: 'hr',
        },
        p_3: {
          type: 'static',
          content: 'Payment and Leave details over email',
          description: 'You can\'t unsubscribe from booking confirmation emails.',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        confirmation: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          disabled: true,
          align: 'right',
          default: true,
        },
        promotions_title: {
          type: 'static',
          content: 'Promotions & Deals',
          description: 'Emails based on destinations you\'re interested in and newsletters highlighting deals.',
          tag: 'h2',
          top: '2',
        },
        divider_1: {
          type: 'static',
          tag: 'hr',
        },
        p_4: {
          type: 'static',
          content: 'Deal discovery',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        deal_discovery: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
        },
        promotions_divider_1: {
          type: 'static',
          tag: 'hr',
        },
        p_5: {
          type: 'static',
          content: 'Rewards',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        rewards: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
          default: true,
        },
        promotions_divider_2: {
          type: 'static',
          tag: 'hr',
        },
        p_6: {
          type: 'static',
          content: 'Refer A Friend',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        refer: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
        },
        promotions_divider_3: {
          type: 'static',
          tag: 'hr',
        },
        p_7: {
          type: 'static',
          content: 'Direct mail',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        direct_mail: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
          default: true,
        },
        experience_title: {
          type: 'static',
          content: 'Travel Experiences',
          description: 'Customized info and offers to make your good trip a great one.',
          tag: 'h2',
          top: '2',
        },
        divider_2: {
          type: 'static',
          tag: 'hr',
        },
        p_8: {
          type: 'static',
          content: 'Attractions and tours',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        attractions: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
          default: true,
        },
        experience_divider_1: {
          type: 'static',
          tag: 'hr',
        },
        p_9: {
          type: 'static',
          content: 'Extra services for your stay',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        extra: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
        },
        experience_divider_2: {
          type: 'static',
          tag: 'hr',
        },
        p_10: {
          type: 'static',
          content: 'Restaurant guides and offers',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        restaurant: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
          default: true,
        },
        experience_divider_3: {
          type: 'static',
          tag: 'hr',
        },
        p_11: {
          type: 'static',
          content: 'Shopping and events',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        shopping: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
          default: true,
        },
        experience_divider_4: {
          type: 'static',
          tag: 'hr',
        },
        p_12: {
          type: 'static',
          content: 'Travel guides',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        travel: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
          default: true,
        },
        transportation_title: {
          type: 'static',
          content: 'Transportation',
          description: 'Everything to help you get around – from your flights to transportation during your stay.',
          tag: 'h2',
          top: '2',
        },
        divider_3: {
          type: 'static',
          tag: 'hr',
        },
        p_13: {
          type: 'static',
          content: 'Transportation deals and offers',
          columns: {
            container: 10,
            label: 12,
            wrapper: 12,
          },
          tag: 'p',
        },
        transportation: {
          type: 'toggle',
          columns: {
            container: 2,
            label: 12,
            wrapper: 12,
          },
          align: 'right',
          default: true,
        },
      },
    })

    return {
      vueform,
    }
  }
}
</script>

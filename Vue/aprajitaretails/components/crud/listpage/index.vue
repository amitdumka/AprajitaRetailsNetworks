<!-- Record Listing Page Components -->
<script setup lang="ts">
import {Client,StoreGroup, Store} from "~/types"
import { defineProps } from 'vue';
// rest of your code

const props=defineProps({
  clients: {
    type: Array as PropType<Client[]>,
    default: () => []
  },
  groups: {
    type: Array as PropType<StoreGroup[]>,
    default: () => []
  },
  stores:{
    type: Array as PropType<Store[]>,
    default: () => []
  },
  entities:{
    type: Array as PropType<any[]>,
    default: () => []
  },
  entityName:{
    type: String,
    default: () => ''
  }
})

function getEntities(entityName:string){

  switch(entityName){
    case 'client':
      return props.clients
    case 'group':
      return props.groups
    case 'store':
      return props.stores
    default:
      return props.entities
  }

}


</script>

<template>
  <div>
    <slot />
  </div>
</template>

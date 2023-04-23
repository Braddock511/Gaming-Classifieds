<template>
  <Transition name="slide">
    <div v-if="alert.message" :class="['alert', `alert-${alert.variant}`, 'position-fixed', 'top-0', 'end-0', 'm-3', 'fade', 'show']" role="alert">
      {{ alert.message }}
      <button type="button" class="btn-close" style="font-size: 14px;" data-bs-dismiss="alert" aria-label="Close" @click="alert = {}"></button>
    </div>
  </Transition>
</template>

<script>
  import { Transition } from 'vue';
  export default {
    props: {
      alert: {
        type: Object,
        default: {},
      },
    },
    updated(){
      setTimeout(() => {this.alert.message = ""}, 5000)
    },
    components:{
      Transition
    }
  };
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.5s ease-out, opacity 0.5s ease-out;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
  opacity: 0;
}

.slide-leave-active {
  opacity: 0;
}
</style>
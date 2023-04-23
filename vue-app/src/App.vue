<template>
  <div id="app">
    <router-view/>
  </div>
</template>


<script>
    export default {
        created() {
          if (!this.$cookies.get('user-login')) {
            this.$cookies.set('user-login', false, '0', '/', '', false, 'Lax');
          }
        }
    }
</script>
<template>
  <div id="app">
    <router-view/>
  </div>
</template>


<script>
    export default {
        created() {
          if (!this.$cookies.get('user-login-flag')) {
            this.$cookies.set('user-login-flag', false, '0', '/', '', false, 'Lax');
            this.$cookies.set('user-login', "", '0', '/', '', false, 'Lax');
          }
        }
    }
</script>
<template>
    <TheHeader/>
    <section id="form-container" v-if="!loading">
        <form id="login-register-form" @submit.prevent="loginUser">
            <div class="title">Login</div>
            <div class="input-container">
                <input v-model="login" id="login" class="input" type="text" placeholder="Login" required/>
            </div>
            <div class="input-container">
                <input v-model="password" id="password" class="input" type="password" placeholder="Password" required/>
            </div>
            <button class="btn btn-primary" type="submit" style="padding: 0.5rem; font-size: 20px;">Login</button>
        </form>
    </section>
    <div id="loading" v-if="loading">
        <img src="@/assets/spinner.gif" alt="loading">
    </div>
    <TheAlert :alert="alert"/>
</template>

<script>
    import TheHeader from '@/components/TheHeader.vue'
    import TheAlert from '../components/TheAlert.vue'
    import axios from 'axios'

    export default{
        data(){
            return{
                login: "",
                password: "",
                response: "",
                alert: {},
                loading: false,
            }
        },
        methods:{
            async loginUser(){
                this.loading = true
                this.response = await axios.post("http://127.0.0.1:8000/login", {login: this.login, password: this.password})
                if (this.response.data.status == 200){
                    this.alert = {variant: "success", message: "Login - success"}
                    this.$cookies.set('user-login-flag', true, '', '/', '', false, 'Lax')
                    this.$cookies.set('user-login', this.login, '', '/', '', false, 'Lax')
                    setTimeout(()=>{this.$router.push("/")}, 2000)
                }
                else if (this.response.data.status == 404){
                    this.alert = {variant: "warning", message: "Wrong password or login"}
                    this.loading = false
                }
            }
        },
        components: {
            TheHeader,
            TheAlert
        }
    }
</script>

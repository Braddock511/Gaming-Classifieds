<template>
    <TheHeader/>
    <section id="form-container" v-if="!loading">
        <form id="login-register-form" @submit.prevent="register">
            <div class="title">Register</div>
            <div class="input-container">
                <input v-model="login" id="login" class="input" type="text" placeholder="Login" required/>
            </div>
            <div class="input-container">
                <input v-model="password" id="password" class="input" type="password" placeholder="Password" required/>
            </div>
            <div class="input-container">
                <input v-model="email" id="email" class="input" type="email" placeholder="Email" required/>
            </div>
            <button class="btn btn-primary" type="submit" style="padding: 0.5rem; font-size: 20px;">Register</button>
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
                email: "",
                response: "",
                alert: {},
                loading: false
            }
        },
        methods:{
            validPassword() {
                const regex = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
                return this.password.length >= 6 && regex.test(this.password);
            },
            async register(){
                if (this.validPassword()){
                    this.loading = true
                    this.response = await axios.post("http://127.0.0.1:8000/register", {login: this.login, password: this.password, email: this.email})
                    if (this.response.data.status == 200){
                        this.alert = {variant: "success", message: "Register - success"}
                        this.$cookies.set('user-login-flag', true, '', '/', '', false, 'Lax')
                        this.$cookies.set('user-login', this.login, '', '/', '', false, 'Lax')
                        setTimeout(()=>{this.$router.push("/")}, 2000)
                    }
                    else if (this.response.data.status == 401){
                        this.alert = {variant: "warning", message: "User exists"}
                        this.loading = false
                    }
                }
                else{
                    this.alert = {variant: "warning", message: "Password must be 6 characters and 1 special character"}
                }
            },
        },
        components: {
            TheHeader,
            TheAlert
        }
    }
</script>

<template>
    <TheHeader/>
    <section id="form-container">
        <form id="login-register-form" @submit.prevent="register" v-if="!registerFlag">
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

        <div id="result" v-if="registerFlag">
            <h1>Rejestracja success</h1>
            <h2>Login: {{ login }}</h2>
            <h2>Email: {{ email }}</h2>
        </div>
    </section>
    
</template>

<script>
    import TheHeader from '@/components/TheHeader.vue'
    import axios from 'axios'

    export default{
        data(){
            return{
                login: "",
                password: "",
                email: "",
                response: "",
                registerFlag: false
            }
        },
        methods:{
            async register(){
                this.response = await axios.post("http://127.0.0.1:8000/register", {login: this.login, password: this.password, email: this.email})
                console.log(this.response)
                if (this.response.data.result == 200){
                    this.registerFlag = true
                    setTimeout(()=>{this.$router.push("/")}, 3000)
                }
            }
        },
        components: {
            TheHeader,
        }
    }
</script>

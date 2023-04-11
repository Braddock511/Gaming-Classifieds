<template>
    <TheHeader/>
    <section id="form-container">
        <form id="login-register-form" @submit.prevent="loginUser" v-if="!loginFlag">
            <div class="title">Login</div>
            <div class="input-container">
                <input v-model="login" id="login" class="input" type="text" placeholder="Login" required/>
            </div>
            <div class="input-container">
                <input v-model="password" id="password" class="input" type="password" placeholder="Password" required/>
            </div>
            <button class="btn btn-primary" type="submit" style="padding: 0.5rem; font-size: 20px;">Login</button>
        </form>
        <div id="result" v-if="loginFlag">
            <h1>{{ result }}</h1>
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
                response: "",
                result: "",
                loginFlag: false
            }
        },
        methods:{
            async loginUser(){
                this.response = await axios.post("http://127.0.0.1:8000/login", {login: this.login, password: this.password})
                console.log(this.response)
                if (this.response.data.result == 200){
                    this.loginFlag = true
                    this.result = "Logowanie udane"
                    setTimeout(()=>{this.$router.push("/")}, 2000)
                }
                else if (this.response.data.result == 404){
                    this.loginFlag = true
                    this.result = "Wrong login or password"
                    setTimeout(()=>{this.loginFlag = false}, 2000)
                }
            }
        },
        components: {
            TheHeader,
        }
    }
</script>

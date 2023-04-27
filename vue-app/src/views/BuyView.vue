<template>
    <TheHeader/>
    <div id="container" v-if="!loading">
        <form @submit.prevent="buy">
            <main>
                <div id="left">
                    <div id="client-data">
                    <h2>Payment information</h2>
            
                    <div class="block">
                        <label for="email">Email address <span class="red">*</span></label>
                        <input type="email" id="email" name="email" required v-model="order.email">
                    </div>
            
                    <div class="block">
                        <label for="name">First and last name <span class="red">*</span></label>
                        <input type="text" id="name" name="name" required v-model="order.name">
                    </div>
            
                    <div class="block">
                        <label for="phone">Phone number <span class="red">*</span></label>
                        <input type="tel" id="phone" name="phone" pattern="[0-9]{9}" maxlength="9" required title="Enter phone number in format XXXXXXXXX" v-model="order.phone">
                    </div>
            
                    <h2>Shipping information</h2>
            
                    <div class="block">
                        <label for="city">City, postal code <span class="red">*</span></label>
                        <div class="sublock">
                        <input type="text" id="city" name="city" required v-model="order.city">
                        <input type="text" id="city" name="code" pattern="[0-9]{2}-[0-9]{3}" maxlength="6" style="width: 20%;" required title="Enter postal code in format XX-XXX" v-model="order.postalCode">
                        </div>
                    </div>
            
                    <div class="block">
                        <label for="address">Address, building number, apartment number <span class="red">*</span></label>
                        <div class="sublock">
                        <input type="text" id="address" name="address" required v-model="order.address">
                        <input type="text" id="address" name="buildingNumber" required style="width: 15%;" v-model="order.buildingNumber">
                        <input type="text" id="address" name="apartmentNumber" style="width: 15%;" v-model="order.apartmentNumber">
                        </div>
                    </div>
            
                    <div class="block">
                        <label for="instructions">Order instructions</label>
                        <textarea id="instructions" name="instructions" v-model="order.instructions"></textarea>
                    </div>
                    </div>
                </div>
            </main>
            <div id="right">
                <h2>Payment</h2>
                
                <div class="pay-price"><h4>Products</h4> <h4>{{ (totalPrice()).toFixed(2) }}€</h4></div>
                <div class="pay-price"><h4>Delivery</h4> <h4>3.99€</h4></div>
                <div class="pay-price"><h3>Total</h3> <h3>{{ (totalPrice() + 3.99).toFixed(2) }}€</h3></div>

                <button class="btn btn-primary w-100" type="submit" style="padding: 0.5rem; font-size: 20px;">Buy</button>
            </div>
        </form>
    </div>
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
        data() {
            return {
                cart: [],
                order: {
                    email: '',
                    name: '',
                    phone: '',
                    city: '',
                    postalCode: '',
                    address: '',
                    buildingNumber: '',
                    apartmentNumber: '',
                    instructions: '',
                    products_id: [],
                    price: ''
                },
                alert: {},
                loading: false
            };
        },
        methods:{
            totalPrice() {
                return parseFloat(this.cart.reduce((total, product) => total + product.price, 0))
            },
            async buy(){
                this.loading = true
                this.order.products_id = this.$store.state.cart
                this.order.price = (this.totalPrice() + 3.99).toFixed(2)
                const response = await axios.post("http://127.0.0.1:8000/order", {order: this.order})
                console.log(response)
                if (response.data.status == 200){
                    this.$store.state.cart = []
                    this.alert = {variant: "success", message: "Success"}
                    setTimeout(()=>{this.$router.push("/")}, 2000)
                }
                else if (response.data.status == 404){
                    this.alert = {variant: "warning", message: "Something went wrong"}
                }
            }
        },
        async mounted(){
            for (let i = 0; i < this.$store.state.cart.length; i++){
                const gameId = this.$store.state.cart[i]

                let url = 'http://127.0.0.1:8000/get-game'
                url += this.$store.state.id ? `?game_id=${gameId}` : ''
                const game = (await axios.get(url).then(response => response.data.output))[0]

                this.cart.push(game)
            }
        },
        components: {
            TheHeader,
            TheAlert
        }
    }
</script>

<style lang="scss" scoped>
    $primary-color: rgb(20, 24, 24);

    #container{
        form{
            display: flex;
            justify-content: center;
            margin-top: 10px;

            #right{
                display: flex;
                flex-direction: column;
                width: 25%;
                height: 400px;
                background-color: $primary-color;
                gap: 30px;
                padding: 30px;

                .pay-price{
                    display: flex;
                    justify-content: space-between;
                }
            }

            main{
        display: flex;
        width: 45%;
        margin-bottom: 10px;
        
        #left{
            background-color: $primary-color;
            padding: 20px;
            margin-right: 10px;
            width: 100%;

            #client-data{
                width: 100%;
                display: flex;
                flex-direction: column;
                gap: 10px;

                h2{
                    margin-bottom: 10px;
                }
                
                .block{
                    label {
                    font-weight: bold;
                    margin-bottom: 10px;
                    display: flex;
                    }

                    input, textarea {
                        width: 60%;
                        padding: 10px;
                        border-radius: 5px;
                        margin-bottom: 20px;
                        color: white;
                        box-sizing: border-box;
                        resize: none;
                    }

                    textarea{
                        height: 100px;
                    }

                    .sublock{
                        display: flex; 
                        gap: 5px;
                    }
                }
            }
        }   
    }

        }
    }

    @media only screen and (max-width: 1400px) {
        #container{
            form{
                flex-direction: column;
                main{
                    width: 100%;
                    margin-left: 5px;
                }
                #right{
                    width: 100%;
                    margin-top: 10px;
                }
            }
        }
    }
        
</style>
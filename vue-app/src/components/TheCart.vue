<template>
    <div id="container">
        <main v-if="!productsCounter">
            <div id="empty">
                <h2>Your cart is empty</h2>
            </div>
        </main>

        <main v-if="productsCounter">
            <div id="not-empty">
                <div id="left">
                    <h2>Your cart</h2>
                    
                    <div class="order-product" v-for="product in cart" :key="product">
                        <div class="subblock">
                            <img :src="product.image_url" alt="order-product"/>

                            <h4 @click="goToProduct(product.id)">{{product.title}}</h4>

                            <span id='pln'>
                                {{product.price}}€
                            </span>

                            <img src="../assets/svg/exit.svg" id='delete' @click="deleteGame(product)"/>
                        </div>
                    </div>
                </div>
                <div id="right">
                    <h2>Price</h2>

                    <div class='price'><span>Products</span> <span>{{ (totalPrice()).toFixed(2) }}€</span></div>
                    <div class='price'><span>Delivery</span> <span>3.99€</span></div>
                    <div class='price'><span>Total</span> <span>{{ (totalPrice() + 3.99).toFixed(2) }}€</span></div>

                    <router-link to="/buy"><button class="btn btn-primary w-100" type="submit" style="padding: 0.5rem; font-size: 20px;">Delivery and payment</button></router-link>
                </div>
            </div>
        </main>
    </div>
</template>

<script>
    import axios from 'axios';

    export default{
        data(){
            return{
                cart: [],
                productsCounter: this.$store.state.cart.length
            }
        },
        methods:{
            totalPrice() {
                return parseFloat(this.cart.reduce((total, product) => total + product.price, 0))
            },
            deleteGame(game) {
                const index = this.cart.indexOf(game)
                if (index !== -1) {
                    this.cart.splice(index, 1)
                    this.$store.state.cart.splice(index, 1)
                 
                    if (this.cart.length == 0){
                        this.$router.go(0)
                    }
                }
            },
            goToProduct(gameId){
                this.$store.state.id = gameId
                localStorage.removeItem('game')
                this.$router.push('/product')
            }
        },
        async mounted(){
            for (let i = 0; i < this.productsCounter; i++){
                const gameId = this.$store.state.cart[i]

                let url = 'http://127.0.0.1:8000/get-game'
                url += this.$store.state.id ? `?game_id=${gameId}` : ''
                const game = (await axios.get(url).then(response => response.data.output))[0]

                this.cart.push(game)
            }
        },
        watch: {
            '$store.state.cart': {
                handler(newValue){
                if (newValue) {
                        this.productsCounter = this.$store.state.cart.length
                    }
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
    $primary-color: rgb(20, 24, 24);

    #container{
        display: flex;
        justify-content: center;
    }

    main{
        width: 80%;
        display: flex;
        justify-content: center;
    }
    
    #empty{
        background-color: $primary-color;
        width: 100%;
        min-width: 500px;
        height: 500px;
        margin: 10px;
        padding: 20px;
    }

    #not-empty{
        width: 100%;
        min-width: 500px;
        padding: 10px;
        display: flex;
        gap: 10px;

        h2{
                text-align: center;
            }

        #left{
            background-color: $primary-color;
            width: 70%;
            padding: 10px;


            .order-product{
                padding: 10px;
                font-size: 24px;
                border-bottom: 1px solid rgb(94, 94, 94);
                
                .subblock{
                    min-width: 100%;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    
                    h4{
                        max-width: 400px;
                        margin-left: 10px;
                        margin-right: 10px;
                        cursor: pointer;

                        &:hover{
                            color:gray;
                        }
                    }

                    img{
                        width: 120px;
                        height: 120px;
                        background-position: center;
                    }

                    #pln{
                        white-space: nowrap;
                    }

                    #delete{
                        width: 35px;
                        height: 35px;
                        cursor: pointer;

                        &:hover{
                            opacity: 0.5;
                        }
                    }
                }
            }
        }

        #right{
            width: 50%;
            height: 380px;
            background-color: $primary-color;
            display: flex;
            flex-direction: column;
            gap: 30px;
            padding: 10px;
            font-size: 22px;

            .price{
                display: flex;
                justify-content: space-between;
            }

        }
    }

    @media only screen and (max-width: 1665px) {
        main{
            width: 95%;
        }
    }

    @media only screen and (max-width: 1400px) {
        #not-empty{
            flex-direction: column;

            #left{
                width: 100%;
            }

            #right{
                width: 100%;
            }
        }
    }

    @media only screen and (max-width: 820px) {
        #not-empty{
            #left{
                .order-product{
                    font-size: 18px;
                    .subblock{

                        img{
                            width: 125px;
                            height: 125px;
                        }
                    }
                }
            }
        }
    }

    @media only screen and (max-width: 700px) {
        #not-empty{
            #left{
                .order-product{
                    font-size: 16px;
                    .subblock{

                        img{
                            width: 125px;
                            height: 125px;
                        }

                        #delete{
                            width: 25px;
                            height: 25px;
                            margin-left: 10px;
                        }
                    }
                }
            }
        }
    }

    @media only screen and (max-width: 500px) {
        #container{
        width: 500px;
        }
    }
</style>
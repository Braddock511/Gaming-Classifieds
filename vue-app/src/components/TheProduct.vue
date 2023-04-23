<template>
    <main>
        <vue-easy-lightbox
            scrollEnabled
            escEnabled
            moveEnabled
            :visible="visible"
            :imgs="game.image_url"
            :zoomScale="1.5"
            @hide="visible = false">
        </vue-easy-lightbox>
        <article>
            <img :src="game.image_url" @click="visible = true" width="500" height="450"/>
            <ul class="information">
                <h2>{{ game.title }}</h2>
                <li>Genre: {{ game.genre }}</li>
                <li>Platform: {{ game.platform }}</li>
                <h2>{{ game.price }} €</h2>
                <button class="btn btn-primary" type="submit" style="padding: 0.5rem; font-size: 20px;" @click="addToCart(game.id)">Add to cart</button>
            </ul>
        </article>

        <nav>
            <h1 style="margin-bottom: 50px;">Description</h1>
            <div id="description">
                {{ game.description }}
            </div>
        </nav>
    </main>
</template>

<script>
    import VueEasyLightbox from 'vue-easy-lightbox'
    import axios from 'axios'

    export default{
        data(){
            return{
                game: "",
                currentIndex: 0,
                visible: false
            }
        },
        methods:{
            addToCart(productId) {
                this.$store.state.cart.push(productId);
                localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
                this.$router.push("/shopping-cart")
            },
        },
        async mounted(){
            // Get game
            let url = 'http://127.0.0.1:8000/get-game'
            url += this.$store.state.id ? `?game_id=${this.$store.state.id}` : ''

            // Check if game data is in local storage
            if(localStorage.getItem('game')){
                this.game = JSON.parse(localStorage.getItem('game'))
            }else{
                // Fetch game data from server
                this.game = (await axios.get(url).then(response => response.data.output))[0]

                // Store game data in local storage
                localStorage.setItem('game', JSON.stringify(this.game))
            }

            // Setup slider
            const images = [this.game.image_url]
            const promises = images.map(imgSrc => {
                return new Promise(resolve => {
                    const img = new Image()
                    img.onload = resolve
                    img.src = imgSrc
                })
            })
            Promise.all(promises).then(() => {
                this.loading = false
            })
        },
        components:{
            VueEasyLightbox
        }
    }
</script>

<style lang="scss" scoped>
    $primary-color: rgb(20, 24, 24);
    $second-color: rgb(34, 36, 36);
    main{
        display: flex;
        flex-direction: column;
        margin-top: 10px;
        background-color: $primary-color;
        article{
            display: flex;
            justify-content: center;
            gap: 100px;
            padding: 11.5px;
            img{
                opacity: 0.85;
                cursor: pointer;
                &:hover{
                    opacity: 1;
                }
            }
            .information{
                display: flex;
                flex-direction: column;
                gap: 10px;
                width: 300px;
                li{
                    font-size: 18px;
                }
            } 
        }

        nav{
            background-color: $second-color;
            padding: 30px;
            margin-top: 10px;

            #description{
                font-size: 20px;
            }
        }
    }

    @media only screen and (max-width: 900px){
        main{

            article{
                flex-direction: column;
                align-items: center;
                gap: 10px 0px;

                img{
                    width: 400px;
                    height: 350px;
                }
            }
        }
    }


    @media only screen and (max-width: 600px){
        main{
            min-width: 500px;
        }
    }
</style>
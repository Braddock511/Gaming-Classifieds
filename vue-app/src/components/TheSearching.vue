<template>
    <main>
        <div class="sort">
            <div class="filter">
                <b @click="filterClick">
                    Filtry
                </b>
                
                <div v-if="filterFlag" class="filters">
                    <div style="display: flex; justify-content: flex-end; padding: 10px;">
                        <img @click="filterClick" v-if="filterFlag" src='../assets/svg/exit.svg' style="z-index: 2">
                    </div>
                    <TheSorting id="filter-nav"/>
                </div>

            </div>
            
            <span style="width: 100%; display: flex; justify-content: end;">
                <select v-model="selected"> 
                    <option value="">Sort</option>
                    <option value="lowest">Price: low-high</option>
                    <option value="highest">Price: high-low</option>
                </select>
            </span>
        </div>

        
        <div v-if="products.length > 0" class="product" v-for="product in  products" :key="product.title" @click="goToProduct(product.id)">            
            <img :src="product.image_url" width="200" height="200">
            
            <div class="description">
                <span>{{product.title}}</span>
                <span>{{product.price}} €</span>
            </div>
        </div> 

        <div v-if="products.length == 0">
            <h2>Not found</h2>
        </div>

    </main>
</template>

<script>
    import TheSorting from '@/components/TheSorting.vue'
    
    export default{
        data(){
            return{
                selected: "",
                products: [],
                filterFlag: false,
            }
        },
        methods:{
            filterClick(){
                this.filterFlag = !this.filterFlag
            },
            goToProduct(gameId){
                this.$store.state.id = gameId
                localStorage.removeItem('game')
                this.$router.push('/product')
            }
        },
        mounted(){
            this.products = this.$store.getters.filteredGamesBySearch(this.$store.state.searchQuery)
        },
        watch: {
            '$store.state.searchQuery': {
                handler(newValue) {
                if (newValue) {
                        this.products = this.$store.getters.filteredGamesBySearch(newValue)
                        this.$store.state.searchQuery = ""
                    }
                },
            },
            '$store.state.games': {
                handler(newGames) {
                    this.$store.state.searchQuery = ""
                    this.products = newGames
                },
            },
            'selected':{
                handler(){
                    if (this.selected === "lowest") {
                    return this.products.sort((a, b) => a.price - b.price);
                    } 
                    else if (this.selected === "highest") {
                        return this.products.sort((a, b) => b.price - a.price);
                    } 
                }
            }
        },
        
        components:{
            TheSorting,
        },
    }
</script>

<style lang="scss" scoped>
    $primary-color: rgb(20, 24, 24);
    $second-color: rgb(34, 36, 36);

    main{
        background-color: $primary-color;
        width: 100%;
        margin-right: 20px;
        padding: 10px;
        padding-left: 30px;
        padding-right: 30px;
        display: flex;
        flex-direction: column;
        gap: 30px;
    

        .sort{
            background-color: $second-color;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            padding: 10px;
            
            .filter{
                display: none;
                margin-top: 20px;      
                margin-right: 10px;
                font-size: 18px;
                cursor: pointer;

                .filters{
                    position: absolute;
                    z-index: 100;
                    top: 0;
                    right: 0;
                    width: 100%;
                    height: 200vh;
                    background-color: rgb(20, 24, 24);
                    cursor: default;

                    img{
                        cursor: pointer;
                    }

                    #filter-nav{
                        display: flex;
                    }

                }
            }

            select{
                width: 300px;
            }
        }

        .product{
            font-size: 20px;
            display: flex;
            border-bottom: 3px solid $second-color;
            padding: 10px;
            cursor: pointer;
            .description{
                display:flex;
                flex-direction: column;
                justify-content: space-around;
                margin-top: 40px;
                margin-left: 10px;
                font-size: 24px;
            }

            &:hover{
                background-color: $second-color;
            }
        }
    }

    @media only screen and (max-width: 1030px){
        main{
            .sort{
                .filter{
                    display: block;
                }
                span{
                    justify-content: center !important;
                }
            }
        }
    }

    @media only screen and (max-width: 500px){
        main{
            width: 500px;
        }
    }
</style>
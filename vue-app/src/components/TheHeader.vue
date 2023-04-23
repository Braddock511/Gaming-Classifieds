<template>
  <header>
        <router-link to='/' id="logo"><img src='../assets/logo.png' alt='logo' width="100" height="100"></router-link>

        <input v-model="searchQuery" type="text" placeholder="Search" id="searchbar" @keydown.enter="searchGames">
        <button id="search-button" @click="searchGames"><img src='../assets/svg/search.svg'></button>
        
        <div class="user-block">
          <div class="text" style="font-size: 26px;">
            <router-link to="/shopping-cart">
                <span><img src='../assets/svg/cart.svg'></span>
                <span v-if="productsCounter" id="counter-products">{{productsCounter}}</span>
            </router-link>
          </div>
          
          <div v-if='isLogin' class="text"><router-link to="/listing"><span>Listing offer</span></router-link></div>
          <div v-if='!isLogin' class="text"><router-link to="/login"><span>Login</span></router-link></div>
          <div v-if='!isLogin' class="text"><router-link to="/register"><span>Register</span></router-link></div>
        </div>
        
        <div class="hamburger">
          <img @click="hamburgerClick" v-if="!hamburgerFlag" src='../assets/svg/hamburger.svg'>
          <img @click="hamburgerClick" v-if="hamburgerFlag" src='../assets/svg/exit.svg' style="z-index: 2;">
          <div v-if="hamburgerFlag" id="hamburger-div">
            <div v-if='isLogin' class="text"><router-link to="/listing"><span>Listing offer</span></router-link></div>
            <div v-if='!isLogin' class="text"><router-link to="/login"><span>Login</span></router-link></div>
            <div v-if='!isLogin' class="text"><router-link to="/register"><span>Register</span></router-link></div>
            <div class="text">
              <router-link to="/shopping-cart">
                <span>Koszyk</span>
              </router-link>
            </div>
          </div>
        </div>
  </header>
</template>

<script>
  export default{
    data(){
      return {
        options: "Wszystkie kategorie",
        hamburgerFlag: false,
        hover: false,
        searchQuery: "",
        totalPrice: 0,
        productsCounter: this.$store.state.cart.length
      }
    },
    computed: {
      isLogin() {
          return this.$cookies.get("user-login") === "true"
      },
    },
    methods:{
      hamburgerClick(){
        this.hamburgerFlag = !this.hamburgerFlag
        
      },
      searchGames(){
        this.$store.state.searchQuery = this.searchQuery
        this.$router.push('/search-view')
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

<style scoped lang="scss">
  header{
    display: flex;
    position: sticky;
    width: 100%;
    background-color: rgb(34, 36, 36);
    padding: 10px;    
      
    #searchbar{
      align-self: center;
      width: 70%;
      height: 39%;
      padding: 10px;
      margin-left: 40px;
    }
    
    #search-button{
      background-color: #202222;
      align-self: center;
      border: 1px solid black;
      cursor: pointer;
      width: 10%;
      padding: 8px;
      border-left: 0px;
      min-width: 40px;
      border-radius: 5%;

      &:hover{
        opacity: 0.8;
      }
    }
    .user-block{
      display: flex;
      justify-content: flex-end;
      width: 50%;
      
      .text{
        position: relative;
        align-self: center;
        padding: 5px;
        margin-right: 80px;
        font-size: 20px;
        
        &:hover{
          opacity: 0.7;
        }
        
        #counter-products{
          position: absolute;
          font-size: 15px;
          padding: 0.250em;
          border-radius: 90em;
          margin-top: 20px;
          font-weight: 600;
        }
      }
    }
    .hamburger{
      display: none;
      
      #hamburger-div{
        position: absolute;
        cursor: default;
        text-align: center;
        z-index: 1;
        top: 0;
        right: 0;
        width: 50%;
        height: 925%;
        background-color: rgb(20, 24, 24);
        opacity: 0.95;

        .text{
          padding-top: 30px;
          font-size: 26px;

          span:hover{
            color:gray;
            opacity: 0.8;
          }
        }
      }
    }
  }


  @media only screen and (max-width: 1150px) {
    header{
      .user-block{
        display: none;
      }

      #search{
        display: flex;
        width: 75%;
        margin-left: 0px;
      }
      .hamburger{
        display: flex;
        justify-content: flex-end;
        cursor: pointer;
        padding: 20px;
        width: 38%;

        img{
          width: 48px;
        }
      }
    }
  }


  @media only screen and (max-width: 500px){
    header{
      width: 500px;
    }
  }
</style>

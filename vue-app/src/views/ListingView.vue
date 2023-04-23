<template>
    <TheHeader/>

    <div id="container">
        <div id="left">
            <h1>Game Image</h1>
            <label for="file-upload" ref="fileLabel" style="cursor: pointer;">
            <img v-if="!image" src="https://placehold.co/1920x1080" alt="Placeholder image">
            <img v-else :src="image" alt="Uploaded image">
            </label>
            <input ref="fileInput" id="file-upload" type="file" @change="onFileChange" style="display: none;" required>
        </div>

        <div id="right">
            <h1 style="text-align: center;">Parameters</h1>
            <form @submit.prevent="addGame">
            <div class="input-container">
                <label><h2>Title</h2></label>
                <input type="text" v-model="title" required>
            </div>
            
            <div class="input-container">
                <label><h2>Description</h2></label>
                <textarea v-model="description" required></textarea>
            </div>

            <div class="input-container">
                <label><h2>Genre</h2></label>
                <select v-model="genre" required>
                    <option value="Action">Action</option>
                    <option value="Adventure">Adventure</option>
                    <option value="RPG">RPG</option>
                    <option value="Strategy">Strategy</option>
                    <option value="Simulation">Simulation</option>
                    <option value="Sports">Sports</option>
                    <option value="Horrors">Horrors</option>
                    <option value="Survivals">Survivals</option>
                    <option value="MMO">MMO</option>
                    <option value="Puzzle">Puzzle</option>
                </select>
            </div>

            <div class="input-container">
                <label><h2>Platform</h2></label>
                <select v-model="platform" required>
                    <option value="PS4">PlayStation 4</option>
                    <option value="PS5">PlayStation 5</option>
                    <option value="XboxOne">Xbox One</option>
                    <option value="Xbox360">Xbox 360</option>
                    <option value="Pc">PC</option>
                </select>
            </div>

            <div class="input-container">
                <label><h2>Price (€)</h2></label>
                    <input type="number" step="0.01" v-model="price" required>
            </div>

            <div class="input-container">
                <button class="btn btn-primary" type="submit" style="padding: 0.5rem; font-size: 20px;" @click="listingGmae">Add game</button>
            </div>
            </form>
        </div>
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
                title: '',
                description: '',
                genre: 'Action',
                platform: 'PS4',
                price: '',
                image: '',
                response: "",
                alert: {},
            }
        },
        methods:{
            async listingGmae(){
                const newGame = {
                    title: this.title,
                    description: this.description,
                    genre: this.genre,
                    platform: this.platform,
                    price: this.price,
                    image: this.image,
                };

                this.response = await axios.post("http://127.0.0.1:8000/listing-game", {newGame})
                
                if (this.response.data.status == 200){
                    this.alert = {variant: "success", message: "Listing - success"}
                    setTimeout(()=>{this.$router.push("/")}, 2000)
                }
                else if (this.response.data.status == 404){
                    this.alert = {variant: "warning", message: "Something went wrong"}
                }
            },
            onFileChange(event) {
                const selectedFile = event.target.files[0]
                const reader = new FileReader()
                reader.readAsDataURL(selectedFile)
                reader.onload = () => {
                    this.image = reader.result
                };
            },
            onPlaceholderClick() {
                this.$refs.fileInput.click()
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
        display: flex;
        justify-content: center;
        margin-top: 10px;
        gap: 10px;

        #left{
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 50%;
            background-color: $primary-color;
            padding: 10px;

            img{
                padding: 30px;
                border-radius: 50px;
                max-width: 100%;
                height: auto;
            }
        }

        #right{
            background-color: $primary-color;
            display: flex;
            align-content: center;
            flex-direction: column;
            padding: 30px;
            width: 30%;
            .input-container{
                display: flex;
                flex-direction: column;
                margin-bottom: 35px;

                select, input, textarea{
                    align-self: normal;
                    background-color: #2f3131;
                }
            }
        }

        
    }

    @media only screen and (max-width: 1100px){
            #container{
                flex-direction: column;

                #left{
                    width: 100%;
                }

                #right{
                    width: 100%;
                }
            }
    }

    @media only screen and (max-width: 500px){
        #container{
            width: 500px;
        }
    }
</style>
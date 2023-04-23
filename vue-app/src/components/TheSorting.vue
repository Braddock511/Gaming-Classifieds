<template>
    <nav>
        <h2 style="margin-bottom: 10px;">Filtres</h2>

        <h3>Genre</h3>
        <div class="radio-label">
            <label>
                <input v-model="genre" value="All" type="radio" name="genre" checked/>
                <span>All</span>
            </label>
            <label>
                <input v-model="genre" value="Action" type="radio" name="genre"/>
                <span>Action</span>
            </label>
            <label>
                <input v-model="genre" value="Adventure" type="radio" name="genre"/>
                <span>Adventure</span>
            </label>
            <label>
                <input v-model="genre" value="RPG" type="radio" name="genre"/>
                <span>RPG</span>
            </label>
            <label>
                <input v-model="genre" value="Strategy" type="radio" name="genre"/>
                <span>Strategy</span>
            </label>
            <label>
                <input v-model="genre" value="Simulation" type="radio" name="genre"/>
                <span>Simulation</span>
            </label>
            <label>
                <input v-model="genre" value="Sports" type="radio" name="genre"/>
                <span>Sports</span>
            </label>
            <label>
                <input v-model="genre" value="Horrors" type="radio" name="genre"/>
                <span>Horrors</span>
            </label>
            <label>
                <input v-model="genre" value="Survivals" type="radio" name="genre"/>
                <span>Survivals</span>
            </label>
            <label>
                <input v-model="genre" value="MMO" type="radio" name="genre"/>
                <span>MMO</span>
            </label>
            <label>
                <input v-model="genre" value="Puzzle" type="radio" name="genre"/>
                <span>Puzzle</span>
            </label>
        </div>

        <h3>Platform</h3>

        <div class="radio-label">
            <label>
                <input v-model="platform" value="All" type="radio" name="platform" checked/>
                <span>All</span>
            </label>
            <label>
                <input v-model="platform" value="PC" type="radio" name="platform"/>
                <span>PC</span>
            </label>
            <label>
                <input v-model="platform" value="PS4" type="radio" name="platform"/>
                <span>PS4</span>
            </label>
            <label>
                <input v-model="platform" value="PS5" type="radio" name="platform"/>
                <span>PS5</span>
            </label>
            <label>
                <input v-model="platform" value="Xbox One" type="radio" name="platform"/>
                <span>Xbox One</span>
            </label>
            <label>
                <input v-model="platform" value="Xbox 360" type="radio" name="platform"/>
                <span>Xbox 360</span>
            </label>
            
        </div>
        <button class="btn btn-primary" type="submit" @click="sortGames" style="padding: 0.5rem; font-size: 20px;">Search</button>
    </nav>
</template>

<script>
    import axios from 'axios'

    export default{
        data(){
            return{
                selected: [],
                genre: "",
                platform: ""
            }
        },
        methods:{
            async sortGames() {
                let url = 'http://127.0.0.1:8000/get-games'
                url += this.genre ? `?genre=${this.genre}` : ''
                url += this.platform ? `${url.includes('?') ? '&' : '?'}platform=${this.platform}` : ''
                let games = await axios.get(url).then(response => response.data.output)
                this.$store.state.games = games
            }
        }
    }
</script>

<style lang="scss" scoped>
    $primary-color: rgb(20, 24, 24);

    nav{
        background-color: $primary-color;
        padding: 10px;
        min-width: 300px;
        display: flex;
        flex-direction: column;
        gap: 20px;
        z-index: 2;
        
        .radio-label{
            display: flex;
            flex-direction: column;
        }
        
        
        label{
            cursor: pointer;
            position: relative;
            overflow: hidden;
            margin-bottom: 0.375em;
            
            input {
                position: absolute;
                left: -9999px;
                &:checked + span {
                    background-color: mix(gray, $primary-color, 84%);
                    &:before {
                        box-shadow: inset 0 0 0 0.35em $primary-color;
                    }
                }
            }
            
            span {
                display: flex;
                align-items: center;
                padding: 0.375em 0.75em 0.375em 0.375em;
                border-radius: 90em;
                transition: 0.25s ease;
                
            &:before {
                    display: flex;
                    flex-shrink: 0;
                    content: "";
                    background-color: white;
                    width: 1.05em;
                    height: 1.05em;
                    border-radius: 50%;
                    margin-right: 0.375em;
                    transition: 0.25s ease;
                    box-shadow: inset 0 0 0 0.2em $primary-color;
                }
            }
        }
    }
    
    @media only screen and (max-width: 1030px){
        #container{

            nav{
                display:none;
            }
        }
    }
</style>
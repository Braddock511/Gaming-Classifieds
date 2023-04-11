<template>
    <main>
        <nav>
            <h2>Categories</h2>
            <div class="category" v-for="(category) in categories">
                <router-link :to="category.url">
                    <table>
                        <tr>
                            <td>
                                <span style="margin-left: 10px;">{{category.value}}</span>
                            </td>
                        </tr>
                    </table>
                </router-link>
            </div>
        </nav>
        
        <aside>
            <h2>Worth seeing</h2>
            <div id="blocks">
                <div id="wrap">
                    <router-link  to="/" class="block" v-for="x in test">
                        <div class="description">
                            {{ x.title }}
                        </div>
                    </router-link>
                </div>
            </div>
        </aside>
    </main>
</template>

<script>
    export default{
        data(){
            return{
                categories:[
                {
                    value: 'Action',
                    url: ""
                },
                {
                    value: 'Adventure',
                    url: ""
                },
                {
                    value: 'RPG',
                    url: ""
                },
                {
                    value: 'Strategy',
                    url: ""
                },
                {
                    value: 'Simulation',
                    url: ""
                },
                {
                    value: 'Sports',
                    url: ""
                },
                {
                    value: 'Horrors',
                    url: ""
                },
                {
                    value: 'Survivals',
                    url: ""
                },
                {
                    value: 'MMO',
                    url: ""
                },
            ]}
        }
    }

</script>

<style lang="scss" scoped>
    $primary-color: rgb(34, 36, 36);

    main{
        width: 100%;
        margin-top: 10px;
        margin-left: 10px;
        display: flex;
        gap: 10px;

        nav{
            width: 20%;
            background-color: $primary-color;
            
            h2{
                padding: 10px;
                text-align: center;
            }
            .category{
                padding: 10px;
                &:hover {
                    opacity: 0.9;
                    border-left: 7px solid black;
                }
                img{
                    width: 30px; 
                    height: 30px;
                }
            }
        }

        aside{
            background-color: $primary-color;
            width: 100%;
            margin-right: 20px;
            text-align: center;
            padding: 10px;

            #blocks{
                width: 100%;
                display: flex;
                padding: 20px;
                
                #wrap{
                    display: flex;
                    gap: 25px 33px;
                    width: 100%;
                    flex-wrap: wrap;
                    justify-content: space-around;
                    
                    .block{
                        position: relative;
                        height: 300px;
                        width: 350px;
                        opacity: 0.9;
                        cursor: pointer;

                        .description{
                            position: absolute;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            min-height: 70px;
                            background-color: rgb(20, 24, 24, 0.7);
                            font-weight: 600;
                            font-size: 16.5px;
                            width: 100%;
                            padding: 15px;                        
                            bottom: 0px;
                        }

                        &:hover{
                            opacity: 1;
                        }

                        &:hover .description{
                            background-color: rgb(20, 24, 24, 0.8);
                        }
                        

                        img{
                            height: inherit;
                            width: inherit;
                        }
                    }
                }
            }
        }
    }

@media only screen and (min-width: 2380px){
    main{
        aside{
            #blocks{
                #wrap{  
                    gap: 25px 200px;
                }
            }
        }
    }
}

@media only screen and (max-width: 1919px){
    main{
        aside{
            #blocks{
                #wrap{
                    gap: 25px 150px;
                    .block:nth-child(-n + 2){
                        display: none;
                    }
                }
            }
        }
    }
}

@media only screen and (max-width: 1540px){
    main{
        aside{
            #blocks{
                #wrap{
                    gap: 25px 100px;
                    .block:nth-child(-n + 2){
                        display: none;
                    }
                }
            }
        }
    }
}

@media only screen and (max-width: 1420px){
    main{
        aside{
            #blocks{
                #wrap{    
                    gap: 25px 100px;
                    .block:nth-child(-n + 4){
                        display: none;
                    }
                }
            }
        }
    }
}

@media only screen and (max-width: 1060px){
    main{
        flex-direction: column;
        margin: 0;
        
        nav{            
            display: none;
        }

        aside{
            margin-top: 10px;
            flex-direction: column;
            
            #blocks{
                #wrap{
                    gap: 25px 100px;
                }
                #leftBlock{
                    height: 650px;
                }
            }
        }
    }

}

@media only screen and (max-width: 860px){
    main{
        aside{
            #blocks{
                #wrap{  
                    gap: 25px 105px;
                    .block{
                        width: 300px;
                        height: 300px;

                        .description{
                            font-size: 14px;
                            padding: 5px;
                        }
                    }
                }
            }
        }
    }
}

@media only screen and (max-width: 765px){
    main{
        aside{
            #blocks{
                #wrap{  
                    .block{
                        width: 250px;
                        height: 250px;
                    }
                }
            }
        }
    }
}

@media only screen and (max-width: 665px){
    main{
        aside{
            #blocks{
                #wrap{  
                    .block{
                        width: 200px;
                        height: 200px;
                    }
                }
            }
        }
    }
}

@media only screen and (max-width: 580px){
    main{
        aside{
            #blocks{
                #wrap{
                    gap: 25px 100px;
                    .block{
                        width: 170px;
                        height: 170px;
                        .description{
                            min-height: 50px;
                            font-size: 12px;
                            padding: 5px;
                        }
                    }

                }
            }
        }
    }
}


@media only screen and (max-width: 500px) {
    main{
        width: 500px;
    }
}
</style>
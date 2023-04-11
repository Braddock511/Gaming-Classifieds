<template>
    <main>
        <div class="slider">
            <div class="slides-container">
                <div class="slide" v-for="(slide, index) in slides" :key="index" :class="{ active: index === activeIndex }">
                    <img :src="slide.url" alt="baner">
                </div>
            </div>
            <button class="prev-button" @click="prevSlide">&#10094;</button>
            <button class="next-button" @click="nextSlide">&#10095;</button>
        </div>
    </main>
</template>

<script>
    export default {
        data() {
            return {
            slides: [
                {name: "red dead redemption 2", url: 'https://ik.imagekit.io/ztf601lz0/the-last-of-us-part-i_2_.jpg?updatedAt=1680799768527.png'},
                {name: "the last of us 1", url: 'https://ik.imagekit.io/ztf601lz0/the-last-of-us-part-i.jpg?updatedAt=1680799461863.png'},
                {name: "witcher 3", url: 'https://ik.imagekit.io/ztf601lz0/thumb-1920-587508.png?updatedAt=1680799975927.png'},
                {name: "cyberpunk 2077", url: 'https://ik.imagekit.io/ztf601lz0/ded2bdf1df65f09413823cd15d0ca6b2.jpg?updatedAt=1680799887358.png'}
            ],
            activeIndex: 0
            }
        },

        methods: {
            nextSlide() {
                this.activeIndex = (this.activeIndex + 1) % this.slides.length;
                clearInterval(this.changeSlide)
                this.changeSlide = setInterval(this.autoChangeSlide, 5000);
            },

            prevSlide() {
                this.activeIndex = (this.activeIndex + this.slides.length - 1) % this.slides.length;
                clearInterval(this.changeSlide)
                this.changeSlide = setInterval(this.autoChangeSlide, 5000);
            },

            autoChangeSlide() {
                this.nextSlide();
            }
        },

        mounted() {
            this.changeSlide = setInterval(this.autoChangeSlide, 5000);
        }
    }
</script>

<style lang="scss" scoped>
    main{
        margin: 10px 0px 0px 0px;

        .slider {
            position: relative;
            .slides-container {
                position: relative;
                height: 700px;
                .slide {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    opacity: 0;
                    transition: opacity 0.5s ease-in-out;
                    &.active {
                        opacity: 1;
                    }
                    img {
                        width: 100%;
                        height: 100%;
                        object-fit: fill;
                        border-radius: 0;
                    }
                }
            }
            .prev-button, .next-button {
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                font-size: 2rem;
                background: none;
                border: none;
                color: white;
                cursor: pointer;
                z-index: 1;
            }
            .prev-button {
                left: 20px;
            }
            .next-button {
                right: 20px;
            }
        }
    }

@media (max-width: 1150px) {
    main{
        display: none;
    }
}
</style>

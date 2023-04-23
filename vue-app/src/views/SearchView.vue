<template>
    <TheHeader />
    <div id="container">
        <TheSorting/>
        <TheSearching/>
    </div>
    
</template>

<script>
    import TheHeader from '@/components/TheHeader.vue'
    import TheSorting from '@/components/TheSorting.vue'
    import TheSearching from '@/components/TheSearching.vue'

    export default{
        components:{
            TheHeader,
            TheSorting,
            TheSearching
        }
    }
</script>

<style lang="scss" scoped>
    #container{
            width: 100%;
            height: 100%;
            margin-top: 10px;
            margin-left: 10px;
            display: flex;
            gap: 10px;
        }
</style>
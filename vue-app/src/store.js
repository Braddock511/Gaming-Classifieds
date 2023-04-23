import { createStore } from 'vuex'
import axios from 'axios'

const store = createStore({
    state: {
      id: '',
      games:  await axios.get('http://127.0.0.1:8000/get-games').then(response => {return response.data.output}),
      searchQuery: '',
      cart: []
    },
    getters: {
      filteredGamesBySearch: (state) => (searchQuery) => {
        return state.games.filter(item => {
          return item.title.toLowerCase().includes(searchQuery.toLowerCase())
        })
      }
    }
  })

export default store;
/**
 * Componente para barra de busca de operadoras
 */
const SearchBar = {
    template: `
      <div class="card mb-4">
        <div class="card-body">
          <div class="row">
            <div class="col-md-8">
              <div class="input-group mb-3">
                <input 
                  type="text" 
                  class="form-control" 
                  placeholder="Digite sua busca aqui..." 
                  :value="searchQuery"
                  @input="$emit('update:searchQuery', $event.target.value)"
                  @keyup.enter="$emit('search')"
                >
                <button 
                  class="btn btn-primary" 
                  @click="$emit('search')" 
                  :disabled="isLoading"
                >
                  <span v-if="isLoading">Buscando...</span>
                  <span v-else>Buscar</span>
                </button>
              </div>
            </div>
            <div class="col-md-4">
              <select 
                class="form-select" 
                :value="limit"
                @change="$emit('update:limit', $event.target.value)"
              >
                <option value="10">10 resultados</option>
                <option value="25">25 resultados</option>
                <option value="50">50 resultados</option>
                <option value="100">100 resultados</option>
              </select>
            </div>
          </div>
        </div>
      </div>
    `,
    props: {
      searchQuery: {
        type: String,
        default: ''
      },
      limit: {
        type: [Number, String],
        default: 25
      },
      isLoading: {
        type: Boolean,
        default: false
      }
    },
    emits: ['search', 'update:searchQuery', 'update:limit']
  };
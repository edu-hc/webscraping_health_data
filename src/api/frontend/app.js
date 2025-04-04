/**
 * Aplicação principal
 */
const { createApp, ref } = Vue;

createApp({
  components: {
    SearchBar,
    OperadorasTable
  },
  setup() {
    // Estado da aplicação
    const searchQuery = ref('');
    const results = ref([]);
    const isLoading = ref(false);
    const hasSearched = ref(false);
    const limit = ref(25);
    
    /**
     * Função para realizar a busca de operadoras
     */
    const searchOperadoras = async () => {
      if (!searchQuery.value.trim()) {
        alert('Por favor, digite um termo para busca.');
        return;
      }
      
      isLoading.value = true;
      hasSearched.value = true;
      
      try {
        const response = await apiService.searchOperadoras(searchQuery.value, limit.value);
        // Utilizando o serviço de API
        console.log('Resultados recebidos:', response); // Log para depuração

        results.value = response;
      } catch (error) {
        console.error('Erro ao buscar operadoras:', error);
        alert('Ocorreu um erro ao buscar operadoras. Verifique o console para mais detalhes.');
        results.value = [];
      } finally {
        isLoading.value = false;
      }
    };
    
    return {
      searchQuery,
      results,
      isLoading,
      hasSearched,
      limit,
      searchOperadoras
    };
  }
}).mount('#app');
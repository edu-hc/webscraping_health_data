/**
 * Serviço para comunicação com a API de operadoras
 */
const apiService = {
    // URL base da API
    baseURL: 'http://localhost:5000/api/operadoras',
    
    /**
     * Busca operadoras com base em um termo de busca
     * @param {string} query - Termo de busca
     * @param {number} limit - Limite de resultados a retornar
     * @returns {Promise} Promise com os resultados da busca
     */
    searchOperadoras(query, limit) {
      return axios.get(this.baseURL, {
        params: {
          q: query,
          limit: limit
        }
      }).then(response => {
        return response.data.results;
      });
    }
  };
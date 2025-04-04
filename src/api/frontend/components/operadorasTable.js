/**
 * Componente para exibição da tabela de operadoras
 */
const OperadorasTable = {
    template: `
      <div class="card" :class="{ loading: isLoading }">
        <div class="card-body">
          <div v-if="hasSearched">
            <div v-if="results.length > 0" class="result-count">
              {{ results.length }} operadora(s) encontrada(s)
            </div>
            <div v-else class="no-results mb-3">
              Nenhuma operadora encontrada para esta busca.
            </div>
          </div>
  
          <div class="table-container" v-if="results.length > 0">
            <table class="table table-striped table-hover">
              <thead class="table-dark">
                <tr>
                  <th>Registro ANS</th>
                  <th>CNPJ</th>
                  <th>Razão Social</th>
                  <th>Nome Fantasia</th>
                  <th>Modalidade</th>
                  <th>Situação</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in results" :key="item.registro_ans">
                  <td>{{ item.registro_ans }}</td>
                  <td>{{ item.cnpj }}</td>
                  <td v-html="highlightText(item.razao_social)"></td>
                  <td v-html="highlightText(item.nome_fantasia)"></td>
                  <td>{{ item.modalidade }}</td>
                  <td>
                    <span :class="{'text-success': item.situacao === 'ATIVA', 'text-danger': item.situacao !== 'ATIVA'}">
                      {{ item.situacao }}
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    `,
    props: {
      results: {
        type: Array,
        default: () => []
      },
      isLoading: {
        type: Boolean,
        default: false
      },
      hasSearched: {
        type: Boolean,
        default: false
      },
      searchQuery: {
        type: String,
        default: ''
      }
    },
    methods: {
      /**
       * Destaca o termo de busca no texto
       * @param {string} text - Texto a ser destacado
       * @returns {string} Texto com destaque em HTML
       */
      highlightText(text) {
        if (!this.searchQuery.trim() || !text) return text;
        
        const regex = new RegExp(`(${this.searchQuery})`, 'gi');
        return text.replace(regex, '<span class="highlight">$1</span>');
      }
    }
  };
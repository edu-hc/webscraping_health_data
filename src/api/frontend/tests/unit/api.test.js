import axios from 'axios';
import apiService from '../../services/api.js'; // Importação padrão

jest.mock('axios'); // Mock do Axios

describe('apiService', () => {
  it('deve retornar os resultados da API', async () => {
    // Mock da resposta da API
    const mockResponse = {
      data: {
        results: [
          { registro_ans: 123, cnpj: '123456789', razao_social: 'Operadora A' },
          { registro_ans: 456, cnpj: '987654321', razao_social: 'Operadora B' },
        ],
      },
    };

    axios.get.mockResolvedValue(mockResponse); // Configura o mock para retornar a resposta simulada

    // Chama o metodo e verifica o resultado
    const results = await apiService.searchOperadoras('operadora', 10);
    expect(results).toEqual(mockResponse.data.results); // Verifica se os resultados estão corretos
    expect(axios.get).toHaveBeenCalledWith('http://localhost:5000/api/operadoras', {
      params: { q: 'operadora', limit: 10 },
    }); // Verifica se a chamada foi feita com os parâmetros corretos
  });

  it('deve lidar com erros da API', async () => {
    // Mock de erro
    axios.get.mockRejectedValue(new Error('Erro na API'));

    // Chama o metodo e verifica o erro
    await expect(apiService.searchOperadoras('operadora', 10)).rejects.toThrow('Erro na API');
  });
});

afterAll(() => {
  jest.clearAllMocks(); // Limpa todos os mocks após os testes
});
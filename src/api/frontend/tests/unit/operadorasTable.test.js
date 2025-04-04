import { mount } from '@vue/test-utils';
import OperadorasTable from '../../components/operadorasTable.js';

describe('OperadorasTable', () => {
  it('deve renderizar os resultados corretamente', () => {
    const results = [
      { registro_ans: 123, cnpj: '123456789', razao_social: 'Operadora A', situacao: 'ATIVA' },
      { registro_ans: 456, cnpj: '987654321', razao_social: 'Operadora B', situacao: 'INATIVA' },
    ];

    const wrapper = mount(OperadorasTable, {
      props: {
        results,
        isLoading: false,
        hasSearched: true,
        searchQuery: '',
      },
    });

    // Verifica se os resultados foram renderizados
    expect(wrapper.findAll('tbody tr').length).toBe(2);
    expect(wrapper.text()).toContain('Operadora A');
    expect(wrapper.text()).toContain('Operadora B');
  });

  it('deve exibir uma mensagem quando não houver resultados', () => {
    const wrapper = mount(OperadorasTable, {
      props: {
        results: [],
        isLoading: false,
        hasSearched: true,
        searchQuery: '',
      },
    });

    // Verifica se a mensagem de "Nenhuma operadora encontrada" é exibida
    expect(wrapper.text()).toContain('Nenhuma operadora encontrada para esta busca.');
  });
});

afterAll(() => {
  jest.clearAllMocks(); // Limpa todos os mocks após os testes
});
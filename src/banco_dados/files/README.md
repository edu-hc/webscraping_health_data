# README - Diretório de Arquivos de Consulta

## **Objetivo**
Este diretório contém os arquivos necessários para realizar consultas e análises nos dados das operadoras de planos de saúde. Para que os scripts funcionem corretamente, você precisará baixar manualmente os arquivos de consulta listados abaixo.

---

## **Arquivos Necessários**

### **1. Dados Cadastrais das Operadoras Ativas**
- **Descrição**: Arquivo CSV contendo informações cadastrais atualizadas das operadoras de planos de saúde ativas na ANS.
- **Fonte**: [https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)
- **Localização no Projeto**:  
  ```
  banco_dados/files/
  ```

### **2. Demonstrações Contábeis (Últimos 2 Anos)**
- **Descrição**: Arquivos contendo dados financeiros e contábeis das operadoras, incluindo despesas com eventos/sinistros.
- **Fonte**: [https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
- **Localização no Projeto**:  
  ```
  banco_dados/files/
  ```


---

## **Como Baixar os Arquivos**

1. **Dados Cadastrais (operadoras_ativas.csv)**:
   - Acesse o link da fonte.
   - Procure pelo arquivo mais recente no formato CSV.
   - Baixe-o e salve em `banco_dados/files`.

2. **Demonstrações Contábeis**:
   - Acesse o link da fonte.
   - Baixe os arquivos dos últimos 2 anos (ex.: `2023.zip`, `2022.zip`).
   - Extraia os arquivos e salve-os na pasta `banco_dados/files/`.

---

## **Observações Importantes**
- Certifique-se de que os arquivos estão no local correto antes de executar os scripts.
- Os nomes dos arquivos devem ser mantidos conforme especificado acima.
- Caso os links estejam indisponíveis, verifique no site da ANS por atualizações ou arquivos alternativos.

---

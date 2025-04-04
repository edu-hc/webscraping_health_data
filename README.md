# README - Projeto de Testes de Nivelamento ANS

## Visão Geral
Este projeto implementa uma solução completa para os testes de nivelamento da ANS, abrangendo:
- Web scraping de documentos públicos
- Transformação de dados de PDF para CSV
- Análise de banco de dados
- API RESTful com interface Vue.js

## Estrutura do Projeto

```
├── .gitignore
├── README.md
└── src
    ├── api
    │   ├── backend (API Python)
    │   └── frontend (Interface Vue.js)
    ├── banco_dados (Scripts SQL e dados)
    ├── instance (Banco de dados SQLite)
    ├── main.py (Execução principal)
    ├── transform_dados (Processamento de dados)
    └── web_scraping (Coleta de dados)
```

## Pré-requisitos

- Python 3.8+
- Node.js 14+ (para o frontend)
- PDFPlumber (para extração de PDF)
- SQLite/MySQL/PostgreSQL

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
```

2. Instale as dependências Python:
```bash
pip install -r src/api/backend/requirements.txt
```

3. Instale as dependências do frontend:
```bash
cd src/api/frontend
npm install
```

## Execução

### Processamento Principal (Exercícios 1 e 2)
```bash
python src/main.py
```

### API Backend
```bash
python src/api/backend/run.py
```

### Frontend
```bash
cd src/api/frontend
npm run serve
```

## Módulos Principais

### 1. Web Scraping
- `src/web_scraping/scraper.py`: Baixa os Anexos I e II do site da ANS
- `src/web_scraping/compact.py`: Compacta os arquivos em ZIP

### 2. Transformação de Dados
- `src/transform_dados/extract_tables.py`: Extrai tabelas de PDF usando pdfplumber
- `src/transform_dados/replace_abb.py`: Substitui abreviações por textos completos
- `src/transform_dados/save_csv_zip.py`: Salva dados em CSV e compacta

### 3. Banco de Dados
- `src/banco_dados/querries/`: Contém scripts SQL para:
  - Criação de tabelas
  - Importação de dados
  - Análises requisitadas

### 4. API
- Backend Python com:
  - Rotas RESTful (`operadora_routes.py`)
  - Serviços de busca (`operadora_service.py`)
  - Utilitários para CSV e sanitização
- Frontend Vue.js com:
  - Componentes de tabela e busca
  - Testes unitários

## Configuração

Edite `src/api/backend/config.py` para:
- Definir caminhos de arquivos
- Configurar parâmetros da API
- Ajustar conexões de banco de dados

## Testes

Testes do frontend:
```bash
cd src/api/frontend
npm test
```

## Dados de Exemplo

Os arquivos necessários podem ser baixados em:
- [Dados Abertos ANS](https://dadosabertos.ans.gov.br)
- [Rol de Procedimentos](https://www.gov.br/ans/pt-br)

Coloque os arquivos baixados em:
- `src/banco_dados/files/` para dados contábeis
- `src/web_scraping/downloads` para os Anexos PDF

## Contribuição

1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
# 🏥 Projeto de Extração e Análise de Dados da ANS

Extrai, transforma e analisa dados do Rol de Procedimentos e Eventos em Saúde da Agência Nacional de Saúde Suplementar (ANS).

## 📋 Descrição

Este projeto automatiza a coleta e processamento de:
- Tabelas de procedimentos de saúde (Anexos I e II em PDF)
- Dados cadastrais de operadoras (CSV)
- Demonstrações contábeis (arquivos FTP)

## ⚙️ Funcionalidades

- **Web Scraping**: Download automático de PDFs e CSVs
- **ETL**: Extração de tabelas de PDFs para DataFrames
- **Limpeza de Dados**: Padronização de colunas e valores
- **Análise**: Queries SQL para responder perguntas estratégicas

## 🛠️ Tecnologias

- Python 3.10+
- Bibliotecas:
  - `pdfplumber` (extração de PDFs)
  - `pandas` (processamento de dados)
  - `requests` (download de arquivos)
- Banco de Dados:
  - PostgreSQL e MySQL
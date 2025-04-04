-- Script 3.3. Criação das tabelas necessárias
-- PostgreSQL 10.0+

-- Tabela para armazenar os dados cadastrais das operadoras
CREATE TABLE IF NOT EXISTS operadoras (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(100),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    data_registro_ans DATE
);

-- Tabela para armazenar as demonstrações contábeis
CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20),
    data_ano INTEGER,
    data_trimestre INTEGER,
    conta VARCHAR(50),
    descricao TEXT,
    valor_final DECIMAL(20,2),
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);
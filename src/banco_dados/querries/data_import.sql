-- Script 3.4. Importação dos dados
-- PostgreSQL 10.0+

-- Importação dos dados das operadoras
-- Criar tabela temporária para importação sem restrições de chaves estrangeiras
CREATE TEMP TABLE temp_operadoras (
    registro_ans VARCHAR(20),
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
    data_registro_text VARCHAR(10)
);

-- Importar dados das operadoras (ajuste o caminho do arquivo)
COPY temp_operadoras FROM '/caminho/para/operadoras_ativas.csv'
WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'latin1');

-- Inserir na tabela final com conversão de data
INSERT INTO operadoras
SELECT
    registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
    logradouro, numero, complemento, bairro, cidade, uf, cep,
    ddd, telefone, fax, email, representante, cargo_representante,
    TO_DATE(data_registro_text, 'DD/MM/YYYY')
FROM temp_operadoras;

-- Limpar tabela temporária
DROP TABLE temp_operadoras;

-- Importação das demonstrações contábeis
-- Criar tabela temporária para importação das demonstrações contábeis
CREATE TEMP TABLE temp_demonstracoes (
    registro_ans VARCHAR(20),
    conta VARCHAR(50),
    descricao TEXT,
    valor_text VARCHAR(30)
);

-- Exemplo de importação para um arquivo trimestral específico (2023_1T)
COPY temp_demonstracoes FROM '/caminho/para/2023_1T_arquivo.csv'
WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'latin1');

-- Inserir na tabela final com conversão de valores
INSERT INTO demonstracoes_contabeis (registro_ans, data_ano, data_trimestre, conta, descricao, valor_final)
SELECT
    registro_ans,
    2023, -- Ajustar para o ano correto do arquivo
    1,    -- Ajustar para o trimestre correto do arquivo
    conta,
    descricao,
    CAST(REPLACE(REPLACE(valor_text, '.', ''), ',', '.') AS DECIMAL(20,2))
FROM temp_demonstracoes;

-- Limpar tabela temporária
DROP TABLE temp_demonstracoes;

-- Repita os comandos acima (CREATE TEMP TABLE, COPY, INSERT, DROP) para cada arquivo trimestral,
-- ajustando o caminho do arquivo e os valores de data_ano e data_trimestre
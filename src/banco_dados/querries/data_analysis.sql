-- Script 3.5. Análise dos dados
-- PostgreSQL 10.0+

-- Top 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS
-- DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre
WITH UltimoTrimestre AS (
    SELECT MAX(data_ano) as ano, MAX(data_trimestre) as trimestre
    FROM demonstracoes_contabeis
    WHERE data_ano = (SELECT MAX(data_ano) FROM demonstracoes_contabeis)
)
SELECT
    o.razao_social,
    o.registro_ans,
    o.modalidade,
    dc.descricao,
    SUM(dc.valor_final) as valor_total
FROM
    demonstracoes_contabeis dc
JOIN
    operadoras o ON dc.registro_ans = o.registro_ans
JOIN
    UltimoTrimestre ut ON dc.data_ano = ut.ano AND dc.data_trimestre = ut.trimestre
WHERE
    dc.descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
GROUP BY
    o.razao_social, o.registro_ans, o.modalidade, dc.descricao
ORDER BY
    valor_total DESC
LIMIT 10;

-- Top 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS
-- DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano
WITH UltimoAno AS (
    SELECT MAX(data_ano) as ano
    FROM demonstracoes_contabeis
)
SELECT
    o.razao_social,
    o.registro_ans,
    o.modalidade,
    SUM(dc.valor_final) as valor_total
FROM
    demonstracoes_contabeis dc
JOIN
    operadoras o ON dc.registro_ans = o.registro_ans
WHERE
    dc.data_ano = (SELECT ano FROM UltimoAno) AND
    dc.descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
GROUP BY
    o.razao_social, o.registro_ans, o.modalidade
ORDER BY
    valor_total DESC
LIMIT 10;

-- Para exportar os resultados para CSV
-- COPY (SELECT ...) TO '/caminho/para/resultado_trimestre.csv' WITH CSV HEADER DELIMITER ';';
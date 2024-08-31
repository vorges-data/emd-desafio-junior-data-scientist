--1. Quantos chamados foram abertos no dia 01/04/2023?
SELECT 
    COUNT(*) AS total_chamados 
FROM `datario.adm_central_atendimento_1746.chamado` 
WHERE date(data_inicio) = '2023-04-01';


--2. Qual o tipo de chamado que teve mais teve chamados abertos no dia 01/04/2023?
SELECT 
    tipo_situacao, 
    COUNT(*) AS total_chamados
FROM `datario.adm_central_atendimento_1746.chamado` 
WHERE date(data_inicio) = '2023-04-01'
GROUP BY tipo_situacao
ORDER BY total_chamados DESC
LIMIT 1;

--3. Quais os nomes dos 3 bairros que mais tiveram chamados abertos nesse dia?
SELECT 
  b.nome AS bairro, 
  COUNT(id_chamado) AS total_chamados
FROM `datario.adm_central_atendimento_1746.chamado` c
JOIN `datario.dados_mestres.bairro` b ON c.id_bairro = b.id_bairro
WHERE DATE(c.data_inicio) = '2023-04-01'
GROUP BY b.nome
ORDER BY total_chamados DESC
LIMIT 03;

--4. Qual o nome da subprefeitura com mais chamados abertos nesse dia?
SELECT 
  b.subprefeitura,
  COUNT(c.id_chamado) AS total_chamados
FROM `datario.adm_central_atendimento_1746.chamado` c
JOIN `datario.dados_mestres.bairro` b ON c.id_bairro = b.id_bairro
WHERE DATE(data_inicio) = '2023-04-01'
GROUP BY b.subprefeitura
ORDER BY total_chamados DESC
LIMIT 01;

--5. Existe algum chamado aberto nesse dia que não foi associado a um bairro ou subprefeitura na tabela de bairros? Se sim, por que isso acontece?
SELECT
    COUNT(c.id_chamado) AS chamados_sem_associacao
FROM `datario.adm_central_atendimento_1746.chamado` c
LEFT JOIN `datario.dados_mestres.bairro` b ON c.id_bairro = b.id_bairro
WHERE DATE(data_inicio) = '2023-04-01'
AND (b.id_bairro IS NULL OR b.subprefeitura IS NULL);

--Sim, ocorre pois há alguns IDs do chamado sem associação com Bairro e Subprefeitura, neste caso, foram 73 IDs identificados sem associação.
--Podemos pegar esses IDs e fazer uma verificação de correção.
SELECT
    c.id_chamado,
    c.id_bairro,
    b.nome,
    b.subprefeitura
FROM `datario.adm_central_atendimento_1746.chamado` c
LEFT JOIN `datario.dados_mestres.bairro` b ON c.id_bairro = b.id_bairro
WHERE DATE(data_inicio) = '2023-04-01'
AND (b.id_bairro IS NULL OR b.subprefeitura IS NULL);

--6. Quantos chamados com o subtipo "Perturbação do sossego" foram abertos desde 01/01/2022 até 31/12/2023 (incluindo extremidades)?
SELECT
   COUNT(id_chamado) AS total_chamados
FROM `datario.adm_central_atendimento_1746.chamado`
WHERE subtipo = 'Perturbação do sossego'
AND DATE(data_inicio) BETWEEN '2022-01-01' AND '2023-12-31';


--7. Selecione os chamados com esse subtipo que foram abertos durante os eventos contidos na tabela de eventos (Reveillon, Carnaval e Rock in Rio).
SELECT
  c.*
FROM `datario.adm_central_atendimento_1746.chamado` c
JOIN `datario.turismo_fluxo_visitantes.rede_hoteleira_ocupacao_eventos` o 
  ON DATE(c.data_inicio) BETWEEN DATE(o.data_inicial) AND DATE(o.data_final)
WHERE subtipo = 'Perturbação do sossego';
-- Como a tabela de Eventos só possui esses três eventos não preciso especificar na query, mas caso houvesse outros eventos eu adicionaria este filtro.
-- Join entre as tabelas para considerar qualquer chamado que ocorreu durante o evento (independente de ser início, no meio ou no final do evento)


--8. Quantos chamados desse subtipo foram abertos em cada evento?
SELECT
  o.evento,
  COUNT(c.id_chamado) AS total_chamados
FROM `datario.adm_central_atendimento_1746.chamado` c
JOIN `datario.turismo_fluxo_visitantes.rede_hoteleira_ocupacao_eventos` o 
  ON DATE(c.data_inicio) BETWEEN DATE(o.data_inicial) AND DATE(o.data_final)
WHERE subtipo = 'Perturbação do sossego'
GROUP BY o.evento
ORDER BY total_chamados DESC;
-- Como a tabela de Eventos só possui esses três eventos não preciso especificar na query, mas caso houvesse outros eventos eu adicionaria este filtro.
-- Join entre as tabelas para considerar qualquer chamado que ocorreu durante o evento (independente de ser início, no meio ou no final do evento)


--9. Qual evento teve a maior média diária de chamados abertos desse subtipo?
WITH chamados_por_dia AS (
  SELECT 
    o.evento AS evento, 
    DATE(c.data_inicio) AS dia, 
    COUNT(c.id_chamado) AS total_chamados
  FROM `datario.adm_central_atendimento_1746.chamado` c
  JOIN `datario.turismo_fluxo_visitantes.rede_hoteleira_ocupacao_eventos` o 
    ON DATE(c.data_inicio) BETWEEN DATE(o.data_inicial) AND DATE(o.data_final)
  WHERE c.subtipo = 'Perturbação do sossego'
  GROUP BY o.evento, DATE(c.data_inicio)
  )

SELECT 
  evento,
  ROUND(AVG(total_chamados), 2) AS media_diaria
FROM chamados_por_dia
GROUP BY evento
ORDER BY media_diaria DESC
LIMIT 1;
--Para calcular a média diária, precisamos contar os chamados por dia para cada evento e depois calcular a média desses valores.


--10. Compare as médias diárias de chamados abertos desse subtipo durante os eventos específicos (Reveillon, Carnaval e Rock in Rio) e a média diária de chamados abertos desse subtipo considerando todo o período de 01/01/2022 até 31/12/2023.
WITH media_chamados_evento AS (
  SELECT 
    o.evento AS evento, 
    DATE(c.data_inicio) AS dia, 
    COUNT(c.id_chamado) AS total_chamados
  FROM `datario.adm_central_atendimento_1746.chamado` c
  JOIN `datario.turismo_fluxo_visitantes.rede_hoteleira_ocupacao_eventos` o 
    ON DATE(c.data_inicio) BETWEEN DATE(o.data_inicial) AND DATE(o.data_final)
  WHERE c.subtipo = 'Perturbação do sossego'
  GROUP BY o.evento, DATE(c.data_inicio)
  ),

media_chamados_periodo AS (
  SELECT 
    DATE(c.data_inicio) AS dia, 
    COUNT(c.id_chamado) AS total_chamados
  FROM `datario.adm_central_atendimento_1746.chamado` c
  WHERE c.subtipo = 'Perturbação do sossego'
  AND DATE(c.data_inicio) BETWEEN '2022-01-01' AND '2023-12-31'
  GROUP BY DATE(c.data_inicio)
)

SELECT 
  'Média durante os eventos' AS descricao,
  ROUND(AVG(mce.total_chamados), 2) AS media_diaria_evento
FROM media_chamados_evento mce

UNION ALL

SELECT 
  'Média geral do período' AS descricao,
  ROUND(AVG(mcp.total_chamados), 2) AS media_diaria_total
FROM media_chamados_periodo mcp;

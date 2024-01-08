# Desafio Análise Exploratória de Dados

> Atividade individual da disciplina de Análise Exploratória de dados do curso de pós-graduação em _Data Analytics_.

## Proposta

A distribuidora de vinhos **FIAPWine** decidiu expandir seus horizontes e agora está importando vinhos tintos e brancos portugueses, mais especificamente a marca "Vinho Verde", que fará sua carta de vinhos se tornar mais vasta aqui no Brasil.

Hoje, o Head de Dados da **FIAPWine** necessita de uma equipe de dados alinhada com o propósito de gerar _insights_ valiosos para análise da qualidade dos novos vinhos. Para isso, foi disponibilizada uma [base de dados](https://www.kaggle.com/datasets/rajyellow46/wine-quality?resource=download) sobre o vinho português do ano de 2009, cuja referência acadêmica se encontra no artigo de [Cortex et al.,2009](http://www3.dsi.uminho.pt/pcortez/wine5.pdf).

Você foi designado para fazer as análies nos vinhos tintos, então é necessário que você siga os seguintes passos:

1. Importe o dataset `winequality-red.csv` que pode ser baixado no seguinte link: [aqui](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv).
2. Utilize o Pandas para verificar a estrutura do dataset (número de linhas, colunas, tipos de dados das colunas, etc.).
3. Limpe o _dataset_, removendo linhas duplicadas e tratando valores faltantes.
4. Utilize o Matplotlib para visualizar as seguintes informações: </br>
  a. Distribuição da acidez volátil por qualidade do vinho.</br>
  b. Distribuição do teor alcoólico por qualidade do vinho.</br>
  c. Relação entre acidez volátil e teor alcoólico.</br>
  d. Relação entre teor alcoólico e qualidade do vinho.</br>
5. Analise os resultados e responda às seguintes perguntas:</br>
  a. Qual a acidez volátio média dos vinhos de qualidade elevada?</br>
  b. Qual a relação entre teor alcoólico e qualidade do vinho?</br>
  c. Há alguma relação entre acidez volátil e teor alcoólico?</br>
  d. Há alguma relação entre acidez volátil e qualidade do vinho?</br>
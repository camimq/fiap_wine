import pandas as pd
import matplotlib.pyplot as plt

# importa dataframe
wine_data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')

wine_data.head()

# verifica estrutura do dataset
wine_data.dtypes

# verifica distribuição dos dados no dataset
wine_data.describe()

# verifica informações do dataset
wine_data.info()

# verifica linhas duplicadas no dataset
wine_data[wine_data.duplicated()]

# deleta linhas duplicadas, preservando dataframe com a informação sem duplicatas
wine_data.drop_duplicates(keep='first', inplace=True)
wine_data.info()

# verifica dados faltantes
wine_data.isnull().sum()

# criação de gráficos
##  distribuição da acidez volátil por qualidade do vinho

### cria df com acidez volátil x qualidade 3

df_acidez_x_qualidade_3 = wine_data.loc[(wine_data['quality'])==3]
df_acidez_x_qualidade_3.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_3

#### cria o gráfico de distribuição
plt.hist(df_acidez_x_qualidade_3['volatile acidity'])
plt.xlabel('Acidez Volátil')
plt.ylabel('Contagem')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 3')
plt.show()

### cria df com acidez volátil x qualidade 4

df_acidez_x_qualidade_4 = wine_data.loc[(wine_data['quality'])==4]
df_acidez_x_qualidade_4.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_4

#### cria gráfico de distribuição
plt.hist(df_acidez_x_qualidade_4['volatile acidity'])
plt.xlabel('Acidez Volátil')
plt.ylabel('Contagem')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 4')
plt.show()

### cria df com acidez volátil x qualidade 5

df_acidez_x_qualidade_5 = wine_data.loc[(wine_data['quality'])==5]
df_acidez_x_qualidade_5.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_5

#### cria gráfico de distribuição
plt.hist(df_acidez_x_qualidade_5['volatile acidity'])
plt.xlabel('Acidez Volátil')
plt.ylabel('Contagem')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 5')
plt.show()

### cria df com acidez volátil x qualidade 6

df_acidez_x_qualidade_6 = wine_data.loc[(wine_data['quality'])==6]
df_acidez_x_qualidade_6.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_6

#### cria gráfico de distribuição
plt.hist(df_acidez_x_qualidade_6['volatile acidity'])
plt.xlabel('Acidez Volátil')
plt.ylabel('Contagem')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 6')
plt.show()

### cria df com acidez volátil x qualidade 7

df_acidez_x_qualidade_7 = wine_data.loc[(wine_data['quality'])==7]
df_acidez_x_qualidade_7.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_7

#### cria gráfico de distribuição
plt.hist(df_acidez_x_qualidade_7['volatile acidity'])
plt.xlabel('Acidez Volátil')
plt.ylabel('Contagem')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 7')
plt.show()

### cria df com acidez volátil x qualidade 8

df_acidez_x_qualidade_8 = wine_data.loc[(wine_data['quality'])==8]
df_acidez_x_qualidade_8.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_8

#### cria gráfico de distribuição
plt.hist(df_acidez_x_qualidade_8['volatile acidity'])
plt.xlabel('Acidez Volátil')
plt.ylabel('Contagem')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 8')
plt.show()

# calcula acidez volátil média entre os vinhos de qualida >= 8
wine_data[wine_data['quality'] >= 8]['volatile acidity'].mean()

##  Distribuição do teor alcoólico por qualidade do vinho

### cria df com teor alcoólico x qualidade 3
df_teor_x_qualidade_3 = wine_data.loc[(wine_data['quality'])==3]
df_teor_x_qualidade_3.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_3

#### cria gráfico de distribuição
plt.hist(df_teor_x_qualidade_3['alcohol'])
plt.xlabel('Teor Alcoólico')
plt.ylabel('Contagem')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 3')
plt.show()

### cria df com teor alcoólico x qualidade 4
df_teor_x_qualidade_4 = wine_data.loc[(wine_data['quality'])==4]
df_teor_x_qualidade_4.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_4

#### cria gráfico de distribuição
plt.hist(df_teor_x_qualidade_4['alcohol'])
plt.xlabel('Teor Alcoólico')
plt.ylabel('Contagem')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 4')
plt.show()

### cria df com teor alcoólico x qualidade 5
df_teor_x_qualidade_5 = wine_data.loc[(wine_data['quality'])==5]
df_teor_x_qualidade_5.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_5

#### cria gráfico de distribuição
plt.hist(df_teor_x_qualidade_5['alcohol'])
plt.xlabel('Teor Alcoólico')
plt.ylabel('Contagem')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 5')
plt.show()

### cria df com teor alcoólico x qualidade 6
df_teor_x_qualidade_6 = wine_data.loc[(wine_data['quality'])==6]
df_teor_x_qualidade_6.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_6

#### cria gráfico de distribuição
plt.hist(df_teor_x_qualidade_6['alcohol'])
plt.xlabel('Teor Alcoólico')
plt.ylabel('Contagem')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 6')
plt.show()

### cria df com teor alcoólico x qualidade 7
df_teor_x_qualidade_7 = wine_data.loc[(wine_data['quality'])==7]
df_teor_x_qualidade_7.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_7

#### cria gráfico de distribuição
plt.hist(df_teor_x_qualidade_7['alcohol'])
plt.xlabel('Teor Alcoólico')
plt.ylabel('Contagem')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 7')
plt.show()

### cria df com teor alcoólico x qualidade 8
df_teor_x_qualidade_8 = wine_data.loc[(wine_data['quality'])==8]
df_teor_x_qualidade_8.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_8

#### cria gráfico de distribuição
plt.hist(df_teor_x_qualidade_8['alcohol'])
plt.xlabel('Teor Alcoólico')
plt.ylabel('Contagem')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 8')
plt.show()

# visualiza relação entre acidez volátil e teor alcoólico
plt.scatter(wine_data['volatile acidity'], wine_data['alcohol'])
plt.title('Relação Acidez Volátil x Teor Alcoólico')
plt.xlabel('Acidez Volátil')
plt.ylabel('Teor Alcoólico')
plt.show()

# visualiza relação entre teor alcoólico e qualidade do vinho
plt.scatter(wine_data['alcohol'], wine_data['quality'])
plt.title('Relação Teor Alcoólico x Qualidade do vinho')
plt.xlabel('Teor Alcoólico')
plt.ylabel('Qualidade')
plt.show()
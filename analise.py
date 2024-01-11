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

# distribuição da acidez volátil por qualidade do vinho
plt.bar(wine_data['quality'], wine_data['volatile acidity'])
plt.xlabel('Qualidade')
plt.ylabel('Acidez Volátil')
plt.title('Acidez Volátil por Qualidade')
plt.show()

# calcula acidez volátil média entre os vinhos de qualida >= 8
wine_data[wine_data['quality'] >= 8]['volatile acidity'].mean()

# distribuição do teor alcoólico por qualidade do vinho
plt.bar(wine_data['quality'], wine_data['alcohol'])
plt.xlabel('Qualidade')
plt.ylabel('Teor Alcoólico')
plt.title('Teor Alcoólico por Qualidade')
plt.show()

# visualiza distribuição entre acidez volátil e teor alcoólico
plt.scatter(wine_data['volatile acidity'], wine_data['alcohol'])
plt.title('Distribuição Acidez Volátil x Teor Alcoólico')
plt.xlabel('Acidez Volátil')
plt.ylabel('Teor Alcoólico')
plt.show()

# visualiza distribuição entre teor alcoólico e qualidade do vinho
plt.scatter(wine_data['alcohol'], wine_data['quality'])
plt.title('Distribuição Teor Alcoólico x Qualidade do vinho')
plt.xlabel('Teor Alcoólico')
plt.ylabel('Qualidade')
plt.show()
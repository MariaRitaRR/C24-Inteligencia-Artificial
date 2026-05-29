import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

houses = pd.read_csv('kc_house_data.csv')
demographics = pd.read_csv('zipcode_demographics.csv')
future = pd.read_csv('future_unseen_examples.csv')

houses_full = houses.merge(demographics, on='zipcode', how='left')
future_full = future.merge(demographics, on='zipcode', how='left')

full_data = pd.concat([houses_full, future_full], ignore_index=True)

#Informações sobre o dataset
print(full_data.head())
print(full_data.info())
print(full_data.isnull().sum())
print(full_data.duplicated().sum())
print(full_data.describe())


# Correlação apenas das variáveis numéricas
corr = full_data.corr(numeric_only=True)

# Correlação com o preço
price_corr = corr['price'].sort_values(ascending=False)

print(price_corr)

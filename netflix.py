import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("netflix_titles.csv")
#1
sns.set_style("whitegrid")
plt.figure(figsize = (8, 5))
sns.countplot(data = df, x = 'type', palette = 'viridis')
plt.title("Filmes X Séries")
plt.xlabel("Tipo de Conteúdo")
plt.ylabel("Quantidade Total")
plt.tight_layout()
plt.show()

#1
limpeza_paises = df['country'].dropna().str.split(',').explode().str.strip()
top_paises = limpeza_paises.value_counts().head(10)

sns.set_style("whitegrid")
plt.figure(figsize = (12, 8))
sns.barplot(x =top_paises.values, y = top_paises.index, palette = 'viridis')
plt.title("Top 10 Países Produtores de Conteúdo na Netflix")
plt.xlabel("Quantidade de Títulos")
plt.ylabel("País")
plt.tight_layout()
plt.show()

#2
lancamentos_por_ano = df['release_year'].value_counts().sort_index()
sns.set_style("whitegrid")
plt.figure(figsize = (12, 5))
sns.lineplot(x = lancamentos_por_ano.index, y = lancamentos_por_ano.values)
plt.xlabel("Ano")
plt.ylabel("Lançamentos")
plt.tight_layout()
plt.show()

#2
filmes = df[df['type'] == 'Movie'].copy()
filmes['duration_int'] = filmes['duration'].str.replace(' min', '')
filmes.dropna(subset = ['duration_int'], inplace = True)
filmes['duration_int'] = filmes['duration_int'].astype(int)

plt.figure(figsize = (12, 5))
sns.histplot(data = filmes, x = 'duration_int', bins = 40, kde = True)
plt.title("Distribuição da Duração dos Filmes")
plt.xlabel("Duração (Minutos)")
plt.ylabel("Contagem de filmes")
plt.tight_layout()
plt.show()

#3
generos_limpos = df['listed_in'].dropna().str.split(',').explode().str.strip()
generos = generos_limpos.value_counts().head(15)
sns.set_style("whitegrid")
plt.figure(figsize = (12, 5))
sns.barplot(x = generos.values, y = generos.index, palette = 'viridis')
plt.title("15 Gêneros mais comuns")
plt.xlabel("Quantidade")
plt.ylabel("Gêneros")
plt.tight_layout()
plt.show()

#3
tv_show = df[df['type'] == 'TV Show'].copy()
tv_show['seasons_int'] = tv_show['duration'].str.replace(' Seasons', '').str.replace(' Season', '')
tv_show.dropna(subset = ['seasons_int'], inplace = True)
tv_show['seasons_int'] = tv_show['seasons_int'].astype(int)
contagem_temporada = tv_show['seasons_int'].value_counts().sort_index()
sns.set_style("whitegrid")
plt.figure(figsize = (12, 5))
sns.barplot(x = contagem_temporada.index, y = contagem_temporada.values, palette = 'viridis')
plt.title("Distribuição do Número de Temporadas das Séries")
plt.xlabel("Número de Temporadas")
plt.ylabel("Quantidade de Séries")
plt.tight_layout()
plt.show()

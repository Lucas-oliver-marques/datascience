import pandas as pd

uri_filmes = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv'
filmes = pd.read_csv(uri_filmes)

uri_notas = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv'
notas = pd.read_csv(uri_notas)

print("12 primeiros registros:")
print(filmes.head(12))
print("\n6 últimos registros:")
print(filmes.tail(6))

print("\nTamanho da massa de dados:")
print(filmes.shape)

nota_filme_32 = notas[(notas['movieId'] == 32) & (notas['rating'] > 3)]

if not nota_filme_32.empty:
    
    nome_filme = filmes[filmes['movieId'] == 32]['title'].values[0]
    print(f"O filme {nome_filme} é considerado bom, pois recebeu uma nota maior que 3.")
else:
    print("Não há dados disponíveis para o filme com ID=32 ou a nota não é maior que 3.")
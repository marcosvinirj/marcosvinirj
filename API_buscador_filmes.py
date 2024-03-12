#                         1º PASSO ==== OK!
# 1 -= Acessar site The Movie Database
# 2 -= Criar conta e registrar como desenvolvedor , obter chave API
#                         2º CONFIG. DO AMBIENTE === OK!
# 1 -= Instale o pacote "Request" para fazer requisições 
#                         3º CRIANDO O PROJETO === OK!
# 1 -= Criar arquivo .py e escrever o cód === ok!


#                         4º ESCREVENDO O CÓDIGO

# 1 -= importar o módulo request
import requests
# 2 -= Defina um função para fazer uma requisição á API da TMDb e buscar filmes com base em uma consulta
# do usuario.
def search_movies(query):
# 3 -= Parseie a resposta da API e exiba os detalhes dos filmes encontrado (gênero, tempo de duração, e se é para +18)
    api_key = "f2f4b24c648fa3fde02cb5fb1f6051ea"
    url = f"https://api.themoviedb.org/3/search/movie?api_key = {api_key}&query = {query}"
    response = requests.get(url)
    data = response.json()
    if 'results' in data:
        movies = data('results')
        for movie in movies:
         print(f"Titulo: {movie['title']}")
         print(f"Data de lançamento: {movie['release_date']}")
         print(f"Descrição: {movie['overview']}")
         print("")

#                         5º TESTANDO O PROJETO

# 1 -= Execute o Main.py e teste a busca de filmes digitando o nome de um filme quando solicitado.
def Main():
   query = input('Informe o nome do filme que procura: ')
   search_movies(query)
if __name__ == "__main__":
   Main()
#                         6º APERFEIÇOAMENTOS(OPCIONAIS)

# 1 -= Implemente uma interface de linha de comando mais amigável.
# 2 -= Adicione recursos como classificação, elenco, posteres de filme e etc...
# 3 -= Lidere com erros e exceções de forma robusta

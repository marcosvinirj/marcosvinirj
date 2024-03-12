import requests     # O módulo REQUESTS serve para fazer requizições em HTTP em Python
def obter_post():      # Uma função na qual podemos encapsular a lógica para obter e eibir post da API
    url = "https://jsonplaceholder.typicode.com/posts" # Atribui a URL a API JSONplaceholdr para obter# post a uma variável chamada 'url'
    try:
        response = requests.get(url) # Faz uma requiseção GET á API - O resultado é armazenado na variável 'response'

        if response.status_code == 200:    # Verificar se a requisição foi bem-sucedida(Cód. 200)
            posts = response.json()    # Converte o conteúdo da resp. para um formato JSON, 
                                       # Usando o método 'json()' , vamos armazenar o resultado em 'posts'
            for post in posts: 
                print(f'Titulo: {post["title"]}')
                print(f'Corpo: {post["body"]}')
                print('---')
        else:
            print(f"Erro na aquisição: {response.status_code}")
    except Exception as e: # Iniciamos um bloco 'Except' para lidar com as exceções e armazena na variável 'e'
        print(f"Erro: {e}")
obter_post() # Chama a função para obter e eibir os posts, para iniciar a execução do código.
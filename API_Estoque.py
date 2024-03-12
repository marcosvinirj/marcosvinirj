
# IMPLEMENTANDO FUNÇÕES PRA ATRIBUIR E REMOVER PRODUTOS, VERIFICAR O ESTOQUE.

def lin ():
    print('-=' * 30)

# adicionar produtos
def adicionar_produtos(estoque , produto , quantidade):
    if produto in estoque:
        print(f'O produto {produto} já existe em seu estoque! Utilize a função para atualizar a quantidade.')
    else:
        estoque[produto] = quantidade
        print(f'Produto {produto}, adicionado com sucesso!')
lin()
# teste função
estoque = {}
adicionar_produtos (estoque , 'Maçãs' , 100)
print(estoque)
lin()

# Verificar se ja tem em estoque o produto
def verificar_quantidade (estoque , produto):
    if produto in estoque:
        print(f'A quantidade disponível de {produto} no estoque é: {estoque[produto]}')
    else:
        print(f'O produto {produto} não se encontra no estoque.')
# teste verificação
verificar_quantidade(estoque , 'Maçãs')
verificar_quantidade(estoque , 'Banana')
lin()

# Atualizar a quantidade de produto
def atualizar_quantidade (estoque , produto , quantidade):
    if produto in estoque:
        estoque[produto] += quantidade
        print(f'A quantidade de {produto} no estoque foi atualizada para {estoque[produto]}')
    else:
        print(f'O produto {produto} não está no estoque. Não é possível atualiza-lo')
# teste função
atualizar_quantidade ( estoque , 'Maçãs' , 50)
atualizar_quantidade ( estoque, 'Banana' , 100)
lin()

# Remover produtos
def remover_produtos (estoque , produto):
    if produto in estoque:
      print(f'O produto {produto}, foi removido de seu estoque.')
    else:
        print(f'O produto {produto}, não se encontra em seu estoque. Não é possível removê-lo')
# teste função
remover_produtos (estoque , 'Maçãs')
remover_produtos (estoque , 'Banana')
lin()


# interagindo com uma API 
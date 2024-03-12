


# 1 -= Definição de Classes e Estruturas de Dados: Vamos criar classes para representar os principais elementos do sistema, como usuários, motoristas, carros, viagens, etc.
class User:                                              
    def __init__(self , nome , email , senha):       
        self.name = nome
        self.imail = email
        self.passwolrd = senha

class Driver(User):                                      # Nesta linha fizemos uma "Sub Class"  
    def __init__(self, nome, email, senha , carro):      # E essa "Sub Class" serve a Class User.
        super().__init__(nome, email, senha)
        self.car = carro
        self.available = True

class Rider:
    def __init__(self , passageiro , origem , destino):
        self.passageiro = passageiro
        self.origem = origem
        self.destino = destino

        
# 2 -= Implementação do Banco de Dados: Vamos usar um banco de dados para armazenar informações sobre usuários, viagens, etc. Podemos usar o SQLite para simplicidade, mas em um sistema real, poderíamos usar um banco de dados mais robusto como o MySQL ou PostgreSQL.

# 3 -= Gerenciamento de Usuários e Autenticação: Vamos criar funcionalidades para registrar novos usuários, fazer login e autenticar usuários.

# 4 -= Gerenciamento de Viagens: Vamos implementar a lógica para os usuários solicitarem viagens, motoristas aceitarem solicitações, calcular tarifas, etc.

# 5 -= Integração com Serviços de Mapa: Podemos usar APIs de mapas como o Google Maps para obter informações sobre rotas, distâncias, tempo


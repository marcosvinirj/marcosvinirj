#OK =  1 -= Coleta de dados - nome , idade ,  salário , renda extra , limete de cartão(Gastos tbm) e total de dívidas acumuladas.
# OK = 2 -= Calcular Operadores - salário, renda extra  e total de dívidas.
# OK = 3 -= Verificar - se o valor das dívidas são maiores do que seu salário e renda extra.
# 4 -= definindo limetes - Gastos e despesas em cima do calculo ,  10% = Lazer , 10% - Viagem , 
#30% = poupar(investir) , 50% = Contas fixas.



def investimento(salario , renda_extra):
	total = salario + renda_extra
	lazer = total * 0.10
	viagem = total * 0.10
	poupar = total * 0.30
	contas_fixas = total * 0.50
	return lazer , viagem , poupar , contas_fixas

from time import sleep 
def exibir_mensagem(menssagem):
	sleep(0.5)
	print('-'*40)
	print(f'{menssagem:^40}')
	print('-'*40)
	
	
def calculo_total(a , b):  
	return a + b

def main(nome, idade, salario, rendaExtra, limite_gasto, divida_extra):
	dados = {  'nome': '',
			'idade': '',
			'salário' : 0 ,
			'renda_extra' : 0,
			'limite_gasto': 0, 
			'divida_extra': 0
	}
	dados['nome'] =   nome
	dados['idade']=   idade
	dados['salário']= float(salario)
	#renda_extra = str(input('Renda Extra -  [S/N]: ')).upper()[0]
	#if renda_extra in 'Ss':
	dados['renda_extra'] = float(rendaExtra)
	return dados
	
	#resp = str(input('Limite do cartão - [S/N]: ')).upper()[0]
	#while True:
	#	if resp in 'S':
	#		limite_cartão = float(input('Quanto o seu cartão possui de limite: '))
	#		dados['limite_gasto'] = float(input('Quanto de limite gastos: '))
	##		print('Desculpe, digite somente [S/N].')
	#		resp = str(input('Possui limite no cartão - [S/N]: '))
	##		break

	#while True:
	#	dividas = str(input('Possui dívidas acumulada - [S/N]: ')).upper()[0]
	##		dados['divida_extra'] = float(input('Total de dívidas acumuladas: '))
	##	if dividas not in 'SN':
	#		print('Desculpe, digite somente [S/N]. ')
	#		dividas = str(input('Possui dívidas acumulada - [S/N]: '))
	##		break

	

















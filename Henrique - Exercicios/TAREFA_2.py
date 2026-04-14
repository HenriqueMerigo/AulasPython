# Tarefa 2: Classificador de Nadador (If, Elif, Else)
# Para praticar estruturas de decisão, o programa deve pedir a idade de um jovem e dizer em qual categoria de natação ele se encaixa:
# Infantil: de 5 a 10 anos.
# Juvenil: de 11 a 17 anos.
# Adulto: 18 anos ou mais.
# Dica: Se a idade for menor que 5, o programa deve dizer que ele ainda não pode competir.
# ================================================================================================================================================
import os # import utiliza uma biblioteca externa. Usamos "os" para limpar o terminal automaticamente sempre que rodamos o codigo 
os.system('cls') # Essa ferramenta limpa a tela sempre que for executada
idade = int(input("Digite a idade: ")) # Declaramos a variavel "idade" para receber o input do cliente, convertendo para inteiro para comparar com as faixas etárias das categorias de natação

if idade >= 5 and idade <= 10: # O if compara a variavel "idade" com as faixas etárias das categorias de natação e printa a categoria correspondente ou uma mensagem de erro caso a idade seja menor que 5
    print("Infantil")
elif idade >= 11 and idade <= 17: # O elif compara a variavel "idade" com as faixas etárias das categorias de natação e printa a categoria correspondente ou uma mensagem de erro caso a idade seja menor que 5
    print("Juvenil")
elif idade >= 18:
    print("Adulto")
else: # O else é executado caso a variavel "idade" seja menor que 5, printando a mensagem de erro para o cliente
    print("Atleta nao pode competir.")
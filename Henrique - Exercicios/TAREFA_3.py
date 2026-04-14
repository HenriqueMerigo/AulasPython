# Tarefa 3: O Menu do Quiosque (Match Case)
# Utilizando o match case, peça para o aluno criar um pequeno menu de um quiosque de praia. O usuário digita um número e o programa responde o que ele escolheu:
# 1: "Água de Coco - R$ 8,00"
# 2: "Suco de Laranja - R$ 10,00"
# 3: "Açaí na Tigela - R$ 15,00"
# Caso contrário (default): "Opção inválida! Escolha de 1 a 3."
# dica do merigo: antes de declarar a vartiavel do pedido, printa no terminal o codigo e o produto. Ex:
# 1 - Agua de coco
# 2 - etc…
# ================================================================================================================================================
import os # import utiliza uma biblioteca externa. Usamos "os" para limpar o terminal automaticamente sempre que rodamos o codigo 
os.system('cls') # Essa ferramenta limpa a tela sempre que for executada

produtos = {1: "Água de Coco - R$ 8,00", # Declaramoos um "Dicionário" para guardar os produtos e seus respectivos códigos e preços
            2: "Suco de Laranja - R$ 10,00",
            3: "Açaí na Tigela - R$ 15,00"}

print("Menu do Quiosque:") # Printamos o menu do quiosque para o cliente escolher
for codigo, produto in produtos.items(): # O for percorre o dicionário "produtos" e printa o código e o produto para o cliente escolher
    print(f"{codigo} - {produto}") # O print formata a string para mostrar o código e o produto de forma clara para o cliente

var = int(input("Digite o ID do produto que deseja: ")) # Declaramos a variavel "var" para receber o input do cliente, convertendo para inteiro para comparar com os códigos do dicionário

match var: # O match case compara a variavel "var" com os códigos do dicionário e printa o produto correspondente ou uma mensagem de erro caso o código seja inválido
    case 1:
        print(produtos[1]) # Para printarmos o id desejado buscamos o dicionario (produtos[n]) sendo n o numero do id do produto escolhido pelo cliente
    case 2:
        print(produtos[2])
    case 3:
        print(produtos[3])
    case _:
        print("Produto Inexistente")
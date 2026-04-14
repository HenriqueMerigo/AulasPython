# Tarefa 1: O Calculador de Descontos (Variáveis e Cálculos)

# Peça para o aluno criar um programa que ajude uma loja. O programa deve:

# 1 - Receber o nome de um produto.
# 2 - Receber o preço original do produto.
# 3 - Calcular um desconto de 15% sobre esse preço.
# 4 - Exibir uma frase como: "O produto [nome] custava R$ [preço] e com 15% de desconto passará a custar R$ [novo preço]".
# ================================================================================================================================================
import os # import utiliza uma biblioteca externa. Usamos "os" para limpar o terminal automaticamente sempre que rodamos o codigo 
os.system('cls') # Essa ferramenta limpa a tela sempre que for executada

produto = input("Digite o nome do Produto: ") # Declaramos a variavel produto para definir seu nome
preco = float(input("Digite o valor do produto (00.00): ")) # Declaramos o preco do produto em valor float para calcular os centavos se for o caso
desconto = 0.15 # Declaramos a porcentagem do desconto fixa 
calculo = preco * (1 - desconto) # O calculo faz a subtracao da porcentagem do valor do produto

print(f"O produto {produto} custava R$ {preco} e com 15% de desconto passará a custar R$ {calculo}") # Print final do exercicio
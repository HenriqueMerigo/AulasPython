# Tarefa 2: Classificador de Nadador (If, Elif, Else)
# Para praticar estruturas de decisão, o programa deve pedir a idade de um jovem e dizer em qual categoria de natação ele se encaixa:
# Infantil: de 5 a 10 anos.
# Juvenil: de 11 a 17 anos.
# Adulto: 18 anos ou mais.
# Dica: Se a idade for menor que 5, o programa deve dizer que ele ainda não pode competir.

idade = int(input("Digite a idade: "))

if idade >= 5 and idade <= 10:
    print("Infantil")
elif idade >= 11 and idade <= 17:
    print("Juvenil")
elif idade >= 18:
    print("Adulto")
else:
    print("Atleta nao pode competir.")
nome = input("Digite o seu nome: ")
media = float(input("Digite sua media: "))
faltas = int(input("Digite sua quantidade de faltas: "))

if media >= 7 and faltas <= 32:
    print(nome +", você foi aprovado com media maior que 7 e faltas menor ou igual a 32 faltas")
    
elif media < 7 and faltas <= 32:
    print(nome +", você foi reprovado com media menor que 7, mas faltas menor ou igual a 32 faltas")

elif media >= 7 and faltas > 32:
    print(nome +", você tem media maior que 7, mas reprovado por faltas maior que 32 faltas")
    
elif media < 7 and faltas > 32:
    print(nome +", reprovado por media menor que 7 e faltas maior que 32 faltas")
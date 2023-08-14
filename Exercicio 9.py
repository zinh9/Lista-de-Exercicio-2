print("Este programa calcula o valor idela de calorias para homens e mulheres")

sexo = input("Digite qual é o seu sexo: ")
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (cm): "))
idade = int(input("Digite a sua idade: "))

if sexo.lower() == "maculino":
    homem = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
    
    print("A quantidade de caloriais diarias recomendavel para você é de: " +str(homem) +" calorias")

elif sexo.lower() == "feminino":
    mulher = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
    
    print("A quatidade de calorias diarias recomendavel para você é de: " +str(mulher))
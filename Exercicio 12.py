print("Este programa verifica se você é maior de idade de acordo com seu sexo")

sexo = input("Digite o seu sexo: ")
idade = int(input("Digite sua idade: "))

if sexo == "masculino" and idade >= 21:
    print("Você é maior de idade")

elif sexo == "masculino" and idade < 21:
    print("Você é menor de idade")

elif sexo == "feminino" and idade >= 18:
    print("Você é maior de idade")

elif sexo == "feminino" and idade < 18:
    print("Você é menor de idade")
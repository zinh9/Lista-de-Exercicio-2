print("Este programa verifica qual é o maior numero digitado")

numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))
numero_3 = int(input("Digite o terceiro numero: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("O numero " +str(numero_1) +" é o maior")

elif numero_2 > numero_1 and numero_2 > numero_3:
    print("O numero " +str(numero_2) +" é o maior")
    
else:
    print("O numero " +str(numero_3) +" é o maior")
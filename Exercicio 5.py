print("Este programa verifica qual é o maior numero digitado")

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("O numero " +str(numero1) +" é o maior")

elif numero2 > numero1 and numero2 > numero3:
    print("O numero " +str(numero2) +" é o maior")
    
else:
    print("O numero " +str(numero3) +" é o maior")
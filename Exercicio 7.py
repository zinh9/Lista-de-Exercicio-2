angulo1 = int(input("Digite o primeiro ângulo: "))
angulo2 = int(input("Digite o segundo ângulo: "))
angulo3 = int(input("Digite o terceiro ângulo: "))

if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print("A figura é um acutângulo")

elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("A figura é um retângulo")
    
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("A figura é um obtusângulo")
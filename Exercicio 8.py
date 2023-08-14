print("Este programa calcula o consumo de gasolina de um carro")

distancia_percorrida = float(input("Digite a distancia percorrida: "))
consumo_gasolina = float(input("Digite o quanto o carro consumiu de gasolina: "))

consumo = distancia_percorrida / consumo_gasolina

if consumo < 8:
    print("VENDA O CARRO!")

elif consumo == 8 or consumo <= 14:
    print("ECONÔMICO!")

elif consumo > 12:
    print("SUPER ECONÔMICO!")
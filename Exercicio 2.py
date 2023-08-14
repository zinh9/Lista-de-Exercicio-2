print("Este programa calcula a velocidade média de dois carros e verifica qual teve maior velocidade")

dist_carro_1 = float(input("Digite a distancia percorrida do carro 1: "))
temp_carro_1 = int(input("Digite o tempo percorrido do carro 1: "))

dist_carro_2 = float(input("Digite a distancia percorrida do carro 2: "))
temp_carro_2 = int(input("Digite o tempo percorrido do carro 2: "))

vel_media_carro_1 = dist_carro_1 / temp_carro_1
vel_media_carro_2 = dist_carro_2 / temp_carro_2

if vel_media_carro_1 > vel_media_carro_2:
    print("O carro 1 tem maior velocidade que o carro 2  com " +str(vel_media_carro_1) +" m/s")
    
elif vel_media_carro_2 > vel_media_carro_1:
    print("O carro 2 tem maior velocidade que o carro 1 com " +str(vel_media_carro_2) +" m/s")
    
elif vel_media_carro_1 == vel_media_carro_2:
    print("O carro 1 e carro 2 tem a mesma velocidade, com " +str(vel_media_carro_1) +" m/s")
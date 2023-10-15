qt_esfera = 0
qt_limpeza = 0
qt_trocacabo = 0
qt_quebrado = 0
totalM = 0

while True:
    num_identificacao = int(input("Digite o número de identificação do mouse (ou 0 para encerrar): "))
    
    if num_identificacao == 0:
        break  #encerra no 0
    
    print("Opções para o tipo de defeito:")
    print("1 - necessita da esfera")
    print("2 - necessita de limpeza")
    print("3 - necessita troca do cabo ou conector")
    print("4 - quebrado ou inutilizado")
    
    while True:
        tipo_defeito = int(input("Digite o número correspondente ao tipo de defeito: "))
        if 1 <= tipo_defeito <= 4:
            break 
        else:
            print("erro Escolha um número de 1 a 4.")

    if tipo_defeito == 1:
        qt_esfera += 1
    elif tipo_defeito == 2:
        qt_limpeza += 1
    elif tipo_defeito == 3:
        qt_trocacabo += 1
    elif tipo_defeito == 4:
        qt_quebrado += 1
    
    totalM += 1  
pc_esfera = (qt_esfera / totalM) * 100
pc_limpeza = (qt_limpeza / totalM) * 100
pc_trocacabo = (qt_trocacabo / totalM) * 100
pc_quebrado = (qt_quebrado / totalM) * 100

print("Relatório Final")
print(f"Quantidade de mouses: {totalM}")
print("Situação Quantidade Percentual")
print(f"1- necessita da esfera {qt_esfera} {pc_esfera:.0f}%")
print(f"2- necessita de limpeza {qt_limpeza} {pc_limpeza:.0f}%")
print(f"3- necessita troca do cabo ou conector {qt_trocacabo} {pc_trocacabo:.0f}%")
print(f"4- quebrado ou inutilizado {qt_quebrado} {pc_quebrado:.0f}%")

input(" ")
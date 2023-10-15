# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
# fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200
# mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode
# aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá
# receber um número indeterminado de entradas, cada uma contendo: 
# um número de identificação do mouse e o tipo de defeito:
# o necessita da esfera;
# o necessita de limpeza; 
# necessita troca do cabo ou conector;
# a.quebrado ou inutilizado Uma identificação
# igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100
# Situação Quantidade Percentual
#
# 1- necessita da esfera 40 40%
# 2- necessita de limpeza 30 30%
# 3- necessita troca do cabo ou conector 15 15%
# 4- quebrado ou inutilizado 15 15%


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

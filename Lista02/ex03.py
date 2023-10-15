# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL,
# VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses
# carros faz com um litro de combustível. Calcule e mostre:
# . O modelo do carro mais econômico;
# a. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de
# 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo
# segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
# Os dados são fictícios e podem mudar a cada execução do programa.
# Comparativo de Consumo de Combustível
# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5
# Relatório Final
# 1 - fusca - 7.0 - 142.9 litros - R$ 321.43
# 2 - gol - 10.0 - 100.0 litros - R$ 225.00
# 3 - uno - 12.5 - 80.0 litros - R$ 180.00
# 4 - vectra - 9.0 - 111.1 litros - R$ 250.00
# 5 - peugeout - 14.5 - 69.0 litros - R$ 155.17
# O menor consumo é do peugeout.

# Define listas para armazenar os modelos de cinco carros e seus respectivos consumos

modelos = []
consumo = []

for i in range(5):
    modelo = input(f'Digite o modelo do carro {i + 1}: ')
    consumo_carro = float(input(f'Digite o consumo (km/l) do carro {i + 1}: '))

    modelos.append(modelo)
    consumo.append(consumo_carro)

mais_economico = 0
menor_consumo = consumo[0]

for i in range(1, len(consumo)):
    if consumo[i] < menor_consumo:
        menor_consumo = consumo[i]
        mais_economico = i

carro_mais_economico = modelos[mais_economico]

resultados = []  #pra armazenar os resultados depois :3

for i in range(len(modelos)):
    modelo = modelos[i]
    consumo_carro = consumo[i]
    
    litros_necessarios = 1000 / consumo_carro  #calcual quantos litros são necessários para 1000 Km
    custo = litros_necessarios * 2.25  #calcula custo com base no preço da gasolina (R$ 2,25 por litro)

    resultado_carro = (modelo, consumo_carro, litros_necessarios, custo)
    resultados.append(resultado_carro)

print(f"O carro mais econômico é: {carro_mais_economico}")

print("Relatório Final")
for i, resultado in enumerate(resultados):
    modelo, consumo_carro, litros_necessarios, custo = resultado
    print(f"{i + 1} - {modelo} - {consumo_carro:.1f} - {litros_necessarios:.1f} litros - R$ {custo:.2f}")

input(':3c')

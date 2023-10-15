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
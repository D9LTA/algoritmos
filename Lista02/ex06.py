# 6. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um
# vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma
# função para gerar numeros aleatórios, simulando os lançamentos dos dados
import random

resultados = []

for _ in range(100):
    resultado = random.randint(1, 6)
    resultados.append(resultado)
for valor in resultados:
    print(f"Valor: {valor}")
input('')

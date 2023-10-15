import random

resultados = []

for _ in range(100):
    resultado = random.randint(1, 6)
    resultados.append(resultado)
for valor in resultados:
    print(f"Valor: {valor}")
input('')
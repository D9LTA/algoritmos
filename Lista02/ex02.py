total_funcio = 0
minimo_funcio = 0
total_abono = 0
maior_abono = 0

while True:
    salario = float(input("Digite o salário (ou 0 para encerrar): "))
    
    if salario == 0:
        break
    
    abono = salario * 0.20  # 20% do salário
    if abono < 100:
        abono = 100  # Piso do abono

    total_funcio += 1
    total_abono += abono
    if abono == 100:
        minimo_funcio += 1
    if abono > maior_abono:
        maior_abono = abono

    print(f"Salário: R${salario:.2f} | Abono: R${abono:.2f}")

print(f"Total de funcionários processados: {total_funcio}")
print(f"Total a ser gasto com o pagamento do abono: R${total_abono:.2f}")
print(f"Funcionários que receberão o valor mínimo de R$100: {minimo_funcio}")
print(f"Maior valor pago como abono: R${maior_abono:.2f}")

input(" ")
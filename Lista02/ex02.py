# 2. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado
# alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma
# projeção de quanto será gasto com o pagamento deste abono.
# o Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato
# laboral, chegou-se a seguinte forma de cálculo:
# o a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono
# será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor
# mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de
# casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário
# de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a
# digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a
# cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
# o O salário de cada funcionário, juntamente com o valor do abono;
# o O número total de funcionário processados;
# o O valor total a ser gasto com o pagamento do abono;
# o O número de funcionário que receberá o valor mínimo de 100 reais;
# o O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins
# ilustrativos. Os valores podem mudar a cada execução do programa.
# Projeção de Gastos com Abono
# ============================
# Salário: 1000
# Salário: 300
# Salário: 500
# Salário: 100
# Salário: 4500
# Salário: 0
# Salário - Abono
# R$ 1000.00 - R$ 200.00
# R$ 300.00 - R$ 100.00
# R$ 500.00 - R$ 100.00
# R$ 100.00 - R$ 100.00
# R$ 4500.00 - R$ 900.00
# Foram processados 5 colaboradores
# Total gasto com abonos: R$ 1400.00
# Valor mínimo pago a 3 colaboradores
# Maior valor de abono pago: R$ 900.00

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

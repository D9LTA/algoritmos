# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de
# arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos
# usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele
# conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre 456123789
# anderson 1245698456
# antonio 123456456
# carlos 91257581
# cesar 987458
# rosemary 789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que
# gere um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc. Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr. Usuário Espaço utilizado % do uso
# 1 alexandre 434,99 MB 16,85%
# 2 anderson 1187,99 MB 46,02%
# 3 antonio 117,73 MB 4,56%
# 4 carlos 87,03 MB 3,37%
# 5 cesar 0,94 MB 0,04%
# 6 rosemary 752,88 MB 29,16%
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
# de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes
# deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do
# percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

total_usuarios = 0
etotal_bytes = 0
usuarios = []

with open ('usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split()
        nome = partes[0]
        espaco_bytes = int(partes[1])
        usuarios.append((nome, espaco_bytes))
        
        total_usuarios += 1
        etotal_bytes += espaco_bytes

medio_bytes = etotal_bytes / total_usuarios

with open("relatorio.txt", "w") as relatorio:
    relatorio.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
    relatorio.write("-" * 60 + "\n")
    relatorio.write("Nr. Usuário Espaço utilizado % do uso\n")

    for i, (nome, espaco_bytes) in enumerate(usuarios, start=1):
        espaco_mb = espaco_bytes / (1024 * 1024)
        percentual = (espaco_bytes / etotal_bytes) * 100  
        relatorio.write(f"{i} {nome} {espaco_mb:.2f} MB {percentual:.2f}%\n")

    espaco_total_mb = etotal_bytes / (1024 * 1024)
    espaco_medio_mb = medio_bytes / (1024 * 1024)
    relatorio.write(f"\nEspaço total ocupado: {espaco_total_mb:.2f} MB\n")
    relatorio.write(f"Espaço médio ocupado: {espaco_medio_mb:.2f} MB\n")
    input ('')

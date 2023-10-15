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
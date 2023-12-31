# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
# O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
# Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
# Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. 
# O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional Votos %
# ------------------- ----- ---
# Windows Server 1500 17%
# Unix 3500 40%
# Linux 3000 34%
# Netware 500 5%
# Mac OS 150 2%
# Outro 150 2%
# ------------------- -----
# Total 8800
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

Sistemas_operacionais = {
    "Windows Server": 0,
    "Unix": 0,
    "Linux": 0,
    "Netware": 0,
    "Mac OS": 0,
    "Outro": 0 
    }

# le os votos ate o 0
while True:
    try:
        voto = int(input('Digite o número correspondente ao sistema operacional (1 a 6, 0 para finalizar a votação): '))
        if voto == 0:
            break
        elif 1 <= voto <= 6:
            if voto == 1:
                sistema_operacional = "Windows Server"
            elif voto == 2:
                sistema_operacional = "Unix"
            elif voto == 3:
                sistema_operacional = "Linux"
            elif voto == 4:
                sistema_operacional = "Netware"
            elif voto == 5:
                sistema_operacional = "Mac OS"
            else:
                sistema_operacional = "Outro"

            # Atualiza a contagem dos votos corretamente
            Sistemas_operacionais[sistema_operacional] += 1
        else:
            print("Escolha respectivamente entre 1 a 6. 0 para finalizar a votação")
    except ValueError:
        print("Escolha respectivamente entre 1 a 6. 0 para finalizar a votação")

# Calculo dos votos
total_votos = sum(Sistemas_operacionais.values())

sistema_mais_votado = ""
votos_mais_votado = 0

print("Sistema Operacional Votos %")
print("------------------- ----- ---")
for sistema, num_votos in Sistemas_operacionais.items():
    percentual = (num_votos / total_votos) * 100
    print(f"{sistema} {num_votos} {percentual:.0f}%")

    if num_votos > votos_mais_votado:
        sistema_mais_votado = sistema
        votos_mais_votado = num_votos

print("------------------- ----- ---")
print(f"Total {total_votos}")

# Apresenta o resultado
print(f"O Sistema Operacional mais votado foi o {sistema_mais_votado}, com {votos_mais_votado} votos, correspondendo a {(votos_mais_votado / total_votos) * 100:.0f}% dos votos.")
input("...")

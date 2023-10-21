alunos = {
    '001': {'Nome': 'José', 'Nota1': 10, 'Nota2': 8, 'Média': 9},
    '002': {'Nome': 'Maria', 'Nota1': 10, 'Nota2': 10, 'Média': 10},
    '003': {'Nome': 'Pedro', 'Nota1': 5, 'Nota2': 5, 'Média': 5}
}

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

while True:
    print("                           CADASTRO DE ALUNOS")
    print('''
1- Incluir
2- Consultar/Alterar
3- Excluir
4- Listar
5- Sair''')

    opcao = input("Escolha uma opção (1 a 5): ")

    if opcao == '1':
        while True:
            print("\n                            Inclusão De Alunos")
            matricula = input("Matrícula do aluno: ")

            if matricula in alunos:
                print("Matrícula já existe. Tente novamente.")
            else:
                nome = input("Nome do aluno: ")
                nota1 = float(input("Nota 1: "))
                nota2 = float(input("Nota 2: "))
                media = calcular_media(nota1, nota2)

                print("\nMédia: {:.2f}".format(media))
                opcao_inclusao = input("Deseja incluir este aluno (S/N) ou retornar ao menu principal (R)? ").strip().upper()

                if opcao_inclusao == 'S':
                    alunos[matricula] = {'Nome': nome, 'Nota1': nota1, 'Nota2': nota2, 'Média': media}
                    print("Aluno incluído com sucesso!\n")
                    break
                elif opcao_inclusao == 'N':
                    break
                elif opcao_inclusao == 'R':
                    break
    elif opcao == '2':
        print("\nConsulta/Alteração de Alunos")
        matricula_consulta = input("Matrícula: ")

        if matricula_consulta in alunos:
            print("Nome:", alunos[matricula_consulta]['Nome'])
            print("Nota 1:", alunos[matricula_consulta]['Nota1'])
            print("Nota 2:", alunos[matricula_consulta]['Nota2'])
            print("Média:", alunos[matricula_consulta]['Média'])

            opcao_alteracao = input("Deseja alterar os dados deste aluno (S/N) ou retornar ao menu principal (R)? ").strip().upper()

            if opcao_alteracao == 'S':
                nome = input("Novo nome: ")
                nota1 = float(input("Nova Nota 1: "))
                nota2 = float(input("Nova Nota 2: "))
                media = calcular_media(nota1, nota2)
                alunos[matricula_consulta] = {'Nome': nome, 'Nota1': nota1, 'Nota2': nota2, 'Média': media}
                print("Dados do aluno atualizados com sucesso!\n")
            elif opcao_alteracao == 'N':
                continue
            elif opcao_alteracao == 'R':
                break
        else:
            print("Matrícula Inexistente. Tente novamente.")
        pass
    elif opcao == '3':
        print("\nExclusão de Alunos")
        matricula_exclusao = input("Matrícula: ")

        if matricula_exclusao in alunos:
            print("Nome:", alunos[matricula_exclusao]['Nome'])
            opcao_exclusao = input("Deseja excluir este aluno (S/N) ou retornar ao menu principal (R)? ").strip().upper()

            if opcao_exclusao == 'S':
                del alunos[matricula_exclusao]
                print("Aluno excluído")
            elif opcao_exclusao == 'N':
                continue
            elif opcao_exclusao == 'R':
                break
        else:
            print("Matrícula Inexistente. Tente novamente.")
        pass
    elif opcao == '4':
        while True:
            print("\nListagem de Alunos")
            print("Matrícula  Aluno       Nota 1       Nota 2      Média")
            for matricula, aluno in alunos.items():
                print(f"{matricula}       {aluno['Nome']}         {aluno['Nota1']}           {aluno['Nota2']}          {aluno['Média']}")
            
            opcao_listagem = input("Digite <N> para nova listagem ou <R> para retornar ao menu principal: ").strip().upper()
            if opcao_listagem == 'R':
                break
        pass
    elif opcao == '5':
        print("Saindo")
        break
    else:
        print("Opção inválida. Tente novamente.\n")

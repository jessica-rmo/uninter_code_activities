def main():
    print(">>> Bem-vindo(a) ao Controle de Estoque da Bicicletaria da Jéssica! <<<\n" +
    ">> Desenvolvido por Jéssica Raquel de Melo Oliveira (RU: 3593002) <<")

    # lista de peças cadastradas
    # cada peça é um dicionário com as infomrações da peça em questão
    pecas = []
    codigo_counter = 1

    while True:
        try:
            print("Escolha a opção desejada:")
            print(
                " 1. Cadastrar Peça\n" +
                " 2. Consultar Peça\n" +
                " 3. Remover Peça\n" +
                " 4. Sair"
            )
            opcao = int(input())

            if (opcao == 1):
                print(">>> Você selecionou a opção: Cadastrar Peça")
                cadastrarPeca(pecas, codigo_counter)
                codigo_counter += 1  # incrementando contador de código para a peça seguinte

            elif (opcao == 2):
                print(">>> Você selecionou a opção: Consultar Peça")
                consultarPeca(pecas)
            
            elif (opcao == 3):
                print(">>> Você selecionou a opção: Remover Peça")
                removerPeca(pecas)

            elif (opcao == 4):
                print(">>> Você selecionou a opção: Sair")
                break
            else:
                raise ValueError

        except ValueError:
            print("(!) Digite uma opção válida.")
            continue


def cadastrarPeca(pecas, codigo_counter):
    while True:
        try:
            print("Código da peça: {:03d}".format(codigo_counter))
            nome = input("Digite o nome da peça: ")
            fabricante = input("Digite o fabricante da peça: ")
            valor = float(input("Digite o valor da peça: "))
            if (valor <= 0):
                raise ValueError
            
            nova_peca = {
                "codigo": codigo_counter,
                "nome": nome,
                "fabricante": fabricante,
                "valor": valor
            }
            pecas.append(nova_peca)
            break  # saindo do loop de cadastro

        except ValueError:
            print("(!) Valor inválido. Digite um valor maior que zero para a peça.")
            continue


def consultarPeca(pecas):
    while True:
        try:
            print("Escolha a opção desejada:")
            print(
                " 1 - Consultar Todas as Peças\n" +
                " 2 - Consulta Peças por Código\n" +
                " 3 - Consulta Peças por Fabricante\n" +
                " 4 - Retornar"
            )
            opcao_consulta = int(input())

            if (opcao_consulta == 1):
                for peca in pecas:
                    printPeca(peca)
                printLine()

            elif (opcao_consulta == 2):
                codigo_peca = int(input("Digite o código da peça: "))
                for peca in pecas:
                    if (peca['codigo'] == codigo_peca):
                        printPeca(peca)
                        printLine()
                        break
            
            elif (opcao_consulta == 3):
                fabricante_peca = input("Digite o fabricante da peça: ")
                for peca in pecas:
                    if (peca['fabricante'] == fabricante_peca):
                        printPeca(peca)
                else:
                    print("(!) Fabricante não encontrado.")
                printLine()

            elif (opcao_consulta == 4):
                break
            else:
                raise ValueError
        except ValueError:
            print("(!) Digite uma opção válida.")
            continue


def removerPeca(pecas):
    while True:
        try:
            codigo_peca = int(input("Digite o código da peça a ser removida: "))

            for peca in pecas:
                if (peca['codigo'] == codigo_peca):
                    pecas.remove(peca)
                    print(f"(!) Peça removida com sucesso: {peca} ")
                    break
            else:
                print("(!) Peça não encontrada.")

            break  # saindo do loop de remoção

        except ValueError:
            print("(!) Digite um valor numérico válido.")
            continue


def printPeca(peca):  # função auxiliar para exibir as informações da peça
    printLine()
    print(f"| código     : {peca['codigo']}")
    print(f"| nome       : {peca['nome']}")
    print(f"| fabricante : {peca['fabricante']}")
    print( "| valor (R$) : {:.2f}".format(peca['valor']))


def printLine():  # função auxiliar para separar a exibição das peças
    print("+----------------------------------")


main()
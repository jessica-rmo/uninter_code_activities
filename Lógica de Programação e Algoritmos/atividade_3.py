
def main():  # função principal que chama as funções específicas do programa
    print(">>> Bem-vindo(a) a Cia de logística S.A. <<<\n" +
    ">> Desenvolvido por Jéssica Raquel de Melo Oliveira (RU: 3593002) <<")

    dimensoes = dimensoesObjeto()
    peso = pesoObjeto()
    rota = rotaObjeto()

    total = dimensoes * peso * rota
    print("Total a pagar (R$): {:.2f} ".format(total), end=" ")
    print(f"(dimensões: {dimensoes} * peso: {peso} * rota: {rota})")


def dimensoesObjeto():
    while True:
        try:
            altura = float(input("Digite a altura do objeto (em cm): "))
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))

            volume = altura * comprimento * largura
            print(f"O volume do objeto é (em cm³): {volume}")

            if (volume < 1000):
                return 10
            elif (volume < 10000):
                return 20
            elif (volume < 30000):
                return 30
            elif (volume < 100000): 
                return 50
            else:  # valor inválido --> volume >= 100000:
                raise Exception
        except ValueError:
            print("Você digitou uma dimensão com valor não numérico.")
            print("Por favor, informe as dimensões desejadas novamente.")
            continue
        except Exception:
            print("Não aceitamos objetos com dimensões dessa magnitude.")
            print("Por favor, informe as dimensões desejadas novamente.")
            continue

def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            if (peso <= 0.1):
                return 1
            elif (peso < 1):
                return 1.5
            elif (peso < 10):
                return 2
            elif (peso < 30):
                return 3
            else:  # valor inválido --> peso => 30
                raise Exception
        except ValueError:
            print("Você digitou o peso do objeto com valor não numérico.")
            print("Por favor, informe o peso novamente.")
            continue
        except Exception:
            print("Não aceitamos objetos com peso dessa magnitude.")
            print("Por favor, informe o peso novamente.")
            continue


def rotaObjeto():
    while True:
        try:
            print("Selecione a rota do objeto (digite a sigla): ")
            print(
                " RJSP - De Rio de Janeiro até São Paulo\n" +
                " SPRJ - De São Paulo até Rio de Janeiro\n" +
                " DFSP - De Brasília até São Paulo\n" +
                " SPDF - De São Paulo até Brasília\n" +
                " DFRJ - De Brasília até Rio de Janeiro\n" +
                " RJDF - Rio de Janeiro até Brasília\n" +
                ">>>", end=" ")
            rota = input()
            rotas = {  # dicionário com as siglas das rotas e os multiplicadores associados
                "RJSP": 1   , "SPRJ": 1   ,
                "DFSP": 1.2 , "SPDF": 1.2 ,
                "DFRJ": 1.5 , "RJDF": 1.5
            }
            if (rota.upper() not in rotas.keys()):  # verifica se o valor informado para a rota não existe como chave no dicionário
                raise Exception
            else:
                return rotas.get(rota.upper())  # se existe, seleciona o valor de acordo com a sigla informada
        except Exception:
            print("Você digitou uma rota inexistente.")
            print("Por favor, informe o rota novamente.")
            continue


main()

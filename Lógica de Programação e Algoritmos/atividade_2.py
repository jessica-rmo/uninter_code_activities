print("""
::::::::: +  Bem-vindo(a) à lanchonete da Jéssica  + :::::::::
Desenvolvido por Jéssica Raquel de Melo Oliveira (RU: 3593002)

.---------------------------------------------.
| ::::::::: +   C A R D Á P I O   + ::::::::: |
+---------+-----------------------+-----------+
|  Código |       Descrição       |   Valor   |
+---------+-----------------------+-----------+
|  100    | Cachorro-Quente       | R$   9.00 |       
|  101    | Cachorro-Quente Duplo | R$  11.00 |       
|  102    | X-Egg                 | R$  12.00 |       
|  103    | X-Salada              | R$  13.00 |       
|  104    | X-Bacon               | R$  14.00 |       
|  105    | X-Tudo                | R$  17.00 |       
|  200    | Refrigerante Lata     | R$   5.00 |       
|  201    | Chá Gelado            | R$   4.00 |       
+---------+-----------------------+-----------+
""")

cardapio = {  # dicionário que contém as informações do cardápio
    100: {'descricao': 'Cachorro-Quente', 'valor': 9.0},
    101: {'descricao': 'Cachorro-Quente Duplo', 'valor': 11.0},
    102: {'descricao': 'X-Egg', 'valor': 12.0},
    103: {'descricao': 'X-Salada', 'valor': 13.0},
    104: {'descricao': 'X-Bacon', 'valor': 14.0},
    105: {'descricao': 'X-Tudo', 'valor': 17.0},
    200: {'descricao': 'Refrigerante Lata', 'valor': 5.0},
    201: {'descricao': 'Chá Gelado', 'valor': 4.0}
}

# ----- variavais iniciais ----- #
total_pedido = 0.0

while True:
    codigo = int(input("Informe o código do produto desejado: "))

    if codigo not in cardapio:  # verifica se o código informado existe no cardápio
        print("Opção inválida.")
        continue

    total_pedido += cardapio[codigo]['valor']
    print(f"Você pediu um {cardapio[codigo]['descricao']} no valor de R$ {cardapio[codigo]['valor']:.2f}")

    opcao = int(input("Deseja pedir mais alguma coisa?\n 1 - Sim\n 0 - Não\n>> "))
    if opcao == 0:
        break
    elif opcao == 1:
        continue

print(f"O valor total a ser pago pelo pedido é: R$ {total_pedido:.2f}")

print("""
>>> Bem-vindo(a) ao calculador de descontos! <<<
>> Desenvolvido por Jéssica Raquel de Melo Oliveira (RU: 3593002) <<
""")

# ---- variaveis iniciais ---- #
preco_unidade = 0.0
qtd_produto = 0
desconto = 0.0

while True:
    try:  # verificação da entrada para o preço da unidade
        preco_unidade = float(input("Informe o valor de 1 unidade do produto: "))
        if (preco_unidade <= 0):
            raise ValueError
        break
    except ValueError:
        print("(!) Insira um valor numérico válido maior que zero.")
        continue  # retorna para o while da linha 6

while True:
    try:  # verificação da entrada para a quantidade do produto
        qtd_produto = int(input("Informe a quantidade do produto desejada: "))
        if (qtd_produto <= 0):
            raise ValueError
        break
    except ValueError:
        print("(!) Insira um valor inteiro e maior que zero.")
        continue  # retorna para o while da linha 16

valor_liquido = preco_unidade * qtd_produto
print(">>> O valor total sem desconto é: R$ {:.2f}".format(valor_liquido))

# loop para calcular o descondo de acordo com a entrada do usuario
if qtd_produto < 10:
    desconto = 0
elif qtd_produto < 100:
    desconto = 0.05
elif qtd_produto < 1000:
    desconto = 0.1
else:
    desconto = 0.15

valor_com_desconto = valor_liquido * (1 - desconto)
if (desconto == 0):  # if para printar mensagem caso não haja desconto
    print("    Nenhum desconto foi aplicado.")
else:  # caso haja desconto, informa o valor calculado ao usuário
    porcentagem = int(desconto * 100)  # calcula o valor da porcentagem para exibir ao usuario
    print(">>> O valor total com desconto é: R$ {a:.2f} (desconto: {b:}%)".format(a=valor_com_desconto,
    b=porcentagem))

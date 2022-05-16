"""
Funcoes - def
"""

# def funcao():
#     print("Test !")
# funcao()
#
# def saudacao(msg, nome):
#     print(msg, nome)
# saudacao("ola", "Richard")
#
# def testando(msg, nome):
#     print(msg, nome)
# testando(nome ="Richao", msg = "Hello")

"""
Funcoes - def - return
"""
# def funcao(var):
#     return var
#
# variavel = funcao("Valor que eu quero")
#
# if variavel:
#     print(variavel)
# else:
#     print("Nenhum valor.")

def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

divide = divisao(8,2)

if divide:
    print(divide)
else:
    print("Conta invalida")
"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""
# def function2():
#     print("GG!")
#
# def function1(function):
#     return function2()
#
#
# print(function2())
#######################################################################################

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número 
diferente de argumentos.
"""
def function1(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

function1(function2())
function1(function2())

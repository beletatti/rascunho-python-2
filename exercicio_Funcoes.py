"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""

# def saudacao(saudacao, nome):
#     print(saudacao, nome)
#
# saudacao("Ola seja bem-vindo,", "Richard")

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""

# def soma(n1, n2, n3):
#     return  print(n1 + n2 + n3)
# soma(2,2,2)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
# def function(n1, n2):
#     return print(n1 + ((n1 * n2) / 100))
#
# function(5, 10)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
def function(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        print("FIZZBUZZ")
    elif n1 % 5:
        print("BUZZ")
    elif n1 % 3:
        print("FIZZ")
    else:
        print ("f'{n1} NADA =(")
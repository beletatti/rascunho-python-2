# def funcao(arg, arg2):
#     return  arg * arg2
#
# var = funcao(2,2)
#
# a = lambda x , y: x * y
#
# print(a(2,2))

lista = [['P1',13],
['P2',12],
['P3',10],
['P4',19],
['P5',9]
]

print(sorted(lista, key=lambda  i: i[0], reverse=True))

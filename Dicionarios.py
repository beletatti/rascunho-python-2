# d1 = {'chave1': 'valor da chave'}
# d1 ['nova chave'] = 'Valor da nova chave'
#
# # print(d1)
# print(d1['chave1'])

# d1 = dict(chave1="Valor da key", chave2="Valor da outra key")
# d1['nova key'] = 'Valor da nova chave'
#
# print(d1)

# d1 = {1: 'valor', 2: 'valor', 3:'valor'}
# print(d1)

# d1 = {
#     'valor1' : 'valor',
#     'valor2' : 'Outro valor',
#     'valor3' : 'Tupla'
# }
# print(d1[(1,2,3,4)])

# for k in d1.items():
#     print(k[0], k[1])

# for k, v in d1.items():
#     print(k, v)

clientes = {
    'cliente1' : {
        'nome': 'Richard',
        'sobrenome': 'Beletatti',
    },
    'cliente2' : {
        'nome': 'Camila',
        'sobrenome': 'Beletatti',
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_k}')
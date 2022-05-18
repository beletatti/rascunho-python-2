''''Sistemas de respostas'''

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto e 2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '3',},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto e 3*2?',
        'respostas': {'a': '4', 'b': '10', 'c': '6',},
        'resposta_certa': 'c',
    },
}
print(" ")

resposta_certa = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]:{rv}')

    resposta_usuario = input("Digite sua resposta: ")

    if resposta_usuario == pv ['resposta_certa']:
        print("VOCE ACERTOU !!!")
        resposta_certa += 1
    else:
        print("VOCE ERROU !!!")
    print()

qtd_perguntas = len(perguntas)
porcetagem_acerto = resposta_certa / qtd_perguntas * 100

print(f'Voce acertou {resposta_certa} respostas.')
print(f'Sua porcentagem de acerto foi de {porcetagem_acerto}%.')

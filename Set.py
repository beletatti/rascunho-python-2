''''SET'''
#
# s1 = set()
#
# s1.add(1)
# s1.add(2)
# s1.add(3)
# s1.discard(2)
# s1.update('a') #armazena igual add
# s1.update('Python') #Armazena tudo fora de ordem
#
# print(s1)
#
# s2 = {1,2,3,4,5}
# s3 = {1,2,3,4,5,6}
#
# s4 = s2 | s3 # union
# print(s4)

# s2 = {1,2,3,4,5,7}
# s3 = {1,2,3,4,5,6}
#
# s4 = s2 - s3 # mostra diferenca dos dois
# print(s4)

s2 = {1,2,3,4,5}
s3 = {1,2,3,4,5,6}

s4 = s2 ^ s3 #elementos q estao nos dois set, mas nao estao em ambos
print(s4)
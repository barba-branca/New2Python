#!/usr/bin/python

idade = 17
pais = False

if idade >= 18:
    print "Voce pode ter habilitacao"
elif pais == True:
    print "Voce tem permissao para dirigir do seus pais"
else:
    print "Voce nao tem idade ainda"

for x in range(0,10):
    print(x)

produtos = ["camisetas","tenis","calca","bermuda","chapeu","jeans"]

for p in produtos:
    if p == "bone":
        print p+" encontrada"
        break
else:
    print "Produto nao encontrado"

for letra in "Python":
    if letra == "y":
        print letra + " encontrada"
        continue
    else: 
        print letra
    print "Testando continue"

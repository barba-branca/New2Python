#!/usr/bin/python

animais = ["gato","cachorro","tartaruga","papagaio","lagarto"]
mamiferos = []
aves = []
print "Lista de Aves: ", aves
aves.append("canario")
print "Lista de Aves atualizada: ", aves

print "Qtd de aves: ", len(aves)

animais.remove("papagaio") # remove o valor
print "Lista de Animais ", animais

aves.insert(0, "papagaio")
print "Lista de Aves atualizada: ", aves

aves.pop(1) #remove pelo indice
print "Lista de Aves atualizada: ", aves

aves.pop() #remove o ultimo item da lista
print "Lista de Aves atualizada: ", aves

print "Tartaruga esta no indice ", animais.index("tartaruga")

animais.reverse()
print "Animais invertida ", animais

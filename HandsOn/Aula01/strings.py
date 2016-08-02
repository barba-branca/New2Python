#!/usr/bin/python

nome = "Guido Van Rossum"
idade = 59

print "O Criador do ython se chama " +nome
print "A idade dele eh",idade

print "O " + nome + " idade" , idade

print "Criador do Python %s, a idade eh %s"%(nome,idade)

nome = raw_input("Digite o seu nome ")
idade = input("Digite a sua idade ") #Nao aceita letras - No Python 3 somente este funciona

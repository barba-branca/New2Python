#!/usr/bin/python

PI = 3.14
numero = 1 
dolar = 3.23
texto = "Curso de Python"
dicionario = {"dino":"animal pre-historico","cebola":"eh um tempero",3:"Numero tres",
              "4linux":4,
              "produtos":["Produto 1","Produto 2","Produto 3"]}

notas = [10, 8, 8, 9.5, 5]
materias = ["portugues","matematica","fisica", "artes", "geografia"]

tupla = ("parm1", "parm2", "parm3")

print zip(materias, notas)
print "**********************"

print dicionario.get("produtos")
print "**********************"
print "Valor 0 da tupla: ",tupla[0]
print dicionario.keys()[0]


    

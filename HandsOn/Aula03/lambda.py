#!/usr/bin/python

def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

print soma(2,2)
print subtracao(2,2)
print multiplicacao(2,2)

# como fazer o mesmo com LAMBDA

somar = lambda a,b: a+b
subtrair = lambda a,b: a-b
multiplicar = lambda a,b: a*b

print somar(2,2)
print subtrair(2,2)
print multiplicar(2,2)



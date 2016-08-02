#!/usr/bin/python
"""
Feito por: Yannick Belot
Data: 01/08/2016
Email: yannickbh@gmail.com
Objetivo: primeiro teste
"""
print "**** Sistema de Autenticacao ****"
print "Digite o seu usuario:"
usuario = raw_input()
senha = raw_input("Digite sua senha: ")

print "Autenticando o usuario " + usuario

if senha == "123456":
    print "Autenticado com Sucesso"
else:
    print "Falha na Autenticacao"

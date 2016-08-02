#!/usr/bin/python

usuario = raw_input("Informe o seu usuario: " ) 

senha = raw_input("Informe a sua senha: ")

usuarios = {"Yannick":"123456"}
print usuarios.keys()[0]
print usuarios.get(usuarios.keys()[0])

if (usuario == usuarios.keys()[0]) and (senha == usuarios.get(usuarios.keys()[0])):
    print("Usuario autenticado com sucesso")
    print("Seja Bem Vindo " +usuario)
else:
    print("Acesso Negado")

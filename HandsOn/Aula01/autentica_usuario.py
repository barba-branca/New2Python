#!/usr/bin/python

usuario = raw_input("Informe o seu usuario: " ) 

senha = raw_input("Informe a sua senha: ")

if (usuario == "Yannick") and (senha == "123456"):
    print("Usuario autenticado com sucesso")
    print("Seja Bem Vindo " +usuario)
else:
    print("Acesso Negado")

#!/usr/bin/python

usuarios = []

def cadastrar_usuario(nome, descricao="vazia", teste=""): #Parametros nao obrigatorios SEMPRE no final
    global usuarios #obtem variavel global
    print "USUARIOS", usuarios
    for u in usuarios:
        if u == nome:
            print "Usuario ja cadastrado"
            break
        else:
            usuarios.append(nome)

    return nome

cadastrar_usuario("Yannick")
cadastrar_usuario("Joao")
cadastrar_usuario("Joao")

print usuarios

#cadastrar_usuario("1","2","3")


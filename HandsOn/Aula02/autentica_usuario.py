#!/usr/bin/python

usuarios = []
senhas = []

def listar_opcoes():
    print "1 - Cadastrar Usuario"
    print "2 - Acessar Sistema"
    print "3 - Sair do Sistema"

def switch(x):
    dic_funcoes = {1: cadastrar_usuario,
                   2: acessar_sistema,
                   3: sair_sistema}
    dic_funcoes[x]()

def sair_sistema():
    print "Sair do Sistema"
    exit()

def cadastrar_usuario():
    print "Cadastrar Usuario"
    global usuarios
    global senhas

    login = raw_input("Digite o login do usuario: ")
    senha = raw_input("Digite a senha do usuario: ")
    usuarios.append(login)
    senhas.append(senha)

def acessar_sistema():

    global usuarios
    global senhas

    usuario = raw_input("Informe o seu usuario: " ) 
    senha = raw_input("Informe a sua senha: ")
 
    for usuario in usuarios:

        indice = usuarios.index(usuario)
        
        if usuarios.index(usuario) == 0: 
            print "Usuario nao encontrado."
            break
        elif senhas[indice] != senha:
            print "Senha nao confere"
            break
        else:
            print "Acesso liberado ao Sistema"
            print("Seja Bem Vindo " +usuario) 

while True:
    listar_opcoes()
    opcao = int(raw_input("Digite a opcao desejada: "))
    switch(opcao)
    

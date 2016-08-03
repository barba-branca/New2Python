#!/usr/bin/python

usuarios = []
servidores = []
senhas = []

def switch(x):
    dic_funcoes = {1: cadastrar_sysadmin,
                   2: listar_sysadmin,
                   3: remover_sysadmin,
                   4: cadastrar_servidor}
    dic_funcoes[x]()

def cadastrar_sysadmin(): # se nao houver parametro, assume "vazio"
    print "Cadastrando Sysadmin"
    global usuarios
    global senhas
    login = raw_input("Digite o login do usuario: ")
    senha = raw_input("Digite a senha do usuario: ")
    usuarios.append(login)
    senhas.append(senha)
    return (login, senha)

def listar_sysadmin():
    print "Listando Sysadmin"
    global usuarios
    for i,u in enumerate(usuarios):
        print "ID %s Usuario %s "%(i, u)
        #print "SEGUNDA - ID %s Usuario %s "%(usuarios.index(u), u)

def remover_sysadmin():
    print "Removendo Sysadmin"
    global usuarios
    global senhas
    listar_sysadmin()
    indice = input("Informe o indice de quem voce deseja remover: ")
    usuarios.pop(indice)
    senhas.pop(indice)

def cadastrar_servidor():
    login, senha = cadastrar_sysadmin()
    if autenticar_usuario(login, senha):
        print "CADASTRAR SERVIDOR"
    else:
        print "Voce nao tem permissao para cadastrar servidores"
    
def autenticar_usuario(login, senha):
    global usuarios
    global senhas
    for usuario in usuarios:
        if usuario == login:
            indice = usuarios.index(usuario)
            if usuarios[indice] == login and senhas[indice] == senha:
                print "Atenticacao Realizada com Sucesso!"
                return True        
            else:
                return False
    
    
def listar_opcoes():
    print "1 - Cadastrar Sysadmin"
    print "2 - Listar Sysadmin"
    print "3 - Remover Sysadmin"
    print "4 - Cadastrar Servidor"
    print "5 - Listar Servidores"
    print "6 - Remover Servidor"
    print "7 - Sair do Programa"

while True:
    listar_opcoes()
    opcao = int(raw_input("Digite a opcao desejada: "))
    switch(opcao)
    if opcao == 7:
        break
"""
if opcao == 1:
    print "Funcao: Cadastrar Sysadmin"
elif opcao == 2:
    print "Funcao: Listar Sysadmin"
elif opcao == 3:
    print "Funcao: Remover Sysadmin"
elif opcao == 4:
    print "Funcao: Cadastrar Servidor"
elif opcao == 5:
    print "Funcao: Listar Servidores"
elif opcao == 6:
    print "Funcao: Remover Servidor"
elif opcao == 7:
    print "Funcao: Sair do Sistema"
else:
    print "Opcao invalida"
"""

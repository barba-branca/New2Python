#!/usr/bin/python

import json

def ler_banco():
    with open("banco.json","r") as f: # with define o contexto no python + caminho absoluto arquivo + r = read
        dados = json.loads(f.read()) # converte arquivo String (json) para dicionario 
    return dados

def escrever_banco(dado):
    with open("banco.json","w") as f: # "w" = write
        dado = json.dumps(dado) # converte dicionario em string
        f.write(dado)         

def cadastrar_usuario(): # se nao houver parametro, assume "vazio"
    dados = ler_banco()
    usuario = {}
    usuario['login'] = raw_input("Digite o login do usuario: ")
    usuario['senha'] = raw_input("Digite a senha do usuario: ")
    
    dados['usuarios'].append(usuario)       
    escrever_banco(dados)   

def listar_usuario():    
    dados = ler_banco()
    print "##############",dados.keys()
    print produtos["usuarios"][1]
    for i in dados.keys():
        #print dados.keys()[i]
        print dados.get['usuarios'][i]        

def remover_usuario():
    print "Removendo Sysadmin"
    global usuarios
    global senhas
    listar_sysadmin()
    indice = input("Informe o indice de quem voce deseja remover: ")
    usuarios.pop(indice)
    senhas.pop(indice)

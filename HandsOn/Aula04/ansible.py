#!/usr/bin/python
# arquivo: ansible.py
# 
from datetime import datetime, timedelta
from Modulos.SSH import executar_comando
#import Modulos.SSH
from Modulos.Usuarios import cadastrar_usuario, listar_usuario, remover_usuario


def switch(x):
    try: 
        dic_funcoes = {1: cadastrar_usuario,
                       2: listar_usuario,
                       3: remover_usuario}
        dic_funcoes[x]()
    except Exception as e:
        print "Opcao %s eh Invalida"%e 

acesso = datetime(2016,8,3,20,00,00) # deveria importar a datetime.now() na hora do acesso
expira = datetime(2016,8,3,20,59,00) # Criacao de logica para ficar uma hora disponivel para rodar

# se o tempo >= 1 hora, nao permite executar
if (expira - acesso).total_seconds() >= 3600:
    print "Seu token expirou"
    sys.exit()
else:
    executar_comando("pwd") # Nome da funcao a ser executada
    #Modulos.SSH.executar_comando("pwd") # Nome da funcao a ser executada

def listar_opcoes():
    print "1 - Cadastrar Usuario"
    print "2 - Listar Usuarios"
    print "3 - Remover Usuario"
#    print "4 - Cadastrar Servidor"
#    print "5 - Listar Servidores"
#    print "6 - Remover Servidor"
#    print "7 - Sair do Programa"

if __name__ == '__main__':

    while True:
        listar_opcoes()
        opcao = int(raw_input("Digite a opcao desejada: "))
        switch(opcao)






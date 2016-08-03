#!/usr/bin/python

print "###### SISTEMA AUTO ESCOLA ########"

nome = raw_input("Digite o seu nome: ")
idade = raw_input("Digite a sua idade: ")

if int(idade) >= 18:
    print "Voce pode ter habilitacao"
else:
    responsavel = raw_input("Esta acompanhado do responsavel? ")
    if responsavel[0].lower() in "sim":
        nome_responsavel = raw_input("Informe o nome do responsavel: ")
        print "Cliente Cadastrado"
    else:
        print("Nao foi possivel efetutar o cadastro")

#!/usr/bin/python

def parametro_dinamicos(*args): # parametros especificos
    print args
    print args[3][2]

parametro_dinamicos(1,2,"Yannick",[9,9,"abracadabra"])

def exemplo_api(**kwargs): # mais utilizado para APIs
    print kwargs
    print kwargs.get("nome")

exemplo_api(nome='Yannick')
exemplo_api(nome='Yannick', sobrenome='Belot')

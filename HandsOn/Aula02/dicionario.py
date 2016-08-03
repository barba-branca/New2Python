#!/usr/bin/python

produtos = {"nome":"Celular",
            "preco": 823.32,
            "caracteristicas":["tela", "cor", "bateria"]}
print produtos.get("nome")
print produtos["caracteristicas"]
print produtos["caracteristicas"][0]

produtos["nome"] = "Moto X"
print produtos

produtos["caracteristicas"][1] = "dimensao"
print produtos

produtos["caracteristicas"].append("antena")
print produtos
produtos["caracteristicas"].reverse()

print produtos
produtos["nota"] = 4.8
print produtos

print produtos.keys()
print produtos.values()

for keys in produtos.keys():
    print "Chave:", keys
    print "Valor:", produtos.get(keys)

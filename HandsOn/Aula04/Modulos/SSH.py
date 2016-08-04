#!/usr/bin/python

from datetime import datetime, timedelta
import paramiko

def executar_comando(cmd):
        
    # Automatiza o SSH
    client = paramiko.SSHClient()
    client.load_system_host_keys() # le o arquivo know_hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # aceita fingerprint automaticamente
    client.connect(hostname="127.0.0.1", username="forlinux", password="4linux") # conecta na maquina

    #stdin, stdout, stderr = client.exec_command("sudo apt-get update -y") # executa comando do Sistema Operacional
    stdin, stdout, stderr = client.exec_command(cmd) # executa comando do Sistema Operacional
    #stdin, stdout, stderr = client.exec_command("XPTO") # ERRO executa comando stdout = sucesso, stderr = erro

    log = datetime.now()

    if stderr.channel.recv_exit_status() != 0:
        print "FALHOU:: ", stderr.read()
        print "Executado as ", log     
    else:
        print "FUNCIONOU:: ", stdout.read()
        print "Executado as ", log + timedelta(7)

if __name__ == '__main__':
    print "############ Importando arquivo do SSH ############"
    print __name__
#executar_comando("hostname")



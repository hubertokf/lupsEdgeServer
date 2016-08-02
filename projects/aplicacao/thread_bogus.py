import  main.set_add
import socket
import _thread

HOST = '10.0.50.184'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
var = main.set_add(1)
def conectado(con, cliente):
    print("Conectado por", cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        #print cliente, msg
        if msg == "1":
            #set_add(1)         <--- CHAMAR METODO PARA SETAR VALOR
            print("FOI")
        else:
            print("JUCA")

    print("Finalizando conexao do cliente", cliente)
    con.close()
    _thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    _thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()

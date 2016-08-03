from analisador import  *
import socket
import _thread

HOST = '192.168.15.10'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
#var = main.set_add(1)
def conectado(con, cliente):
    print("Conectado por", cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        #print cliente, msg
        if msg is '1':
            #set_add(1)         <--- CHAMAR METODO PARA SETAR VALOR
            #juca.set_add(1)
            print("FOI")
        else:
            self.juca.set_add(1)
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
    _thread.start_new_thread(juca = Analisador_Complexo())

tcp.close()

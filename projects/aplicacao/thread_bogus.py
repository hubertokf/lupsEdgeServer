from analisador import  *
import socket
import _thread

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
#print s.getsockname()[0]

HOST = s.getsockname()[0]              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
#var = main.set_add(1)
asd = 0

class Asd(object):
    def __init__(self):
        self.asd = 0

    def set_asd(self, val):
        self.asd = val

    def get_asd(self):
        return self.asd

def conectado(con, cliente, asd):
    #global asd
    print("Conectado por", cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        #print cliente, msg
        #print(type(msg.decode()))
        if msg.decode() == "aba":
            #set_add(1)         <--- CHAMAR METODO PARA SETAR VALOR

            #asd = 1
            asd.set_asd(1);
            #print("FOI")
        else:
            #self.juca.set_add(1)
            #asd = 0
            asd.set_asd(0);
            #print("JUCA")

        #print(asd.get_asd())
    print("Finalizando conexao do cliente", cliente)
    con.close()
    _thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    asd = Asd();
    _thread.start_new_thread(conectado, tuple([con, cliente, asd]))
    _thread.start_new_thread(juca = Analisador_Complexo(asd))#, tuple([asd]))

tcp.close()

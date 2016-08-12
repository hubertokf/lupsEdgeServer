from analisador import  *
import socket
import _thread

#--------------------------Pega o IP local da máquina---------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))

HOST = s.getsockname()[0]              # Endereco IP do Servidor
PORT = 5000                            # Porta que o Servidor esta
#-------------------------------------------------------------------------------


#---------------------Objeto compartilhado entre as THREADS---------------------
class Asd(object):
    def __init__(self):
        self.asd = 1

    def set_asd(self, val):
        self.asd = val

    def get_asd(self):
        return self.asd
#-------------------------------------------------------------------------------


#----------------------Função de comunicação, por SOCKET------------------------
def conectado(con, cliente, asd):
    print("Conectado por", cliente)     # Utilizado p/ verificar quem conecta

    while True:
        msg = con.recv(1024)            # Tamanho max da mensagem "(bytes)???"
        if not msg: break

        if msg.decode() == "aba":       # Variável utilizada para ativar a veri-
            asd.set_asd(1);             #cação, ADD/REMOVENDO sensores do CRON
        else:
            asd.set_asd(0);
    print("Finalizando conexao do cliente", cliente)
    con.close()
    _thread.exit()

#-------------------------------------------------------------------------------


#----------------------------------MAIN-----------------------------------------
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # Reconect, utilizada
                                            # quando a conecção n foi finalizada

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:                     # Cria duas THREADS, SOCKET e ANALIZADOR
    con, cliente = tcp.accept()
    asd = Asd();
    _thread.start_new_thread(conectado, tuple([con, cliente, asd]))
    _thread.start_new_thread(juca = Analisador_Complexo(asd))#, tuple([asd]))
    
tcp.close()

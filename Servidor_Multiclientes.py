# Importa la librería
import socket , threading

# Clase
class Atiende(threading.Thread):

    # Constructor
    def __init__(self,Socket,Origen):
        # Inicia el Hilo
        threading.Thread.__init__(self)
        
        # crea el socket para controlar
        self.socket = Socket
        
        # crea el origen
        self.origen = Origen
                
    # El código que ejecutará el Hilo        
    def run(self):
        #mensaje
        print ("Resiviendo Cliente:")
        print (self.origen[0],":",self.origen[1])

        # Ciclo para  
        while True:  
            # Recibir datos
            recibido = self.socket.recv(100)  
            if recibido.decode("utf-8") == "salir":  
                break        
            print (self.origen[0],":",self.origen[1],end="")
            print (">",recibido.decode("utf-8"))    
            
        # Sale  
        print ("Cerrando la conexión con:",end="")
        print (self.origen[0],":",self.origen[1])
  
        # Cierra la conexión
        self.socket.close()              
                
# Crea un objeto de Sockets  
SocketServidor = socket.socket()   
print("Socket creado con Exito ...")

# Se conecta a un servidor a través de un puerto
SocketServidor.bind(("localhost", 8000))  
print("Conectando a localhost por puerto 8000...")

# Se dispone a escuchar
SocketServidor.listen(3)
print("Interlazando...")

# Ciclo para atender conexiones
while True:

    # Acepta a un Cliente
    SocketCliente, addr = SocketServidor.accept()     

    #Crea un objeto
    xSocket = Atiende(SocketCliente, addr)

    xSocket.start()
 
# Cierra el Servidor
SocketServidor.close()
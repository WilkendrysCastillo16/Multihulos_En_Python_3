# Importa la librería
import socket  

# Crea el Socket  
Socket_Clientes = socket.socket()   

# Se conecta al localhost
Socket_Clientes.connect(("localhost", 8000))  

# Ciclo para mandar mensajes  
while True:  

      # Solicita mensaje a enviar
      mensaje = input("> ")  
      # Enviando el Mensaje
      Socket_Clientes.send(bytes(mensaje,'utf-8'))  
      # Si mensaje
      if (mensaje == "salir"):  
         break  
         
# Mensaje de salida del Cliente  
print ("El Cliente ha finalizado")

# Cierra el Socket  
Socket_Clientes.close()
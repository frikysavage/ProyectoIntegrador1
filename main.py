import readchar
from readchar import readkey, key
def Juego():
    d=0
    jueg=True
    while d==0:
     print("Hola y bienvenido al juego deL Laberinto por favor escribe tu nombre para iniciar el juego o presiona 1 para salir")
     nombre=input()
     if nombre=="1":
      d=1
     else:
        print("Escribe lo que que quieras ", nombre)
        while jueg==True:
          tecla = readchar.readkey()
          teclaespecial= readkey()
          print(tecla, end="")
          if teclaespecial == key.UP:
             print("Gracias por jugar")
             break

if __name__ == "__main__":
    Juego()

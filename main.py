import os, readchar
from readchar import readkey
def borrarpantalla():
    contador=0
    print("Bienvenido al contador de borradas , escribe lo que quieras para contar y borrar")
    while contador<50:
        tecla=readchar.readkey()
        if ord(tecla)>0:
            os.system('cls' if os.name=='nt' else 'clear')
            contador=contador+1
            print(contador)
        
    
if __name__ == "__main__":
    borrarpantalla()

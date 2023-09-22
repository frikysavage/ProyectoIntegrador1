import os
from readchar import readkey, key

def cadena_mapa():
    matriz = [list(linea) for linea in cadena.split("\n")]
    return matriz

cadena = "..###\n....#\n###.#\n###..\n####."
matriz = cadena_mapa()

def limpiar():
    os.system('cls')

pj = "P"
i = 0

posinicial = [0, 0]
posfinal = [4, 4]

def mainloop():
    global posinicial, posfinal, matriz
    
    while True:
        print("Bienvenido al juego del laberinto por favor ingrese su nombre")
        nombre = input()
        limpiar()
        print(f"Hola {nombre} este es el menu principal")
        print("1.Jugar")
        print("2.Salir")
        seleccion = input()
        limpiar()
        if seleccion == "1":
            matriz[posinicial[0]][posinicial[1]] = pj
            while matriz[posfinal[0]][posfinal[1]] != pj:
                for fila in matriz:
                    print("".join(fila))
                k = readkey()
                if k == key.DOWN:
                    # Mover hacia abajo
                    if posinicial[0] < len(matriz) - 1 and matriz[posinicial[0] + 1][posinicial[1]] != "#":
                        matriz[posinicial[0]][posinicial[1]] = "."
                        posinicial[0] += 1
                        matriz[posinicial[0]][posinicial[1]] = pj
                    limpiar()
                elif k == key.UP:
                    # Mover hacia arriba
                    if posinicial[0] > 0 and matriz[posinicial[0] - 1][posinicial[1]] != "#":
                        matriz[posinicial[0]][posinicial[1]] = "."
                        posinicial[0] -= 1
                        matriz[posinicial[0]][posinicial[1]] = pj
                    limpiar()
                elif k == key.RIGHT:
                    # Mover hacia la derecha
                    if posinicial[1] < len(matriz[0]) - 1 and matriz[posinicial[0]][posinicial[1] + 1] != "#":
                        matriz[posinicial[0]][posinicial[1]] = "."
                        posinicial[1] += 1
                        matriz[posinicial[0]][posinicial[1]] = pj
                    limpiar()
                elif k == key.LEFT:
                    # Mover hacia la izquierda
                    if posinicial[1] > 0 and matriz[posinicial[0]][posinicial[1] - 1] != "#":
                        matriz[posinicial[0]][posinicial[1]] = "."
                        posinicial[1] -= 1
                        matriz[posinicial[0]][posinicial[1]] = pj
                    limpiar()
            print(f"Gracias por jugar {nombre}, has ganado")
            break
        elif seleccion == "2":
            limpiar()
            print(f"Hasta la próxima {nombre}")
            break

mainloop()
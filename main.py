import os
import random
from readchar import readkey, key


class Juego:
    def __init__(self, mapa, pos_inicial, pos_final):
        self.matriz = self.cargar_mapa(mapa)
        self.pos_inicial = pos_inicial
        self.pos_final = pos_final
        self.pj = "P"

    def cargar_mapa(self, mapa):
        matriz = [list(linea) for linea in mapa.split("\n")]
        return matriz

    def limpiar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def jugar(self):
        while True:
            self.limpiar()
            print("Bienvenido al juego del laberinto, por favor ingrese su nombre")
            nombre = input()
            self.limpiar()
            print(f"Hola {nombre}, este es el menú principal")
            print("1. Jugar")
            print("2. Salir")
            seleccion = input()
            if seleccion == "1":
                self.matriz[self.pos_inicial[1]][self.pos_inicial[0]] = self.pj
                while self.matriz[self.pos_final[1]][self.pos_final[0]] != self.pj:
                    self.limpiar()
                    for fila in self.matriz:
                        print("".join(fila))
                    k = readkey()
                    self.mover_personaje(k)
                self.limpiar()
                print(f"¡Felicitaciones {nombre}, has ganado!")
                seguir_jugando = input("¿Deseas jugar nuevamente? (1 para sí, 2 para no): ")
                self.limpiar()
                if seguir_jugando != "1":
                    print(f"Hasta la próxima {nombre}")
                    return
            elif seleccion == "2":
                self.limpiar()
                print(f"Hasta la próxima {nombre}")
                return


    def mover_personaje(self, direccion):
        px, py = self.pos_inicial
        if direccion == key.DOWN:
            if py < len(self.matriz) - 1 and self.matriz[py + 1][px] != "#":
                self.matriz[py][px] = "."
                self.pos_inicial = [px, py + 1]
                self.matriz[py + 1][px] = self.pj
        elif direccion == key.UP:
            if py > 0 and self.matriz[py - 1][px] != "#":
                self.matriz[py][px] = "."
                self.pos_inicial = [px, py - 1]
                self.matriz[py - 1][px] = self.pj
        elif direccion == key.RIGHT:
            if px < len(self.matriz[0]) - 1 and self.matriz[py][px + 1] != "#":
                self.matriz[py][px] = "."
                self.pos_inicial = [px + 1, py]
                self.matriz[py][px + 1] = self.pj
        elif direccion == key.LEFT:
            if px > 0 and self.matriz[py][px - 1] != "#":
                self.matriz[py][px] = "."
                self.pos_inicial = [px - 1, py]
                self.matriz[py][px - 1] = self.pj


class JuegoArchivo(Juego):
    def __init__(self, archivo_mapa):
        ruta_archivo = os.path.join(os.path.dirname(__file__), archivo_mapa)
        with open(ruta_archivo, 'r') as mapa_archivo:
            contenido = mapa_archivo.read().splitlines()

        posiciones = list(map(int, contenido[0].split()))
        pos_inicial = [posiciones[0], posiciones[1]]
        pos_final = [posiciones[2], posiciones[3]]

        mapa = "\n".join(contenido[1:])

        super().__init__(mapa, pos_inicial, pos_final)


def main():
    print("Bienvenido al juego del laberinto")
    while True:
        print("1. Jugar con mapa predefinido")
        print("2. Jugar con mapa aleatorio")
        print("3. Salir")
        seleccion = input()

        if seleccion == "1":
            juego = Juego(
                "..###\n....#\n###.#\n###..\n####.", [0, 0], [4, 4])
            juego.jugar()
            break
        elif seleccion == "2":
            mapa_aleatorio = random.choice(['mapa1.txt', 'mapa2.txt'])
            juego = JuegoArchivo(mapa_aleatorio)
            juego.jugar()
            break
        elif seleccion == "3":
            print("¡Hasta la próxima!")
            return


if __name__ == "__main__":
    main()


from reloj import Reloj
import threading
import time


class Berkeley:

    def __init__(self, relojes=[]):
        self.esclavos = []
        self.maestro: Reloj = None
        for r in relojes:
            if r.get_lat() == 0:
                self.maestro = r
            else:
                self.esclavos.append(r)


        if self.maestro is None:
            print("No se encontró al master")
            return
        if len(self.esclavos) == 0:
            print("No hay esclavos")
            return

        self.proc = threading.Thread(target=self.berkeley_loop, args=())

    def sincronizar(self):
        self.proc.start()

    def berkeley_loop(self):
        while True:
            self.berkeley()
            time.sleep(3)

    def berkeley(self):
        diferencias = []
        for e in self.esclavos:
            diff = self.calcular_diferencia(self.maestro, e)
            diferencias.append(diff)
        prom = self.calcular_promedio(diferencias)
        synchronized_time = self.maestro.current_time + prom
        self.maestro.set_current_time(synchronized_time)
        self.broadcast_time(synchronized_time)


    def calcular_diferencia(self, maestro, esclavo):
        dif = maestro.current_time - esclavo.current_time
        return dif

    def calcular_promedio(self, diferencias):
        sum = 0
        for d in diferencias:
            sum += d
        prom = sum / len(diferencias)
        return prom

    def broadcast_time(self, synchronized_time):
        for e in self.esclavos:
            e.set_current_time(synchronized_time)
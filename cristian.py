from reloj import Reloj
import time
import threading


class CristianStarter:

    def __init__(self, relojes=[]):
        self.esclavos = []
        self.maestro: Reloj = None
        for r in relojes:
            if r.get_lat() == 0:
                self.maestro = r

        for r in relojes:
            if r.get_lat() > 0:
                self.esclavos.append(Cristian(self.maestro, r))

    def sincronizar(self):
        for e in self.esclavos:
            e.sincronizar()


class Cristian:

    def __init__(self, master: Reloj, esclavo: Reloj):
        self.reloj = esclavo
        self.master = master

        self.proc = threading.Thread(target=self.cristian, args=())

    def sincronizar(self):
        self.proc.start()

    def cristian(self):
        while True:
            now = self.master.get_current_time()
            self.reloj.set_current_time(now)
            time.sleep(1)

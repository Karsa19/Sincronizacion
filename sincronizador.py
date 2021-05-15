import cristian
import berkeley
import reloj


class Sincronizador:

    def __init__(self, relojes=[]):
        self.relojes =  relojes
        self.ber = berkeley.Berkeley(relojes)
        self.cri = cristian.CristianStarter(relojes)

    def set_relojes(self, relojes):
        self.relojes = relojes
        self.ber = berkeley.Berkeley(relojes)
        self.cri = cristian.CristianStarter(relojes)

    def get_relojes(self):
        return self.relojes

    def get_coordinador(self):
        return self.ber.maestro

    def start_berkeley(self):
        self.ber.sincronizar()

    def start_cristian(self):
        self.cri.sincronizar()

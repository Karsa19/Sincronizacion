import cristian
import berkeley
import reloj

class Sincronizador:

    def __init__(self, relojes=[], coordinador):

        self.relojes =  relojes
        self.coordinador = coordinador


    def set_relojes(self, relojes):
        self.relojes = relojes

    def set_coordinador(self, relojes):
        
        for r in relojes:
            if r.lat= 0:
                self.coordinador = r
                break
        

    def get_relojes(self):
        return self.relojes

    def get_coordinador(self):
        return self.coordinador
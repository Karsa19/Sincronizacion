from datetime import timezone
import datetime
import threading
import time
from datetime import datetime


class Reloj:

    def __init__(self, hrs=0, mins=0, segs=0, lat=0):
        self.hrs = hrs
        self.mins = mins
        self.segs = segs
        self.lat = lat

        today = datetime.utcnow().date()
        self.midnight = datetime.combine(today, datetime.min.time())
        self._actualiza_reloj()
        reloj = threading.Thread(target=self.cuerda_reloj, args=())
        reloj.start()

    def _actualiza_reloj(self):
        self.current_time = round(self.midnight.timestamp() * 1000) + self.hrs * 60 * 60 * 1000 + self.mins * 60 * 1000 + self.segs * 1000
        self._actualiza_fecha()

    def _actualiza_fecha(self):
        self.current_dt = datetime.fromtimestamp(self.current_time / 1000.0, tz=timezone.utc)

    def cuerda_reloj(self):
        while True:
            time.sleep(0.010)
            self.current_time += 10
            self._actualiza_fecha()

    def set_hrs(self, hrs):
        self.hrs = hrs
        self._actualiza_reloj()

    def set_mins(self, mins):
        self.mins = mins
        self._actualiza_reloj()

    def set_segs(self, segs):
        self.segs = segs
        self._actualiza_reloj()

    def set_lat(self, lat):
        self.lat = lat

    def get_hrs(self):
        return self.current_dt.hour

    def get_mins(self):
        return self.current_dt.minute

    def get_segs(self):
        return self.current_dt.second

    def get_lat(self):
        return self.lat

    def set_current_time(self, current_time):
        time.sleep(self.lat)
        self.current_time = current_time + self.lat * 1000
        self._actualiza_fecha()

    def get_current_time(self):
        return self.current_time
    
    def mustrar_reloj(self):
        h = self.get_hrs()
        m = self.get_min()
        s = self.get_segs()
        l = self.get_lat()

        print(h + ":" + m + ":" + s + "\n Lat: " + l)

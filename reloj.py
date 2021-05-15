
from datetime import timezone
import datetime
import sys

class Reloj:

    def __init__(self, hrs=0, mins=0, segs=0, lat=0):
        self.hrs = hrs
        self.mins = mins
        self.segs = segs
        self.lat = lat
        
    def set_hrs(self, hrs):
        self.hrs = hrs

    def set_mins(self, mins):
        self.mins = mins

    def set_segs(self, segs):
        self.segs = segs

    def set_lat(self, lat):
        self.lat = lat

    def get_hrs(self):
        return self.hrs

    def get_mins(self):
        return self.mins

    def get_segs(self):
        return self.segs

    def get_lat(self):
        return self.lat

    
    def mustrar_reloj(self):
        h = get_hrs()
        m = get_min()
        s = get_segs()
        l = get_lat()

        print(h + ":" + m + ":" s + "\n Lat: " + l)

    def tiempo_seg(self):
        seg = (hrs*3600) + (mins*60) + segs

        return seg
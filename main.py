from reloj import Reloj
from sincronizador import Sincronizador
import time


def main():
    print("Algoritmos de Sincronización")
    r1 = Reloj(hrs=15, mins=0, segs=0, lat=0)
    r2 = Reloj(hrs=14, mins=25, segs=27, lat=1)
    r3 = Reloj(hrs=16, mins=15, segs=36, lat=7)
    r4 = Reloj(hrs=15, mins=0, segs=0, lat=5)
    r5 = Reloj(hrs=12, mins=40, segs=38, lat=10)
    i = 0
    relojes = [r1, r2, r3, r4, r5]

    s = Sincronizador(relojes)
    #s.start_cristian()
    s.start_berkeley()

    while i < 100:
        i += 1
        time.sleep(1)
        for r in relojes:
            print("Seconds {:d}:{:d}:{:d}".format(r.get_hrs(), r.get_mins(), r.get_segs()))
        print()


if __name__ == '__main__':
    main()

def abajo():
    d_all.lpf=500
    d_all.solo()
def arriba():
    d_all.lpf=0
    d_all.solo(0)
def abajoarriba(intervalo):
    abajo()
    Clock.future(intervalo, lambda: arriba())

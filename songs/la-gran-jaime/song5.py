# Code from Tomas Cajelo
# Taken from https://www.instagram.com/p/BzQe6qFnqzV/?utm_source=ig_web_copy_link

def cambio_de_etapa(f):
    d1.reset()
    m1.reset()
    b1.reset()
    v1.reset()
    v1.stop()
    m1.stop()
    f()
    print("CAMBIO DE PARTE")
Scale.default = "minor"
Root.default.set("B")
Clock.bpm=140
def intro():
    d2 >> play("--(--)-(----)--").sometimes("stutter")
    p1 >> ambi([(0,2,4),(6,8,10),(4,6,8),(5,7,9)], dur=8, oct=(5,4,4,6), chop=12, root=2.5, mix=2.6)
def verse():
    d1 >> play("x OXXO XO {kE}")
    d2 >> play("--[--]-[---]--").sometimes("stutter")
    t1 >> blip([0,1,2,4], dur=1/2, pan=(-1,1), delay=(0.5, 0, 1, 0.25), amp=0.5)
    p1 >> ambi([(0,2,4),(6,8,10),(4,6,8),(5,7,9)], dur=3, oct=(5,4,4,4), chop=12, room=2.5, mix=0.6)
    b1 >> dab([0,6,4,5], dur=8, sus=6, oct=[5,4,4,4], amp=1, chop=0, room=0.5, mix=0.75, shape=0)
def preChorus():
    t3 >> blip([0,1,2,4], dur=1/4, pan=[-1,1], delay=[0.5,0,1,0.25], amp=1.5, oct=(5,6,7,8), room=0.75, mix=2.5)
    d_all.stop()
    p1.stop()
    b1.stop()
def chorus():
    d3 >> play("X  x {O[0000]}  ")
    d4 >> play("s  [sss]")
    b3 >> jbass([5,6,7,2,6], dur=[4,4,4,2,2], oct=[4,4,4,5,4],shape=linvar([0.1,0.8],30), amp=0.25)
    b4 >> jbass([5,6,7,2,6], dur=[4,4,4,2,2], oct=[4,4,4,5,4])
    t3 >> blip([0,1,2,4],dur=1/4,pan=(-1,1), delay=(0.5, 0, 1, 0.25), amp=0.75, oct=(5,6,7,6), room=0.75, mix=0.5).sometimes("reverse").every(3,"stutter")
    d5 >> play("a", sample=[1,2,3], dur=PDur(3,8,[0.2]), amp=0.5)
def verse2():
    d3.stop()
    d4.stop()
    b3.stop()
    b4.stop()
    t3.stop()
    d5.stop()
    d1 >> play("X O X XO X O {kL}")
    d2 >> play("--(-)-( -)--").sometimes("stutter")
    t1 >> blip([0,1,2,0], dur=1/2, pan=(-1,1), delay=(0.5,0,1,0.25), amp=0.5)
    p1 >> ambi([(0,2,4),(6,8,10),(4,6,8),(5,7,9)], dur=8, oct=(5,4,4,4),chop=12, room=0.5, mix=0.6)
    p1 >> dub([0,6,4,2], dur=8, sus=6, oct=[3,4,4,4], amp=0.75, chop=0, room=0.5, mix=0.75, shape=0)
total = 32
aviso_tiempo_previo = 28
def proximo(etapa,tiempo,nombre):
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//4} beats para el {nombre}"),tiempo - aviso_tiempo_previo//4)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//2} beats para el {nombre}"),tiempo - aviso_tiempo_previo//2)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo} beats para el {nombre}"),tiempo - aviso_tiempo_previo)
    Clock.schedule(lambda : cambio_de_etapa(etapa), tiempo)


start = Clock.mod(16) - 0.1
Clock.schedule(intro, start)
# VERSO
proximo(verse, start + total,"verso")
# ESTRIBILLO
proximo(preChorus, start + total*2,"pre-estribillo")
# VERSO
proximo(chorus, start + total*3,"estribillo")
# ESTRIBILLO
proximo(verse2, start + total*5,"verso")
# VERSO
proximo(chorus, start + total*7,"estribillo")
# ESTRIBILLO
proximo(verse, start + total*9,"ultimo estribillo!!!")




def cambio_de_etapa(f):
    d1.reset()
    m1.reset()
    b1.reset()
    v1.reset()
    v1.stop()
    m1.stop()
    b2.stop()
    f()
    print("CAMBIO DE PARTE")
    
Scale.default = "minor"
Root.default.set("B")
Clock.bpm=90
def intro():
    m1 >> soprano(PWalk(8),dur=1,sus=2,amp=1,oct=4)
    d3 >> play("#",rate=-1/2,dur=8,amp=3)
    m2 >> gong(var([p2.pitch],4), dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)
def verse():
    b1 >> sawbass(var([0,1,-1],[12,2,2]),cut=0,sus=0.5, echo=0, echotime=1,decay=0.5,room=0.7, mix=1, amp=[4,2,2,5], dur=1/2,shape=var([0.2,0.3],8), oct=[6,5,5])
    d2 >> play('V-[sV]-').offbeat().sometimes('amen')
    d1 >> play('o|*3|', sample=2, dur=2, amp=4)
def prechorus():
    d1 >> play(" X",amp=17)
    d2 >> play("-",amp=10)
def chorus():    
    b1.reset()
    b1 >> bass(var([0,-1],[8,2]),dur=4,chop=var([8,16],5),amp=3)


d1 >> play('[bbbb] ',dur=1)


v1 >> charm(PWalk(5),amp=5,chop=2,scale=Scale.minorPentatonic)

v2 >> loop("v1",P[0:16],mix=0.6,room=0.9,amp=var([0],[4]))

v1 >> loop("o1",P[0:8],mix=0.8,room=0.9,amp=var([12,0],[4]))

m1 >> blip(PWalk(4),dur=1,amp=10)


notas = (PWalk(4))[:20]
voice(notas,dur=[1],lyrics="aa",file="o1",octave=6,scale=Scale.minorPentatonic)


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
proximo(prechorus, start + total*2,"pre-estribillo")
# VERSO
proximo(chorus, start + total*3,"estribillo")
# ESTRIBILLO
proximo(verse, start + total*5,"verso")
# VERSO
proximo(chorus, start + total*7,"estribillo")
# ESTRIBILLO
proximo(verse, start + total*9,"ultimo estribillo!!!")


p1 >> pluck()




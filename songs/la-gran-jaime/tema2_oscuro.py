#from .Extensions.Voice import voice
#notas = (PWalk(4))[:20]
#voice(notas,dur=[1],lyrics="aa",file="o1",octave=6,scale=Scale.minorPentatonic)

#notas = PWalk(3)[:18]
#voice(notas,dur=[2],lyrics="ab ra cada bra ",file="t3v2",octave=5,scale=Scale.minorPentatonic)

#notas = PWalk(3)[:18]
#voice(notas,dur=[2],lyrics="live coding",file="t3v3",octave=5,scale=Scale.minorPentatonic,lang="en")

#notas = PWalk(3)[:18]
#voice(notas,dur=[2],lyrics="colec tivo delaiv coders",file="t3v4",octave=5,scale=Scale.minorPentatonic)

def cambio_de_etapa(f):
    f()
    print("CAMBIO DE PARTE")    
total = 48
aviso_tiempo_previo = 28
def proximo(etapa,tiempo,nombre):
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//4} beats para el {nombre}"),tiempo - aviso_tiempo_previo//4)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//2} beats para el {nombre}"),tiempo - aviso_tiempo_previo//2)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo} beats para el {nombre}"),tiempo - aviso_tiempo_previo)
    Clock.schedule(lambda : cambio_de_etapa(etapa), tiempo)
Scale.default = "minor"
Root.default.set("B")
Clock.bpm=90
def intro():
    b1.stop()
    m1 >> soprano(PWalk(8),dur=1,sus=2,amp=0.5,oct=4)
    d3 >> play("#",rate=-1/2,dur=8,amp=1)
    m2 >> gong(var([p2.pitch],4), dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)
def verse1():
    b1 >> sawbass(var([0,1,-1],[12,2,2]),cut=0,sus=0.5, echo=0, echotime=1,decay=0.5,room=0.7, mix=1, amp=[1,0.5,0.5,1.5], dur=1/2,shape=var([0.2,0.3],8), oct=[6,5,5])
def verse2():
    d2 >> play('V-X-', amp=0.7).sometimes('amen')
    d1 >> play('o|*3|', sample=2, dur=2, amp=1)
def bridge():
    b1.solo()
def prechorus():
    d1.reset()
    d1 >> play(" X",amp=1)
    d2.reset()
    d2 >> play("-",amp=1)
    b1.amp=1.3
def chorus():    
    b1.reset()
    b1 >> bass(var([0,-1],[8,2]),dur=4,chop=var([8,16],5),amp=0.9, pan=[1,-1])
    
intro()

verse1()

verse2()

bridge()

prechorus()

chorus()

v1 >> loop("t3v3",P[0:16],amp=var([1.5],4),mix=0.0,room=0.0)

# Instrumentis
# bajo del coro con shape
b1 >> bass(var([0,-1],[8,2]),dur=4,chop=var([8,16],5),amp=0.8, pan=[1,-1], shape=0.2)

#bips del tema anterior
bb >> play('{[bb] b}{b }{[bb]bb }',dur=1/2, rate=1, amp=PRand(1))

#ambi cosmico # SIRENAAAAAA
y1 >> ambi(linvar([0,5],16), dur=1/8, cut=0, chop=0, room=0.6, mix=0.8, pan=linvar([-1,1]), amp=linvar([1,1.5,1.5,1]))

d1 >> play('o|*3|', sample=2, dur=2, amp=1)

v1 >> charm(PWalk(5),amp=2,chop=2,scale=Scale.minorPentatonic)

v2 >> loop("t3v1",P[0:16],mix=0.9,room=0.9,amp=var([1],[4]))

v1 >> loop("o1",P[0:8],mix=0.8,room=0.9,amp=var([1,0],[4]))

m1 >> blip(PWalk(4),dur=1,amp=1)

start = Clock.mod(16) - 0.1
Clock.schedule(intro, start)
proximo(verse1, start + total*1,"verso1")
proximo(verse2, start + total*2,"verso2")
proximo(bridge, start + total*3,"puente")
proximo(prechorus, start + total*3.5,"pre-estribillo")
proximo(chorus, start + total*4.5,"estribillo")

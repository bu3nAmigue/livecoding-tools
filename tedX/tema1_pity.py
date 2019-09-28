#########
# UTILS
#from .Extensions.Voice import voice

#letra1 = "música con computa doras "
#letra2 = "progra mando melo días "
#letra3 = "to dos los días "
#letra4 = "co deo en vivo "

#notas = (PWalk(10))[:20]
#voice(notas,dur=[1],lyrics=letra1+letra2+letra3+letra4,file="t2v2",octave=5,scale=Scale.minorPentatonic)

#letra1 = "on the flight programming "
#letra2 = "just in time programming ",

#notas = (PWalk(5))[:10]
#notas = [0,5,4,2]
#voice(notas,dur=[1],lyrics="la",file="t2v7",octave=6,scale=Scale.minor)

stopChoir()
d2.stop()
b2.chop=0
b2.sus=0

# VOCES
#intro
v2 >> loop("t2v2",P[0:4],dur=1,amp=var([2,0],4),mix=0.8,room=0.8,formant=[0])

#verso
v3 >> loop("t2v2",P[0:16],dur=PSum(4,4),amp=var([1],8),formant=[1])

#estribillo
v2 >> loop("t2v7",P[0:8],dur=PSum(1,1),amp=var([1],4),mix=0.9,room=0.9,formant=2)

v3 >> loop("t2v5",P[0:16],dur=PSum(9,4),amp=var([1,0],4),mix=0.9,room=0.9,formant=linvar([0,0]))


#vx.stop()

#INSTRUMENTIS

#intro
ps >> saw([0,2], dur=4, sus=3, oct=(5))

#verso
chords = [0,2,3,4]
duracion = 4

m1 >> gong(P+[chords]|P[chords],dur=[duracion/2]*4+[duracion/4]*4, amp=1, oct=(4,[5,6])).every(4,'shuffle').every(2, 'offadd',-1) + var([(0,2,4,6),1])

m2 >> piano(PWalk(4),dur=0.5,amp=1,scale=Scale.minorPentatonic)
#m1.stop()
#m2.stop()

#estribillo
a1 >> gong(PWalk(4),dur=duracion/4,amp=2,scale=Scale.minorPentatonic, sus=duracion/2)

#el buen quin
m2 >> quin(var(chords), oct=[4,5], dur=PDur(5,8), amp=1.5, hpf=linvar([300, 1000]), shape=0.5) + var([0,2,-1])
m2.stop()

#cierre
m1 >> piano(chords, dur=duracion, amp=[[1.5]*4+[0]*4]) + var([0,2,4])

#v2.solo()
#v3.stop()

#p1 >> play("o",rate=-0.5,dur=var([1,0.5,0.25,0.125,0.1],[4]),amp=6)
#p2 >> play("b",rate=[0.2,0.1,0.05],dur=4,amp=20)
#v1 >> loop("bomb",P[0:8],amp=10,rate=2)

# AGREGAR SAMPLE DE EXPLOSION

verso()

intro()

estribillo()

cierre()

def cambio_de_etapa(f):
    d1.reset()
    m1.reset()
    b1.reset()
    b2.reset()
    v1.reset()
    v1.stop()
    m1.stop()
    f()
    print("CAMBIO DE PARTE")
Scale.default = 'minor'
Clock.bpm = 90
def intro(duracion = 1):
    d1 >> play('<-><  K ><Xs  >', dur=duracion, amp=1)
    b1 >> dbass(var([0,2,3,4],4), dur=duracion,sus=0.5, amp=[0.6],oct=5)
def verso(duracion = 1):
    chords = P[0,2,3,4]
    b1 >> dbass(var(chords,4),dur=[duracion],sus=1)
    d1 >> play("{x*xb}",dur=duracion/4,amp=0.5)
def estribillo(duracion=1):
    chords = P[0,5,4,2]
    b1 >> dbass(var(chords,1),dur=duracion/2, sus=1,oct=5)
    d1 >> play("<V([sV][{[--]-bb-b}])><#  b>",dur=duracion/2, sample=[1,2,3])
def cierre(duracion=4):
    d1 >> play('[bbbb] ',dur=duracion)
    b1 >> dbass([0], dur=duracion, sus=duracion,amp=0.6)
total = 64
aviso_tiempo_previo = 32
def proximo(etapa,tiempo,nombre):
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//4} beats para el {nombre}"),tiempo - aviso_tiempo_previo//4)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//2} beats para el {nombre}"),tiempo - aviso_tiempo_previo//2)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo} beats para el {nombre}"),tiempo - aviso_tiempo_previo)
    Clock.schedule(lambda : cambio_de_etapa(etapa), tiempo)
    
#BOTON DE ENCENDIDO
start = Clock.mod(16) - 0.1
proximo(intro, start + total*0,"intro")
# VERSO
proximo(verso, start + total*1,"verso")
# ESTRIBILLO
proximo(estribillo, start + total*2,"estribillo")
# VERSO
proximo(verso, start + total*3,"verso")
# ESTRIBILLO
proximo(estribillo, start + total*4,"ultimo estribillo!!!")
# CIERRE
proximo(cierre, start + total*5,"cierre")

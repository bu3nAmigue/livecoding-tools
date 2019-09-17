
from .Extensions.Voice import voice

def cambio_de_etapa(f):
    d1.reset()
    m1.reset()
    b1.reset()
    v1.reset()
    v1.stop()
    m1.stop()
    f()
    print("CAMBIO DE PARTE")

letra1 = "música con computa doras "
letra2 = "progra mando melo días "
letra3 = "to dos los días "
letra4 = "co deo en vivo "
letra5 = "scriptear es vi da "
letra6 = "on the flight programming "
letra7 = "just in time programming "
letra8 = "and conversational programming "
letra9 = "programmers programming programs "
letra10 = "live coders expose and rewire the innards of software while it generates improvised music and visuals "
letra11 = "música por computa doras "

Scale.default = 'minor'
Clock.bpm = 90

def intro(duracion = 1):
    d1 >> play('<-><  K ><Xs  >', dur=duracion, amp=2)
    b1 >> dbass(var([0,2,3,4],4), dur=duracion,sus=0.5, amp=[0.9],oct=5)
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


print(Clock.now()%16)

#########
# UTILS
notas = (PWalk(4))[:20]
voice(notas,dur=[1],lyrics=letra5 + letra6 + letra7 + letra8,file="v6",octave=6,scale=Scale.minorPentatonic)

v1.reload()
v1 >> loop("v5",P[0:16],amp=var([1],4))

# Intro
intro(2)

v2 >> loop("v6",P[0:4],dur=1,amp=var([3,0],4),mix=0.8,room=0.8,formant=[0])

p5 >> saw([0,2,-1,-2], dur=2, sus=1, oct=(5,6))
p5.stop()


# Verso
chords = [0,2,3,4]
duracion = 4

m1 >> gong(P+[chords]|P[chords],dur=[duracion/2]*4+[duracion/4]*4, amp=4, oct=(4,[5,6])).every(4,'shuffle').every(2, 'offadd',-1) + var([(0,2,4,6),1])


m2.stop()

v3 >> loop("v2",P[8:12],dur=PSum(4,4),amp=var([1,0],8),formant=[1])

verso(2)

v3.solo()

verso(1)

v1.stop()

v1.stop()

m2 >> piano(PWalk(4),dur=2,amp=2,scale=Scale.minorPentatonic) + var([(0,4)])

v3.stop()


# Estribillo
chords = [0,2,3,4]
v2.solo()

estribillo(8)

m2 >> quin(var(chords),oct=5, dur=PDur(7,16), amp=1.5,hpf=linvar([300,1000]), shape=0.5).every(8,'reverse')

x3 >> saw(P+[chords], sus=1, dur=1)

p7 >> play('[####]', dur=duracion, amp=5)

p7.stop()

dur=1
p1 >> prueba([0,5,4,2],dur=dur,sus=dur/10,oct=5) + var([(0)])

x6 >> blip(0, decay=[0,1])

a1 >> gong(PWalk(4),dur=duracion/4,amp=4,scale=Scale.minorPentatonic, sus=duracion/2)

v1 >> loop("v6",P[0:8],dur=PSum(9,4),amp=var([4],4),mix=0.0,room=0.0,formant=linvar([0,0]))

v3 >> loop("v5",P[0:8],dur=PSum(1,1),amp=var([4],4),mix=0.0,room=0.0,formant=2)

v3.stop()

v2 >> loop("v6",P[0:32],dur=PSum(1,1),amp=var([8],4),formant=0,mix=0.0,room=0.0)

estribillo(8)

m2.stop()

v2.stop()

v2.stop()
v3.stop()


m2.stop()

# Final
v2.solo()

v2 >> loop("v6",P[0:32],amp=var([0,3],4),mix=0.0,room=0.0)

v2.amp = 3

cierre(1)

p7.stop()


m1.solo()

m1 >> piano(chords, dur=duracion, amp=[[1.5]*4+[0]*4]) + var([0,2,4])

m1.stop()

p1 >> play("o",rate=-0.5,dur=var([1,0.5,0.25,0.125,0.1],[4]),amp=6)

p2 >> play("b",rate=[0.2,0.1,0.05],dur=4,amp=20)

v1 >> loop("bomb",P[0:8],amp=10,rate=2)

# AGREGAR SAMPLE DE EXPLOSION

# INICIAR CANCION
total = 128
aviso_tiempo_previo = 32
def proximo(etapa,tiempo,nombre):
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//4} beats para el {nombre}"),tiempo - aviso_tiempo_previo//4)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//2} beats para el {nombre}"),tiempo - aviso_tiempo_previo//2)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo} beats para el {nombre}"),tiempo - aviso_tiempo_previo)
    Clock.schedule(lambda : cambio_de_etapa(etapa), tiempo)

start = Clock.mod(16) - 0.1
Clock.schedule(intro, start + total*0)
# VERSO
proximo(verso, start + total*1,"verso")
# ESTRIBILLO
proximo(estribillo, start + total*2,"estribillo")
# VERSO
proximo(verso, start + total*3,"verso")
# ESTRIBILLO
proximo(estribillo, start + total*4,"estribillo")
# VERSO
proximo(verso, start + total*5,"verso")
# ESTRIBILLO
proximo(estribillo, start + total*6,"ultimo estribillo!!!")
# CIERRE
proximo(cierre, start + total*7,"cierre")


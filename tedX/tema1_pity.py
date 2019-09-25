from .Extensions.Voice import voice

#########
# UTILS
notas = (PWalk(4))[:20]
voice(notas,dur=[1],lyrics=letra5 + letra6 + letra7 + letra8,file="v6",octave=6,scale=Scale.minorPentatonic)

chords = [0,2,3,4]
duracion = 4

# VOCES
#utils
v1.reload()
v1 >> loop("v6",P[0:16],amp=var([1],4))
#intro
v2 >> loop("v6",P[0:4],dur=1,amp=var([3,0],4),mix=0.8,room=0.8,formant=[0])
#verso
v3 >> loop("v2",P[0:16],dur=PSum(4,4),amp=var([1,0],8),formant=[1])
#estribillo
#el buen quin
m2 >> quin(var(chords), oct=[4,5], dur=PDur(5,8), amp=1.5, hpf=linvar([300, 1000]), shape=0.5) + var([0,2,-1])
m2.stop()

v3 >> loop("v5",P[0:8],dur=PSum(1,1),amp=var([4],4),mix=0.9,room=0.9,formant=2)

v2 >> loop("v1",P[0:16],dur=PSum(9,4),amp=var([4,0],4),mix=0.9,room=0.9,formant=linvar([0,0]))
#vx.stop()

#INSTRUMENTIS

#intro
ps >> saw([0,2], dur=4, sus=3, oct=(5))
#verso
m1 >> gong(P+[chords]|P[chords],dur=[duracion/2]*4+[duracion/4]*4, amp=4, oct=(4,[5,6])).every(4,'shuffle').every(2, 'offadd',-1) + var([(0,2,4,6),1])

m2 >> piano(PWalk(4),dur=0.5,amp=1,scale=Scale.minorPentatonic)
#m1.stop()
#m2.stop()

# estribillo
a1 >> gong(PWalk(4),dur=duracion/4,amp=4,scale=Scale.minorPentatonic, sus=duracion/2)

#cierre
m1 >> piano(chords, dur=duracion, amp=[[1.5]*4+[0]*4]) + var([0,2,4])

#v2.solo()
#v3.stop()

#p1 >> play("o",rate=-0.5,dur=var([1,0.5,0.25,0.125,0.1],[4]),amp=6)
#p2 >> play("b",rate=[0.2,0.1,0.05],dur=4,amp=20)
#v1 >> loop("bomb",P[0:8],amp=10,rate=2)

# AGREGAR SAMPLE DE EXPLOSION

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
# INICIAR CANCION
total = 96
aviso_tiempo_previo = 32
def proximo(etapa,tiempo,nombre):
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//4} beats para el {nombre}"),tiempo - aviso_tiempo_previo//4)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//2} beats para el {nombre}"),tiempo - aviso_tiempo_previo//2)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo} beats para el {nombre}"),tiempo - aviso_tiempo_previo)
    Clock.schedule(lambda : cambio_de_etapa(etapa), tiempo)
    

#BOTON DE ENCENDIDO
start = Clock.mod(16) - 0.1
Clock.schedule(intro, start + total*0)
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

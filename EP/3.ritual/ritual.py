Scale.default = "minor"
Root.default.set("B")
Clock.bpm=100

def note2index(note):
    scale = list(Scale.default)
    return scale[note]
def play2notes(notas,sample="b",dur=1,ritmo=8,oct=0,player=p1):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    player >> play(sample,dur=var(ritmo,dur), rate=var(rates,dur),amp=0.5,sample=2)

### ABAJO/ARRIBA

def abajo():
    d_all.lpf=500
    d_all.solo()
def arriba():
    d_all.lpf=0
    d_all.solo(0)
def abajoarriba(intervalo):
    abajo()
    Clock.future(intervalo, lambda: arriba())

# Voces

from .Extensions.Voice import voice

voice([0,4,3,2,3,0],dur=[1],lyrics="Tec Flow",file="o2",octave=5,scale=Scale.minorPentatonic)

notas = PWalk(4)[:16]
voice(notas,dur=[1],lyrics="des mi ti fi can do da ta",file="o1",octave=6,scale=Scale.minorPentatonic)

v2.reload()
v2 >> loop("o2",P[0:16])

v1.reload()
v1 >> loop("o1",P[0:16])

####################
##### CANCION ######
####################

def intro1():
    m2 >> gong(var([p2.pitch],4), dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)    
def intro2():
    d2 >> play('w' ,dur=PSum([1,6],4), rate=1/4) 
def intro3():
    d3 >> play('K', dur=2, sample=3)
def verso1():
    m2.stop()
    play2notes([0],"Q",dur=[4],ritmo=[4],oct=-2,player=q1)
def verso2():
    pass
def verso3():
    v2 >> loop("o1",P[2:6], lpf=0, rate=[2,0.5], drive=0.3, echo=0, amp=var([0.5,0],4),dur=var([2,4,1],4))
    p1 >> piano(var([0,2],4), drive=0.3, dur=PSum(7,4),amp=0.7,pan=PWhite(-1,1)).every(4,'stutter',2,dur=1) + var([0,2],8)
def puenteA1():
    d2.solo()
    d3 >> play('---[--]',sample=2,dur=0.5,amp=1)
    c1 >> glass([0],oct=4)
def puenteA2():
    y1 >> ambi(linvar([0,5],16), dur=1/8, cut=0, chop=0, room=0.6, mix=0.8, pan=linvar([-1,1]), amp=linvar([1,1.5,1.5,1]))
def cierre1():
    pass
def cierre2():
    Clock.clear()

verso1()

def suma(v,n):
    return [note2index((a + n)%7) for a in v]

def arreglo_coral(notas,sample,dur=1,d=0,h=1):
    x1 >> loop(sample, P[d:h], pshift=var(suma(notas,0),dur))
    x2 >> loop(sample, P[d:h], pshift=var(suma(notas,2),dur), delay=0)
    x3 >> loop(sample, P[d:h], pshift=var(suma(notas,4),dur), delay=0)
    
print(note2index(5))

print(Scale.minor)

Scale.default='minor'
arreglo_coral([0,5,4,2],"perro_tuned")

v1 >> loop('perro_tuned', P[0:1], dur=1,rate=1,formant=0, pshift=[0,1,2,3,4,3,2,1], slide=0.0)

v2 >> loop('perro_tuned', P[0:1], dur=1,rate=1,formant=0, pshift=[1,0,1,2,3,4,3,2], delay=0.0)

v2.stop()

v2 >> loop('c2', P[0:16], dur=1,rate=2,formant=2)

v3 >> loop('c1', P[0:16], dur=1,rate=2,formant=2)

v4 >> loop('t1v1', P[0:16], dur=1,rate=1,formant=0)



puenteA1()

print(SynthDefs)

a1.reset() >> glass([0],oct=4)



play2notes([0],"1234",dur=[4],ritmo=[2],oct=-1,player=p3)

a4 >> pluck()

abajo()

d3.reset() >> play('K', dur=2, sample=3)

d3.dur=PSum(5,4)
d3.rate=var([1,2],4)

verso3()

puenteA2()

arriba()

d1 >> play('(X )', sample=6,dur=0.5)

### ESTO DONDE LO METEMOS?

cc >> combs(linvar([0,2],8), amp=0.1, room=0.5).spread()

m2 >> gong(var([p2.pitch],4), dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)

### CANCION ###

intro = [intro1, intro2,intro3]
verso = [verso1,verso2,verso3]
puenteA = [puenteA1,puenteA2]
cierre = [cierre1, cierre2]
cancion = intro + verso + puenteA + verso + puenteA + verso + puenteA + verso + cierre


### EFECTOS #####

def efecto1():
    p1 >> piano([0,0,5,5,4,2], drive=0.5, dur=PSum(4,4),amp=0.4,pan=PWhite(-1,1))
def efecto2():
    d3.reset() >> play('K', dur=2, sample=3)
    d3.dur=PSum(5,4)
    d3.rate=var([1,2],4)
efectos = {
    "verso3": {"efecto": efecto1, "restantes": 1},
    "verso1": {"efecto": efecto2, "restantes": 2}
}

### RESET ###

def reset():
    pass

### REPRODUCTOR ###

def countRepetitions(fname,cancion):
    fnames = list(map(lambda x : x.__name__,cancion))
    return fnames.count(fname)
def reproducir(cancion,efectos,reset,start):
    reset()
    if len(cancion) > 0:
        cancion[0]()
        fname = cancion[0].__name__
        if fname in efectos and countRepetitions(fname,cancion) == efectos[fname]["restantes"]:
            efectos[fname]["efecto"]()
        Clock.schedule(lambda : reproducir(cancion[1:],efectos,reset,start+8),start + 8)

start = Clock.mod(8) - 0.1
Clock.schedule(lambda : reproducir(cancion,efectos,reset,start), start)

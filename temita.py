Root.default = -3
Scale.default = 'minor'

def verso():
    b1 >> pluck([0,-2,4,3],dur=4,sus=2,oct=4)
    p1 >> pluck([0,0,4,2,0,0,5,2,4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])

def estribillo():
    b1 >> pluck([2,-1,0,-2],dur=4,sus=2,oct=4)
    n = 6
    p1 >> pluck([(2,4,6)]*n+[(-1,1,3)]*n+[(0,2,4)]*n+[5,4,3,2],dur=list(PSum(n,4)[:n*3])+[1]*4,amp=[1,1,1,1]*3 + [1,1,1,1])
    d1 >> play("X ")
    d2 >> play("-")

def puente():
    b1 >> pluck([0],dur=4,sus=2,oct=4)
    p1 >> pluck([(0,2,4)]*4,dur=2,amp=1)

start = Clock.mod(32) - 0.1
Clock.schedule(verso, start)
Clock.schedule(puente, start+32)
Clock.schedule(estribillo, start+32+16)

### Version 2 ### 

Root.default = -3
Scale.default = 'minor'


def intro():
    p1 >> piano([0,0,4,2,0,0,5,2,4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
def verso():
    b1 >> ambi([0,-2,4,3],dur=4,sus=3,oct=5)
    p1 >> piano([0,0,4,2,0,0,5,2,4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
    d2 >> play("-")
def estribillo():
    b1 >> jbass([2,-1,0,-2],dur=4,sus=2,oct=6,amp=1,chop=1)
    n = 6
    p1 >> piano([(2,4,6)]*n+[(-1,1,3)]*n+[(0,2,4)]*n+[5,4,3,2],dur=list(PSum(n,4)[:n*3])+[1]*4,amp=[1,1,1,1]*3 + [1,1,1,1])
    d1 >> play("X ")
def estribillo_loco():
def puente():
    pt >> play('#', dur=8,sus=4, rate=-1/2)
    b1 >> ambi([0],dur=4,sus=2,oct=6)
    p1 >> piano([(0,2,4)]*4,dur=2,amp=1)

print(SynthDefs)



acordes = [(2,4,6),(-1,1,3),(0,2,4)]
escalera = P[5,4,3,2]

# intro
p1 >> piano([0,0,4,2,0,0,5,2,4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])

d1 >> play("X ",amp=2)

# verso
b1 >> ambi([0,-2,4,3],dur=4,sus=3,oct=5)
p1 >> space([0,0,4,2,0,0,5,2,4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
d2 >> play("-")

# puente
p1.solo()
pt >> play('#', dur=8,sus=4, rate=-1/2)
b1 >> ambi([0],dur=4,sus=2,oct=6)
p1 >> space([(0,2,4)]*4,dur=2,amp=1)

# estribillo
d1 >> play("X ",amp=4)
play2notes([2,-1,0,-2]," Q",dur=4,ritmo=[0.5],oct=0)
n = 5
p1 >> quin([(2,4,6)]*n+[(-1,1,3)]*n+[(0,2,4)]*n+[5,4,3,2],dur=list(PSum(n,4)[:n*3])+[1]*4,amp=[1,1,1,1]*3 + [1,1,1,1])
Clock.future(16, lambda: guitarra())

# puente2

n=3
p1 >> space([(2,4,6)]*n+[(-1,1,3)]*n+[(0,2,4)]*n+[5,4,3,2],dur=list(PSum(n,4)[:n*3])+[1]*4,amp=[1,1,1,1]*3 + [1,1,1,1])
p1.solo()
#b1 >> ambi([0,-2,4,3],dur=4,sus=3,oct=5)
d2 >> play("-")
d1 >> play("X ",amp=4)

# verso
b1 >> ambi([0,-2,4,3],dur=4,sus=3,oct=5)
p1 >> space([0,0,4,2,0,0,5,2,4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
d2 >> play("-")

guitarra()

def guitarra(dur=1/2):
    gg >> sitar(var([acordes[0:3]],4)+var([0,-2],4), dur=dur, amp=1, cut=0.8).every([1], 'stutter',2)
    d1 >> play("(X[sX])([--][-X])(- ))",amp=4,dur=dur*2)


### Mas codigo por si acaso ###




p2 >> jbass([2,-1,0,-2],dur=4,sus=2,oct=6,amp=1,chop=1)

n = 6

p1 >> saw([(2,4,6)]*n+[(-1,1,3)]*n+[(0,2,4)]*n+[5,4,3,2],dur=list(PSum(n,4)[:n*3])+[1]*4,amp=[1,1,1,1]*3 + [1,1,1,1])
p1.oct=var([5,6],4)
p1.formant=3
p1.cut=0.8


p1.stop()

b1.stop()

d1 >> play("X ",amp=5)
play2notes([2,-1,0,-2]," Q [O123]",dur=4,ritmo=[1],oct=-2)

p2.stop()

b1 >> jbass(var([2,-1,0,-2],4),dur=4,sus=b1.dur/2,oct=6,amp=2,cut=0.5)

print(Clock)

gg >> space(var([acordes[0:3]],4)+var([0,-2],4), dur=1/2, amp=1, cut=0.7, oct=[4,4,5,6]).every([1,2], 'stutter',2)

gg.stop()

n = 6
p1 >> space([(2,4,6)]*n+[(-1,1,3)]*n+[(0,2,4)]*n+[5,4,3,2],dur=list(PSum(n,4)[:n*3])+[1]*4,amp=[1,1,1,1]*3 + [1,1,1,1], cut=2)

p1.stop()

pt >> play('#', dur=8,sus=4, rate=-1/2)

d1.stop()

d1 >> play("X ",sample=2)

## guitarra que se aprendio el tema


print(SynthDefs)


gg.stop()

zz >> blip(escalera, dur=1/2, oct=(5,6), shape=0.3)


verso()

p1 >> jbass([0,2,3,4],dur=[4],oct=1)

estribillo()

start = Clock.mod(32) - 0.1
Clock.schedule(intro, start)
Clock.schedule(verso, start+32)
Clock.schedule(puente, start+64)
Clock.schedule(estribillo, start+64+16)
Clock.schedule(estribillo_loco, start+64+32)

def note2index(note):
    scale = list(Scale.default)
    return scale[note]

def sample2notes(notas,sample="b",dur=1,oct=0):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    p1 >> loop(sample,dur=var(dur,4), rate=var(rates,dur),amp=1)

def play2notes(notas,sample="b",dur=1,ritmo=8,oct=0):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    p2 >> play(sample,dur=var(ritmo,dur), rate=var(rates,dur),amp=0.5,sample=2)

Scale.default='minorPentatonic'
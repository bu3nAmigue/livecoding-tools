def note2index(note):
    scale = list(Scale.default)
    return scale[note]

def sample2notes(notas,sample="b",dur=1):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,nota/12))
    p1 >> loop(sample,dur=dur, rate=var(rates,dur),amp=1)
    
def play2notes(notas,sample="b",dur=1):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,nota/12))
    p2 >> play(sample,dur=var(dur,8), rate=var(rates,dur),amp=1,sample=2)

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
Root.default.set("C")
Clock.bpm=120

def intro():
    d1 >>play("-")
def verse():
    p1.echo=0
    p2.formant=0
    p2.room=0.0
    p2.mix=0.0
    p2.chop=0
    p2.amp=1
    p1.striate=0
    z1 >> play('/', dur=4, sample=1, lpf=linvar([1000,8000],8+PRand(8)),bend=0, amp=[PRand(1),1])
    d3.reset() >> play('x( x)(-{[-x]--}) ',sample=4, dur=1).often('stutter',4)
def preChorus():
    d1 >> play('-', sample=2, dur=1, pan=0)
    d2 >> play('X X ', sample=3, dur=1,amp=3)
def chorus():
    play2notes([0],"Q",[2])
def preChorus2():
    d1.solo()
    d1 >> play('-', sample=2, dur=1, pan=0)
    d2 >> play('X X ', sample=3, dur=1,amp=3)
def verse2():
    play2notes([0,5,4,2],"Q",[1,0.5,0.25,0.125])
    v3.reset() >> blip(var([[0,5,4,2],[PRand(3)+2,PRand(3)+3,4+PRand(1),7]],[1]),dur=1, chop=4,speard=[-1,1], echo=(0.5,0.75), shape=0.7, oct=4+PRand(1), amp=[1,2,1,0]) + var([0,1,2],PRand(4))


play2notes([0,5,4,2],"Q",[1,0.5,0.25,0.125])


total = 32
aviso_tiempo_previo = 28
def proximo(etapa,tiempo,nombre):
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//4} beats para el {nombre}"),tiempo - aviso_tiempo_previo//4)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//2} beats para el {nombre}"),tiempo - aviso_tiempo_previo//2)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo} beats para el {nombre}"),tiempo - aviso_tiempo_previo)
    Clock.schedule(lambda : cambio_de_etapa(etapa), tiempo)


start = Clock.mod(32) - 0.1
Clock.schedule(intro, start)
# VERSO
proximo(verse, start + total,"verso")
# ESTRIBILLO
proximo(preChorus, start + total*2,"pre-estribillo")
# VERSO
proximo(chorus, start + total*3,"estribillo")
# ESTRIBILLO
proximo(verse2, start + total*4,"verso")
# VERSO
proximo(preChorus2, start + total*5,"pre-estribillo")
# VERSO
proximo(chorus, start + total*6,"estribillo")
# ESTRIBILLO
proximo(verse, start + total*7,"ultimo estribillo!!!")












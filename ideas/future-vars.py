Scale.default='minorPentatonic'

base1=var([1,2,3,4],PRand(4))
base2=var([0,1,2],[8,2,2])
def melo1():
    x3 >> saw(base1, dur=1/4, cut=0.7, oct=[4,5,6]) + var([0,1,-2],4)
    x1.dur=1/2
    print('Va la melodia segunda')

def melo2():
    x3 >> saw(base2, dur=1/4, cut=0.7, oct=[4,5,6]) + var([0,1,-2],4)
    x1.dur=1/4
    print('Va la melodia primera')


def intro():
    x1 >> sawbass(var([base1, base2],32), dur=1/4, shape=0.15, hpf=linvar([100,500],4))
def verse():
    x2 >> play('x-o(-[--] -)', sample=2, lpf=2000)
    melo1()    
def preChorus():
    x2 >> play('x-o(-[--] -)', sample=2, lpf=2000)
    x2.solo()
def chorus():
    melo2()    
def preChorus2():
    x2 >> play('x-o(-[--] -)', sample=2, lpf=2000)
    x2.solo()
def verse2():
    melo2()    


def cambio_de_etapa(f):
    d1.reset()
    m1.reset()
    b1.reset()
    v1.reset()
    v1.stop()
    m1.stop()
    f()
    print("CAMBIO DE PARTE")

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

def note2index(note):
    scale = list(Scale.default)
    return scale[note]

def play2notes(notas,sample="b",dur=1):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,nota/12))
    p2 >> play(sample,dur=var(dur,8), rate=var(rates,dur),amp=1,sample=2)

play2notes([0],"X",[0.5])
b1 >> bass(base2,chop=4,amp=2)


d1 >> play("X ",sample=2,amp=8)

p2.stop()

m1.stop()

m1 >> ambi(PWalk(),dur=PSum(8,4), amp=0, mix=0.9, room=0.9, scale=Scale.minorPentatonic)

k1.solo()
          
k1 >> blip(P[0,5,2+PRand(2),6].every(4, 'rotate',1), dur=P[1/2, 1/4, rest(1/4)]/linvar([1,4],4),sus=4,atk=0.6, formant=linvar([(0,1),(2,3)],8), slide=3, slidedelay=0.5, oct=[(4,5),5,(5,6)]).every([1,2,3], 'stutter', 2, oct=6, dur=1)

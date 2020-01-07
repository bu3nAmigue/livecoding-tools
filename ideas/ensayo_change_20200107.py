
def changeDur(rate,group=d_all):
    for i in range(len(group)):
        if (not group.players[i].synthdef is None) and (group.players[i].name in list(map(lambda x:x.name,Clock.playing))):
            try:
                print("modifico a",group.players[i])
                group.players[i].dur = float(group.players[i].dur)*rate
            except:
                print("ERROR")
                print(group.players[i].dur)
                print(help(group.players[i].dur))

def changeAmp(rate, group=d_all):
    for i in range(len(group)):
        if (not group.players[i].synthdef is None) and (group.players[i].name in list(map(lambda x:x.name,Clock.playing))):
            try:
                print("modifico a",group.players[i])
                group.players[i].amp = float(group.players[i].amp)*rate
            except:
                print("ERROR")
                print(group.players[i].amp)
                print(help(group.players[i].amp))


def abajo():
    d_all.lpf=500
    d_all.solo()
def arriba():
    d_all.lpf=0
    d_all.solo(0)
def abajoarriba(intervalo):
    abajo()
    Clock.future(intervalo, lambda: arriba())


d1 >> play("x")

changeDur(2) # Mas lento

changeDur(0.5) # Mas rapido

d2 >> play(' -')
d3 >> play('G')

d1.solo(0)

.stop()

print(Clock.playing[0].synthdef)

print(Clock.__dict__)



print(d_all.players[1].__dict__)






up()

down()

d1 >> play("X x ",dur=4)
d2 >> play("-*+",dur=1)
d3 >> play(" o",dur=2)

Scale.default='phrygian';Clock.bpm=125

change(2)

p2.solo(0)

d1 >> play('R', dur=PDur([3,1,4,1],8), pshift=P[0,3,5].every(2, 'rotate'), sample=2,oct=[5,5,6], lpf=linvar([5000,777],8), room=0.5, mix=linvar([2,0,0],[16,16,16],start=now))

d3 >> play('r(|r3|[--*-]--)',dur=PDur([3,5,3,7],8),pshift=P[2,4,6,-3].every(2, 'rotate'))

d4 >> play('  (|*1|)( -)', pshift=8,dur=0.5)

c1 >> play('*',dur=1)

d6 >> play('Q',dur=4, drive=0.0, rate=var([0.5]),pshift=[0])

d6.stop()

Scale.default = Scale.minor

change(0.5)

d7 >> play(' x', sample=4, echo=(0,0.5))


z1 >> pluck([var([0,2,4],4),[3,[5,7]]],dur=PDur([3,3,1,2],6),drive=0.1,,oct=[(4,5),(4,5),(5,6),(6,7)]) + var([0,1,-2,-4],[8,4,2,2])

b2 >> dirt(var([0,-1],4),dur=4, lpf=777, drive=0.2)

play2notes([0],"Q",4,4,oct=-1,player=d6)


d6.amp=0.2

change(2)

changeAmp(2)



def note2index(note):
    scale = list(Scale.default)
    return scale[note]
    
def play2notes(notas,sample="b",dur=1,ritmo=8,oct=0,player=p1):
    rates = []
    for nota in list(notas):
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    player >> play(sample,dur=var(ritmo,dur), rate=var(rates,dur),amp=0.5,sample=2)

def sample2notes(notas,sample="b",dur=1,oct=0,player=p1):
    rates = []
    for nota in list(notas):
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    player >> loop(sample,dur=var(dur,4), rate=var(rates,dur),amp=1)


sample2notes([0,7,3,2,5],"<{w[ww]}><(k[sk])><{[--][-*]}>",string_to_durs('ELPITYVIEJA', 1/4, 1))

d1 >> play("X ",amp=5)

play2notes([2,-1,0,-2],"Q",dur=4,ritmo=[1],oct=-2,player=d6)


p2.solo(0)

change(0.5)

b2.stop()

b1 >> bass(var([0],4),dur=PSum(6,4),lfo=100)

d5 >> play("X ",sample=2)

p1 >> loop('risa1', P[0:32], pshift=[0], dur=1,chop=4, formant=var([2,3,5,0,10],16), amp=var([0.5,0],[8]))

p2 >> loop('risa2', P[16:32], pshift=[0,2,3,4], dur=1, amp=var([0.5],[4,12]))


p2.stop()






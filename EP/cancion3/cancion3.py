
def note2index(note):
    scale = list(Scale.default)
    return scale[note]
def sample2notes(notas,sample="b",dur=1,oct=0):
    rates = []
    for nota in list(notas):
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    p1 >> loop(sample,dur=var(dur,4), rate=var(rates,dur),amp=1)
def play2notes(notas,sample="b",dur=1,ritmo=8,oct=0,player=p1):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    player >> play(sample,dur=var(ritmo,dur), rate=var(rates,dur),amp=0.5,sample=2)


# Parte picante

p1 >> piano([0,5,4,2], drive=0.5, dur=var([2],8),amp=0.7,pan=PWhite(-1,1))

Group(d2,v1).solo()

v1.solo()




p1.stop()

cc >> combs(linvar([0,2],8), amp=0.1, room=0.5).spread()

print(SynthDefs)

d2 >> play('w' ,dur=var([2,0.5],[6,2]), rate=1/4)

d1 >> play('(X|k0|) ', sample=6, dur=0.5)

play2notes([0],"Q",dur=[4],ritmo=[1],oct=-1,player=q1)



play2notes([0],"1234",dur=[4],ritmo=[4],oct=-1,player=p3)

a1 >> glass(oct=4)

p1.stop()

# Pasajes

p1.solo()
d1 >> play('X ', sample=6,dur=0.5)

# Parte tranca

b1.reset() >> bass(var([0,-1],[8,2]),dur=4,chop=var([8,16],5),amp=0.9, pan=[1,-1],shape=0.3)

c2 >> blip([var([0,2],4),4,5,7], dur=PDur(5,8)*2).every(8,'stutter',4,dur=1, oct=6, pan=[-1,1]).every(6,'offadd',4) + var([0,2],8)

c3 >> ambi(linvar([0,1],8), glide=[7,-7,4,4], dur=v1, oct=5)

m1 >> space(var([0,2,3,4],8),oct=4) + var([(0,2,4)])

v1 >> charm(PWalk(5),amp=2,chop=[4,2],scale=Scale.minorPentatonic)

v2 >> ambi(v1.pitch.accompany(), dur=4)


v1.solo()

##### COSAS ####


d1.reset()
d1 >> play(" X",amp=1)
d2.reset()
d2 >> play("-",amp=1)
b1.amp=1.3

b1.stop()

y1 >> ambi(linvar([0,5],16), dur=1/8, cut=0, chop=0, room=0.6, mix=0.8, pan=linvar([-1,1]), amp=linvar([1,1.5,1.5,1]))

b1.reset() >> bass(var([0,-1],[8,2]),dur=4,chop=var([8,16],5),amp=0.9, pan=[1,-1],shape=0.3)


c1 >> gong(var([0,2],4), oct=6, dur=0.5, amp=3) + (0,2)

c2 >> blip([var([0,2],4),4,6,7], dur=PDur(5,8)*2).every(8,'stutter',4,dur=1, oct=6, pan=[-1,1]) + var([0,2],8)

c3 >> charm(linvar([0,1],8), dur=1)


b1.stop()

d1 >> play('o|*3|', sample=2, dur=2, amp=1)



m1 >> blip(PWalk(4),dur=1,amp=1)


print(SynthDefs)

v1 >> ambi(dur=8)


Scale.default = "minor"
Root.default.set("B")
Clock.bpm=90

m1 >> soprano(PWalk(8),dur=1,sus=2,amp=0.5,oct=4)
d3 >> play("#",rate=-1/2,dur=8,amp=1)
m2 >> gong(var([p2.pitch],4), dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)

b1 >> sawbass(var([0,1,-1],[12,2,2]),cut=0,sus=0.5, echo=0, echotime=1,decay=0.5,room=0.7, mix=1, amp=[1,0.5,0.5,1.5], dur=1/2,shape=var([0.2,0.3],8), oct=[6,5,5])

d2 >> play('V-X-', amp=0.7).sometimes('amen')
d1 >> play('o|*3|', sample=2, dur=2, amp=1)




v1.stop()

v1 >> sillyVoice([PWalk(4)],dur=PSum(4,4), sus=1)


d3 >> play('w' ,dur=2, rate=1/4)


v1.stop()

print(SynthDefs)

# COSO QUE SIGUE

d1 >> play("(XO) ",sample=2,amp=1)


d2 >> play("-")

v1 >> bass(PWalk(4),oct=5,chop=3,sus=2,dur=[4],scale=Scale.minorPentatonic)

v1.stop()

d3 >> play("1234",dur=4)

d1.stop()

d1 >> play("O", dur = var([1,1/2,1/4,1/8], [4,4,4,inf],start=now))

p2.stop()


# COSO MATRIX

def progresion_matriz(acorde,efectos_matriz):
    original = acorde
    transformacion = []
    efectos_lista = []
    for efecto in efectos_matriz:
        for nota in efecto:
            efectos_lista += [nota]    
    acorde_lista = acorde * len(efectos_matriz)
    transformacion = Pattern(acorde_lista) + Pattern(efectos_lista)
    print(f'Armando progresion {transformacion}')
    return transformacion
    
Scale.default='minor'

progresion = [0,0,0,0,-13]
efectos_matriz = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
p1.reset() >> piano(progresion_matriz(progresion, efectos_matriz), dur=P[1,1,1,1,rest(2)]*2,echo=0, glide=[-5,-2,0], glidedelay=[0.5,0], chop=0,oct=5, amp=1)






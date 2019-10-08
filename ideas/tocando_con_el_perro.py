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
    p2 >> play(sample,dur=dur, rate=var(rates,dur),amp=1,sample=2)

v1 >> loop("perro_tuned",P[0:16])

v1 >> loop("perro",P[0:16])

v1.stop()

Scale.default = 'minor'

v2.stop()

v3.reset() >> blip(var([[0,5,4,2],[PRand(3)+2,PRand(3)+3,4+PRand(1),7]],[1]),dur=1, chop=4,speard=[-1,1], echo=(0.5,0.75), shape=0.7, oct=4+PRand(1), amp=[1,2,1,0]) + var([0,1,2],PRand(4))

v2.stop()

sample2notes([0],"perro",[1])

sample2notes([0,5,4,2],"c1",[1])

play2notes([0,5,4,2],"Q",[1])

play2notes([0,5,4,2],"Q",1)

p2.amp=3

play2notes([0],"Q",1)

d1 >> play('-{ [---][--]-r}', sample=2, dur=var([1,1/2],PRand(1)), pan=-1+PRand(2))

d2 >> play('X X ', sample=2, dur=0.5,amp=3)

d1.stop()

p1.echo=0
p2.formant=0
p2.room=0.0
p2.mix=0.0
p2.chop=0
p2.amp=1
p1.striate=0

d1 >> play('x',amp=0)

d3.reset() >> play('x( x)(-{[-x]--}) ',sample=4, dur=1).often('stutter',4)


z1 >> play('/', dur=4, sample=1, lpf=linvar([1000,8000],8+PRand(8)),bend=0, amp=[PRand(1),1])










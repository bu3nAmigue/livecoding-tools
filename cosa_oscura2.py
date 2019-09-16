


v1.stop()

from .Extensions.Voice import voice
notas = (PWalk(4))[:10]
voice([0,2,3,4],dur=[1],lyrics="hola",file="v1",octave=6,scale=Scale.wholeTone)

v2 >> loop("v6",P[0:8],dur=PSum(4,4),amp=var([7],8),mix=0.0,room=0.0,formant=0)

v2.reload()
v2 >> loop("v1",P[0:8],amp=var([7,0],8),dur=PSum(4,4),mix=0.0,room=0.0,formant=0)

m2 >> soprano(PWalk(20),dur=1,sus=3)

Scale.default = Scale.wholeTone

m1 >> soprano(PWalk(8),dur=1,sus=2,amp=1,oct=4)

d4 >> loop("bomb",P[0:4],amp=30)


m1 >> sawbass([0],dur=4,sus=0.5,amp=[0,12])

d5.stop()

d1.stop()


d3 >> play("#",rate=-1/2,dur=8,amp=3)

v1 >> loop("v1",P[0:1])

m1 >> play("+*", dur=PDur(,4),rate=PRand(10),amp=2)

d2 >> play("-",amp=4,dur=PSum(7,4))

d2.stop()


d1 >> pluck()

Scale.default=Scale.minor


m1.stop()

d5 >> play("X ",amp=5,dur=0.125)
d1 >> prophet(var([0,[1,-2]],1),dur=0.125,amp=8) + var([(0)])

print(SynthDefs)

p2 >> charm(P[-3,[1,-2],0], shape=linvar([0.2,0.6],[8,4,2,2]), dur=PDur(8,8), oct=[3,4,(5,6)], room=0.7, mix=0.7, echo=1, echotime=1, amp=linvar([2,0],4), hpf=linvar([200,2002],8)) + var([-1,0,-1,-2])
o1 >> sawbass(P[0,5,7,3].every(4, 'rotate'),oct=5, dur=[1,1/2], amp=2) + linvar([0,2],4)
o1.stop()
o3 >> gong(p2.pitch, dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)

o7 >> space([0,2], dur=[8,4,4,2,2], hpf=linvar([400,4000],16), amp=4)

o6.stop()
p5.stop()

o6 >> play('-- [-----*-]', amp=2, dur=1/32)





p5 >> play('< >', amp=2, dur=1)
p5.stop()





o1.stop()

o2 >> play('/', dur=4)
o2.stop()

p3 >> play('G{ K}', rate=PRand(4), dur=1/2, sample=PRand(4))
p3.stop()

o4 >> play('G', dur=4, chop=8, rate=1/4)



p5.stop()

p4 >> play('< X><(-[--]) ><   >', sample=PRand(5))

p4.stop()

print(Scales.names())


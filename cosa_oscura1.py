


v1.stop()

from .Extensions.Voice import voice
notas = (PWalk(4))[:10]
voice([0,2,3,4],dur=[1],lyrics="música",file="v1",octave=6,scale=Scale.wholeTone)

v1.stop()

v2 >> loop("v6",P[0:2],dur=PSum(4,4),amp=var([2],8),mix=0.0,room=0.0,formant=0)

m1 >> sawbass([0],dur=PSum(1,4),sus=1,amp=6)

v1.reload()
v1 >> loop("v1",P[0:8],amp=var([3,0],8),dur=PSum(4,4),mix=0.0,room=0.0,formant=0)

v1.stop()

d5.stop()



m2 >> soprano()

m2.stop()

Scale.default = Scale.wholeTone

m1 >> soprano(PWalk(8),dur=4,sus=2,amp=1.2,oct=4)

d5.stop()

d5 >> play("X",rate=PRand(4),dur=PSum(8,4))

d3 >> play("#",rate=-1/2,dur=8)


v1 >> loop("v1",P[0:1])

m1.stop()

m1 >> play("+*", dur=PDur(7,4),rate=PRand(10),amp=2)

d2 >> play("-")

d2.stop()

d2 >> play("KaX",sample=PRand(2))

d1 >> pluck()

Scale.default=Scale.minor


m1.stop()

d1 >> prophet([0,[1,-2]],amp=1.4) + var([(0,2,4)])

print(SynthDefs)

p2 >> charm(P[-3,[1,-2],0], shape=linvar([0.2,0.6],[8,4,2,2]), dur=1/4, oct=[3,4,5], room=0.7, mix=0.7, echo=1, echotime=1, amp=linvar([2,0],4), hpf=linvar([200,2000],8)) + var([-1,0,-1,-2])

o1 >> sawbass(P[0,5,7,3].every(4, 'rotate'),oct=5, dur=2, amp=2) + linvar([0,2],4)
o1.stop()

o3 >> gong(var([p2.pitch],4), dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)


o6 >> play('-[--] k')
o6.stop()


o1.stop()

o2 >> play('/', dur=4)
o2.stop()

p3 >> play('G{ K}', rate=PRand(4), dur=1/2, sample=PRand(4))
p3.stop()

o4 >> play('G', dur=4, chop=8, rate=1/4)

p5 >> play('<(X * )>', amp=2)
p5.stop()

p4 >> play('< X><(-[--]) ><   >', sample=PRand(5))

p4.stop()

print(Scales.names())


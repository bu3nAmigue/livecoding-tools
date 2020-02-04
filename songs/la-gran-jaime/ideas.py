
# Voces
from .Extensions.Voice import voice
notas = (PWalk(4))[:10]
voice([0,2,3,4],dur=[1],lyrics="música",file="v1",octave=6,scale=Scale.wholeTone)

from .Extensions.Voice import voice
notas = (PWalk(4))[:10]
voice([0,2,3,4],dur=[1],lyrics="hola",file="v1",octave=6,scale=Scale.wholeTone)

v2 >> loop("v6",P[0:8],dur=PSum(4,4),amp=var([7],8),mix=0.0,room=0.0,formant=0)

v2 >> loop("v1",P[0:8],amp=var([7,0],8),dur=PSum(4,4),mix=0.0,room=0.0,formant=0)

# Escalas
Scale.default = Scale.wholeTone

# Bases

m1 >> sawbass([0],dur=4,sus=0.5,amp=[0,12])

o1 >> sawbass(P[0,5,7,3].every(4, 'rotate'),oct=5, dur=2, amp=2) + linvar([0,2],4)

o7 >> space([0,2], dur=[8,4,4,2,2], hpf=linvar([400,4000],16), amp=4)


# Plays

d1 >> play("+*", dur=PDur(4,4),rate=PRand(10),amp=2)

d2 >> play("-",amp=4,dur=PSum(7,4))

d1 >> play('G{ K}', rate=PRand(4), dur=1/2, sample=PRand(4))

d2 >> play('G', dur=4, chop=8, rate=1/4)

d1 >> play('-- [-----*-]', amp=2, dur=1/2)

d3 >> play('/', dur=4)

d1 >> play('G{ K}', rate=PRand(4), dur=1/2, sample=PRand(4))

d2 >> play('G', dur=4, chop=8, rate=1/4)

d1 >> play('< X><(-[--]) ><   >', sample=PRand(5))

d5 >> play("X",rate=PRand(4),dur=PSum(8,4))

d3 >> play("#",rate=-1/2,dur=8)

d1 >> prophet([0,[1,-2]],amp=1.4) + var([(0,2,4)])


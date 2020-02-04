Root.default = -3
Scale.default = 'minor'
Clock.bpm=100
acordes = [(2,4,6),(-1,1,3),(0,2,4)]
escalera = P[5,4,3,2]

p1 >> space([0,0,4,2,0,0,5,2],dur=1,amp=[0,1,1,1])
d1 >> play("X ",amp=1)
pt >> play('#', dur=16,sus=4, rate=-1/2, amp=var([1,0],[16,inf],start=now))

p1 >> space([4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])

p1 >> space([0,0,4,2,0,0,5,2],dur=1,amp=[0,1,1,1])
b1 >> ambi([0,-2,4,3],dur=4,sus=3,oct=3,chop=3,amp=3)
v1 >> loop("verso",P[0:8],formant=0,amp=2,room=0.0,mix=0.0,glide=0,chop=0)

p1 >> space([4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
v1 >> loop("verso",P[8:16],formant=0,amp=2,room=0.0,mix=0.0,glide=0,chop=0)
d3 >> play("-")

p1 >> space([0,0,4,2,0,0,5,2],dur=1,amp=[0,1,1,1])
v1 >> loop("verso",P[0:8],formant=2,amp=2,room=0.0,mix=0.0,glide=0,chop=0)

p1 >> space([4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
v1 >> loop("verso",P[8:16],formant=2,amp=2,room=0.0,mix=0.0,glide=0,chop=0)

pt >> play('#', dur=16,sus=4, rate=-1/2, amp=var([1,0],[16,inf],start=now))
b1 >> ambi([0],dur=4,sus=2,oct=3,chop=3)

p1 >> space([(0,2,4)]*4,dur=2,amp=1)
p2 >> prophet([(0,2,4)]*4,dur=2,amp=0.5)

d1 >> play("X ",amp=1)
d3 >> play("-",dur=PSum(6,4))
b1 >> bass([2,-1,0,-2],dur=4,chop=2,sus=3,amp=0.7,oct=5)
n = 5
p2 >> prophet([(2,4,6)]*n+[(-1,1,3)]*n+[(0,2,4)]*n+[5,4,3,2],dur=list(PSum(n,4)[:n*3])+[1]*4,amp=[1,1,1,1]*3 + [1,1,1,1])
v1 >> loop("estribillo1_pablito_rack",P[0:8],formant=[0],amp=1)

v1 >> loop("estribillo1_pablito_rack",P[8:16],formant=[0],amp=1)

v1 >> loop("estribillo2_mathi_rack",P[0:8],formant=[0],amp=0.7)

v1 >> loop("estribillo2_mathi_rack",P[8:16],formant=[0],amp=0.7)

v1 >> loop("estribillo3_pablito_rack",P[0:8],formant=[0],amp=1)

v1 >> loop("estribillo3_pablito_rack",P[8:16],formant=[0],amp=1)

v1 >> loop("estribillo4_pablito_rack",P[0:8],formant=[0],amp=1)

v1 >> loop("estribillo4_pablito_rack",P[8:16],formant=[0],amp=1)

b1 >> bass([2],dur=4,chop=3,sus=2)
p1 >> space([(2,4,6)]*4,dur=2,amp=1)
p2 >> prophet([(2,4,6)]*4,dur=2,amp=1)


v1 >> loop('estribillo4_pablito_rack',P[0:8], formant=0,amp=1)
v2 >> loop('estribillo4_mathi_rack', P[8:16],formant=0, amp=0.5)

Group(v1,v2).solo()

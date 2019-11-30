
Root.default = -3
Scale.default = 'minor'
Clock.bpm=100
acordes = [(2,4,6),(-1,1,3),(0,2,4)]
escalera = P[5,4,3,2]

def a():
    v1 >> loop("estribillo1",P[8:16],formant=[0],amp=2.5,room=0.4,mix=0.4,glide=0,chop=0)
    Clock.future(8, lambda : b())
def b():
    v1 >> loop("estribillo1",P[16:24],formant=[0],amp=2.5,room=0.4,mix=0.4,glide=0,chop=0)
    Clock.future(8, lambda : c())
def c():
    v1 >> loop("estribillo1",P[24:32],formant=[0],amp=2.5,room=0.4,mix=0.4,glide=0,chop=0)
    Clock.future(8, lambda : d())
def d():
    v1 >> loop("estribillo1",P[32:40],formant=[0],amp=2.5,room=0.4,mix=0.4,glide=0,chop=0)
    Clock.future(8, lambda : e())
def e():
    v1 >> loop("estribillo1",P[40:48],formant=[0],amp=2.5,room=0.4,mix=0.4,glide=0,chop=0)
def plat():
    pt >> play('#', dur=16,sus=4, rate=-1/2)
def intro():
    Clock.future(8, lambda : plat())
    p1 >> space([0,0,4,2,0,0,5,2,4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
    d1 >> play("X ",amp=1)
def verso():
    b1 >> ambi([0,-2,4,3],dur=4,sus=3,oct=3,chop=3,amp=3)
    p1 >> space([0,0,4,2,0,0,5,2,4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
    d2 >> play("-")
    v1 >> loop("verso",P[0:16],formant=var([2,0],[16]),amp=2,room=0.0,mix=0.0,glide=0,chop=0)
    p2.stop()
def puente1():
    p1.solo()
    pt >> play('#', dur=8,sus=4, rate=-1/2)
    b1 >> ambi([0],dur=4,sus=2,oct=3,chop=3)
    p1 >> space([(0,2,4)]*4,dur=2,amp=1)
    p2 >> prophet([(0,2,4)]*4,dur=2,amp=0.5)
def estribillo():
    d1 >> play("X ",amp=1)
    d3 >> play("-",dur=PSum(6,4))
    b1 >> bass([2,-1,0,-2],dur=4,chop=2,sus=3,amp=0.7,oct=5)
    n = 5
    p1.stop()
    pt.stop()
    p2 >> prophet([(2,4,6)]*n+[(-1,1,3)]*n+[(0,2,4)]*n+[5,4,3,2],dur=list(PSum(n,4)[:n*3])+[1]*4,amp=[1,1,1,1]*3 + [1,1,1,1])
    v1 >> loop("estribillo1",P[0:8],formant=[0],amp=2.5,room=0.4,mix=0.4,glide=0,chop=0)
    Clock.future(8, lambda : a())
def puente2():
    p1.solo()
    b1 >> bass([2],dur=4,chop=3,sus=2)
    p1 >> space([(2,4,6)]*4,dur=2,amp=1)
    p2 >> prophet([(2,4,6)]*4,dur=2,amp=1)

start = Clock.mod(32) - 0.1
Clock.schedule(intro, start)
Clock.schedule(verso, start+16)
Clock.schedule(puente1, start+16+32)
Clock.schedule(estribillo, start+16+32+8)
Clock.schedule(puente2, start+16+32+8+48)
Clock.schedule(verso, start+16+32+8+48+8)
Clock.schedule(puente1, start+16+32+8+48+8+48)
Clock.schedule(estribillo, start+16+32+8+48+8+48+8)
Clock.schedule(puente2, start+16+32+8+48+8+48+8+48)




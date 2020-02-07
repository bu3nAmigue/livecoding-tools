Root.default = 0

Clock.bpm=90
ritmo1 = P[1/2,1/2,1/4,1/4,rest(1/2)]
ritmo2 = P[3/2,rest(1/2),3/2,1/2,1/2,rest(1/2),1]
ritmo3 = P[1/2,3/2,1/4,rest(1/2),rest(1/4)].every(2,'shuffle')
base1=var([1,2,3,4],PRand(4))
base2=var([0,1,2],[8,2,2])
var.chords = var([0,2],8)

Scale.default='minorPentatonic'

Scale.default='minor'


## Intro

## Verso

## Puente

## Estribillo

## Puente.reverse()

## Cierre





# cancion 1

d2 >> play('(xo)-', sample=2)
d3 >> play('-- --- - -- ')

d3 >> play('r', dur=PDur(3,8,[2,0]), sample=[1,2,3], rate=1+0.1*PWhite(-10,10))

g1 >> gong(P[var([0,2],4),4,5,7][:6], dur=2, sus=3).every(6, 'offadd',4, dur=1).every(8,'stutter',4, dur=1, pan=[1,-1])

b1 >> blip(s1.pitch, dur=1/4, oct=[4,5], amp=1).every(6, 'offadd',2).every(8, 'stutter',4, dur=1, pan=[1,-1])
pp >> prophet(base2, dur=2, amp=1)

# Cancion 2
Clock.bpm=90
Scale.default = "minor"

s1 >> saw(var([0,-1,-2],[8,2,2]), cut=0,amp=0.7, shape=0,dur=PDur([3,5],8,[2,0]),oct=var([4,5],8), drive=1, glide=5, glidedelay=s1.sus*0.9) + var([0,2],8)

s3.reset() >> karp(variaciones('=+===+==-=-=====',raiz=1), cut=0, amp=2, dur=[1/2,1/4,rest(1/4),1/4], drive=0, glide=2, glidedelay=0.8, oct=(5,6)).every(3, 'offadd',4)

Group(s3).solo()

p1 >> glass(linvar([0,2],8), echo=1, echotime=2, glide=-8, glidedelay=0.5, dur=4) + var([0,2],16)

# percusion
d1 >> play('S', dur=PDur(3,8), amp=var([1,0],[8,4]), sample=1).every(8,'stutter',3)
d2 >> play(Pvar(['(x|o2|){[X ][ X]X-}','(x-) (x )( |z1|})','X [Xx] '],4),dur=1/2, amp=[1], sample=3, lpf=0)


p8 >> play('{   b}b',dur=PDur([5,[7,5]],8,[2,0]), formant=linvar([0,1],8),hpf=linvar([300,888],16), room=0.9, rate=var(P[2/3,3/5,1,2,1],[8,4,4,8,8])).spread()
p8.stop()


d1 >> play('S', dur=PDur(3,8), amp=var([1,0],[8,4]), sample=1).every(8,'stutter',3)

print(SynthDefs)


print(P[0,[3,5],2,3,5,6,5,2])

print(P[0,0,0].splice([1,2,3],[4,5,6]))

#####################
# TEMA ESTRUCTURADO #
#####################


## CODIGO ##
##### Abajo arriba
def abajo():
    d_all.lpf=500
    d_all.solo()
def arriba():
    d_all.lpf=0
    d_all.solo(
def abajoarriba(intervalo):
    abajo()
    Clock.future(intervalo, lambda: arriba())
#go up
def go_up(nota_base):
    nuevo_up = []
    nuevo_up.append(nota_base + 1)
    nuevo_up.append(nota_base + 1 + PRand(1))
    nuevo_up.append(nota_base + 2 + PRand(2))
    nuevo_up.append(nota_base + 3 + PRand(3))
    return nuevo_up
#go down
def go_down(nota_base):
    nuevo_down = []
    nuevo_down.append(nota_base - 1)
    nuevo_down.append(nota_base - 1 - PRand(1))
    nuevo_down.append(nota_base - 2 - PRand(2))
    nuevo_down.append(nota_base - 3 - PRand(3))
    return nuevo_down
#just stay
def go_stay(nota_base):
    nuevo_stay = []
    nuevo_stay.append(nota_base + PRand(1) + 1)
    nuevo_stay.append(nota_base)
    nuevo_stay.append(nota_base + PRand(1) + 1)
    nuevo_stay.append(nota_base)
    return nuevo_stay
#la funcion variaciones transforma un string en un pitch juntando los sets de go
def variaciones(variation_string, raiz=0):
    final_pitch = []
    notita = raiz
    for each in variation_string:
        if each == '+':
            for stuff in go_up(notita):
                final_pitch.append(stuff)
            notita = notita + 3
        elif each == '-':
            for stuff in go_down(notita):
                final_pitch.append(stuff)
            notita = notita - 3
        elif each == '=':
            for stuff in go_stay(notita):
                final_pitch.append(stuff)
    return final_pitch





# arpa 1

s3.reset() >> karp(variaciones('=+===+==-=-=====',raiz=1), cut=0, amp=2, dur=[1/2,1/4,rest(1/4),1/4], drive=0, glide=2, glidedelay=0.8, oct=(5,6)).every(3, 'offadd',4)

# arpa 2

m1.reset() >> karp(P[0,5,4,2,0,2,3,4].every(2,'mirror').every(3,'reverse'),oct=6,amp=1,dur=var([1,1,0.5,0.25],4),scale=Scale.majorPentatonic, glide=1.5, glidedelay=0.8,room=0.0, mix=0.0).every(2, 'stutter', 3, dur=0.75, pan=[-1,1]) + var([0,2],8)

m1.reset() >> karp(P[0,5,4,2,0,2,3,4].every(2,'mirror').every(3,'reverse'),oct=6,amp=1,dur=var([1,1,0.5,0.25],4),scale=Scale.majorPentatonic, glide=1.5, glidedelay=0.8,room=0.0, mix=0.0).every(2, 'stutter', 3, dur=0.75, pan=[-1,1]) + var([0,2],8)

b1 >> bass([0,5,4,2],chop=3,dur=4,sus=4,scale=Scale.majorPentatonic)

v1 >> space(P[0,5,4,2,0,2,3,4].every(3,'mirror'), oct=6,amp=1.5,dur=0.5).every(4, 'offadd',2)

arriba()


intro()

def batas():
    d1 >> play('S', dur=PDur(3,8), amp=var([1,0],[8,4]), sample=1).every(8,'stutter',3)
    d2 >> play(Pvar(['(x|o2|){[X ][ X]X-}','(x-) (x )( |z1|})','X [Xx] '],4),dur=1/2, amp=[1], sample=3, lpf=0)
def intro():
    m1.reset() >> karp(P[0,5,4,2,0,2,3,4].every(2,'mirror').every(3,'reverse'),oct=6,amp=1,dur=4, sus=8,scale=Scale.majorPentatonic, glide=1.5, glidedelay=5,room=0.9, mix=0.9) + var([0,2],8)
    Clock.future(8,lambda : batas())
def verso():
    v1 >> bass(P[0,5,4,2,0,2,3,4],dur=4,oct=6,chop=3,amp=1.0,scale=Scale.majorPentatonic,glide=0,glidedelay=0.8,mix=0.8,room=0.8)
    m1.reset() >> karp(P[0,5,4,2,0,2,3,4].every(2,'mirror').every(3,'reverse'),oct=6,amp=1,dur=var([1,1,0.5,0.25],4),scale=Scale.majorPentatonic, glide=1.5, glidedelay=0.8,room=0.0, mix=0.0).every(2, 'stutter', 3, dur=0.75, pan=[-1,1]) + var([0,2],8)
def puente():
    abajo()
def estribillo():
    arriba()
    m1.stop()
    s3.reset() >> karp(variaciones('=+===+==-=-=====',raiz=0), cut=0, amp=2, dur=[1/2], drive=0, glide=1.5, glidedelay=0.9, oct=(6)).every(3, 'offadd',4)
def puente2():
    abajo()

estribillo()


start = Clock.mod(32) - 0.1
Clock.schedule(intro, start)
Clock.schedule(verso, start+32)
Clock.schedule(puente, start+48+32)
Clock.schedule(estribillo, start+48+32+16)


p1 >> pluck(([[0,-1,-2,-3],[7,3],[(6,4),(4,2)],5,(4,2),2,4,(5,3)] + [-1,0,(0,2),0,-3,0,(0,2),-1]), dur=[1,1,1.25,0.75,1,1,1,1], amp=[linvar([0.4,0.8],2)], sus=3, echo=4, pan=0.6, oct=([5,4],5,5), lpf=1000)


p2 >> blip(P[-4:10:2], dur=[rest(1),0.75,0.5,0.25], sus=3, echo=6, pan=0.8, amp=[linvar([0.2,0],3)]).every(8,"rotate").every(3, "stutter",4)

p3 >> blip(P[0:8:2], dur=[0.5,0.75,rest(1)], pan=-0.8, sus=3, echo=6, amp=[linvar([0,0.2],2)]).every(5, "stutter",6). every(12, "reverse")


p4 >> sinepad(amp=0.7, oct=[4,5], dur=4, pan=-0.6).follow(p1) + [2]

b1 >> keys([0,0], amp=1.5, dur=[rest(4),4], oct=4, room=6)


##### Abajo arriba
def abajo():
    d_all.lpf=500
    d_all.solo()
def arriba():
    d_all.lpf=0
    d_all.solo()
abajo()
Clock.future(4, lambda: arriba())


def updateAmp(player,amp):
    player.amp = amp
def managePlayer(player,intervals,total):
    print("Running player manager")
    amp = list(player.amp)
    player.amp = 0
    start, end = intervals[0]
    start_time = Clock.now()
    starting_time = start+start_time
    ending_time = end+start_time
    Clock.schedule(lambda : updateAmp(player,amp),starting_time)
    intervals = list(map(lambda interval : (interval[0] - end,interval[1] - end), intervals))
    start, end = intervals[0]
    intervals = intervals[1:] + [(start+total,end+total)]
    print(intervals)
    Clock.schedule(lambda : managePlayer(player,intervals,total),ending_time)

a1 >> pluck(0,dur=1)
b1 >> bass(0,dur=4)
a2 >> pluck(4,dur=1)
b2 >> bass(4,dur=2)
b3 >> pluck(7,dur=1)

managePlayer(a1,[(0,8)],24)
managePlayer(b1,[(0,8)],24)
managePlayer(a2,[(8,16)],24)
managePlayer(b2,[(8,16)],24)
managePlayer(b3,[(16,24)],24)


#Ejemplo
sv >> saw(variaciones('+++===--------====', raiz=0), dur=1)

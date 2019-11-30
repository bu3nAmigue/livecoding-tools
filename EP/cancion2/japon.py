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

Clock.bpm = 120
Scale.default=Scale.minor
def incrementar(notas,inc):
    return list(map(lambda x: x+inc,notas))
def length(chords,dur):
    return sum([ dur[i%len(dur)] for i in range(len(chords))])
    c3.reload()
def choirProgression(chords,letra="la",dur=[1],model=None,octave=5):
    if model is None:
        voice(chords,lyrics=letra,dur=dur,file='c1',octave=octave)
        voice(incrementar(chords,2),lyrics=letra,dur=dur,file='c2',octave=octave)
        voice(incrementar(chords,4),lyrics=letra,dur=dur,file='c3',octave=octave)
    else:
        voice(chords,lyrics=letra,dur=dur,file='c1',octave=octave,model=model)
        voice(incrementar(chords,2),lyrics=letra,dur=dur,file='c2',octave=octave,model=model)
        voice(incrementar(chords,4),lyrics=letra,dur=dur,file='c3',octave=octave,model=model)
def playChoir(chords,dur,reverb=True,amp=1):
    if reverb:
        mix=0.9
        room=0.9
    else:
        mix=0
        room=0
    c1.reload()
    c1 >> loop('c1',P[0:length(chords,dur)],formant=0,amp=amp,mix=mix,room=room)
    c2.reload()
    c2 >> loop('c2',P[0:length(chords,dur)],formant=0,amp=amp,mix=mix,room=room)
    c3.reload()
    c3 >> loop('c3',P[0:length(chords,dur)],formant=0,amp=amp,mix=mix,room=room)
def stopChoir():
    c1.stop()
    c2.stop()
    c3.stop()

# Generate voices
#choirProgression([0,2,3,4],dur=[4], letra="la",octave=5)

#notas = (PWalk(4))[:20]
#voice(notas,dur=([2]*8),lyrics="bien ve ni dos gracias por ve nir",file="t1v2",octave=6,scale=Scale.minorPentatonic)

# Play music

#stopChoir()

start = Clock.mod(16) - 0.1
Clock.schedule(lambda : playChoir([0],[16],amp=1), start)

v2 >> loop("t1v2",P[0:16],dur=PSum(4,4),mix=0.1,room=0.0,amp=1,formant=0)

b2 >> bass(dur=4,chop=3,sus=3, amp=0.6)
d2 >> play("b", amp=0.6)
d1 >> play("X   ",sample=4, amp=1)

v2 >> viola(PWalk(4),dur=[4],sus=2,scale=Scale.minorPentatonic,amp=[1])

###################################################
################# EL PITY #########################
###################################################

stopChoir()
d2.stop()
b2.chop=0
b2.sus=0
d1.sample=0

# VOCES
#intro
v2 >> loop("t2v2",P[0:4],dur=1,amp=var([2,0],4),mix=0.8,room=0.8,formant=[0])

#verso
v3 >> loop("t2v2",P[0:16],dur=PSum(4,4),amp=var([1],8),formant=[1])

#estribillo
v2 >> loop("t2v7",P[0:8],dur=PSum(1,1),amp=var([1],4),mix=0.9,room=0.9,formant=2)

v3 >> loop("t2v5",P[0:16],dur=PSum(9,4),amp=var([1,0],4),mix=0.9,room=0.9,formant=linvar([0,0]))


#vx.stop()

#INSTRUMENTIS

#intro
ps >> saw([0,2], dur=4, sus=3, oct=(5))

#verso
chords = [0,2,3,4]
duracion = 4

m1 >> gong(P+[chords]|P[chords],dur=[duracion/2]*4+[duracion/4]*4, amp=1, oct=(4,[5,6])).every(4,'shuffle').every(2, 'offadd',-1) + var([(0,2,4,6),1])

m2 >> piano(PWalk(4),dur=0.5,amp=1,scale=Scale.minorPentatonic)
#m1.stop()
#m2.stop()

#estribillo
a1 >> gong(PWalk(4),dur=duracion/4,amp=2,scale=Scale.minorPentatonic, sus=duracion/2)

#el buen quin
m2 >> quin(var(chords), oct=[4,5], dur=PDur(5,8), amp=1.5, hpf=linvar([300, 1000]), shape=0.5) + var([0,2,-1])
m2.stop()

#cierre
m1 >> piano(chords, dur=duracion, amp=[[1.5]*4+[0]*4]) + var([0,2,4])

#v2.solo()
#v3.stop()

#p1 >> play("o",rate=-0.5,dur=var([1,0.5,0.25,0.125,0.1],[4]),amp=6)
#p2 >> play("b",rate=[0.2,0.1,0.05],dur=4,amp=20)
#v1 >> loop("bomb",P[0:8],amp=10,rate=2)

# AGREGAR SAMPLE DE EXPLOSION

verso()

intro()

estribillo()

cierre()

def cambio_de_etapa(f):
    d1.reset()
    m1.reset()
    b1.reset()
    b2.reset()
    v1.reset()
    v1.stop()
    m1.stop()
    f()
    print("CAMBIO DE PARTE")
Scale.default = 'minor'
Clock.bpm = 90
def intro(duracion = 1):
    d1 >> play('<-><  K ><Xs  >', dur=duracion, amp=1)
    b1 >> dbass(var([0,2,3,4],4), dur=duracion,sus=0.5, amp=[0.6],oct=5)
def verso(duracion = 1):
    chords = P[0,2,3,4]
    b1 >> dbass(var(chords,4),dur=[duracion],sus=1)
    d1 >> play("{x*xb}",dur=duracion/4,amp=0.5)
def estribillo(duracion=1):
    chords = P[0,5,4,2]
    b1 >> dbass(var(chords,1),dur=duracion/2, sus=1,oct=5)
    d1 >> play("<V([sV][{[--]-bb-b}])><#  b>",dur=duracion/2, sample=[1,2,3])
def cierre(duracion=4):
    d1 >> play('[bbbb] ',dur=duracion)
    b1 >> dbass([0], dur=duracion, sus=duracion,amp=0.6)
total = 64
aviso_tiempo_previo = 32
def proximo(etapa,tiempo,nombre):
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//4} beats para el {nombre}"),tiempo - aviso_tiempo_previo//4)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//2} beats para el {nombre}"),tiempo - aviso_tiempo_previo//2)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo} beats para el {nombre}"),tiempo - aviso_tiempo_previo)
    Clock.schedule(lambda : cambio_de_etapa(etapa), tiempo)
    
#BOTON DE ENCENDIDO
start = Clock.mod(16) - 0.1
proximo(intro, start + total*0,"intro")
# VERSO
proximo(verso, start + total*1,"verso")
# ESTRIBILLO
proximo(estribillo, start + total*2,"estribillo")
# VERSO
proximo(verso, start + total*3,"verso")
# ESTRIBILLO
proximo(estribillo, start + total*4,"ultimo estribillo!!!")
# CIERRE
proximo(cierre, start + total*5,"cierre")


###################################################
################### DARK  #########################
###################################################

def cambio_de_etapa(f):
    f()
    print("CAMBIO DE PARTE")    
total = 48
aviso_tiempo_previo = 28
def proximo(etapa,tiempo,nombre):
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//4} beats para el {nombre}"),tiempo - aviso_tiempo_previo//4)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//2} beats para el {nombre}"),tiempo - aviso_tiempo_previo//2)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo} beats para el {nombre}"),tiempo - aviso_tiempo_previo)
    Clock.schedule(lambda : cambio_de_etapa(etapa), tiempo)
Scale.default = "minor"
Root.default.set("B")
Clock.bpm=90
def intro():
    b1.stop()
    m1 >> soprano(PWalk(8),dur=1,sus=2,amp=0.5,oct=4)
    d3 >> play("#",rate=-1/2,dur=8,amp=1)
    m2 >> gong(var([p2.pitch],4), dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)
def verse1():
    b1 >> sawbass(var([0,1,-1],[12,2,2]),cut=0,sus=0.5, echo=0, echotime=1,decay=0.5,room=0.7, mix=1, amp=[1,0.5,0.5,1.5], dur=1/2,shape=var([0.2,0.3],8), oct=[6,5,5])
def verse2():
    d2 >> play('V-X-', amp=0.7).sometimes('amen')
    d1 >> play('o|*3|', sample=2, dur=2, amp=1)
def bridge():
    b1.solo()
def prechorus():
    d1.reset()
    d1 >> play(" X",amp=1)
    d2.reset()
    d2 >> play("-",amp=1)
    b1.amp=1.3
def chorus():    
    b1.reset()
    b1 >> bass(var([0,-1],[8,2]),dur=4,chop=var([8,16],5),amp=0.9, pan=[1,-1])
    
intro()

verse1()

verse2()

bridge()

prechorus()

chorus()

v1 >> loop("t3v3",P[0:16],amp=var([1.5],4),mix=0.0,room=0.0)

# Instrumentis
# bajo del coro con shape
b1 >> bass(var([0,-1],[8,2]),dur=4,chop=var([8,16],5),amp=0.8, pan=[1,-1], shape=0.2)

#bips del tema anterior
bb >> play('{[bb] b}{b }{[bb]bb }',dur=1/2, rate=1, amp=PRand(1))

#ambi cosmico # SIRENAAAAAA
y1 >> ambi(linvar([0,5],16), dur=1/8, cut=0, chop=0, room=0.6, mix=0.8, pan=linvar([-1,1]), amp=linvar([1,1.5,1.5,1]))

d1 >> play('o|*3|', sample=2, dur=2, amp=1)

m1 >> charm(PWalk(5),amp=2,chop=2,scale=Scale.minorPentatonic)

v2 >> loop("t3v1",P[0:16],mix=0.9,room=0.9,amp=var([1],[4]))

v1 >> loop("o1",P[0:8],mix=0.8,room=0.9,amp=var([1,0],[4]))

m2 >> blip(PWalk(4),dur=1,amp=1)

start = Clock.mod(16) - 0.1
Clock.schedule(intro, start)
proximo(verse1, start + total*1,"verso1")
proximo(verse2, start + total*2,"verso2")
proximo(bridge, start + total*3,"puente")
proximo(prechorus, start + total*3.5,"pre-estribillo")
proximo(chorus, start + total*4.5,"estribillo")


###################################################
################## JINGLE  ########################
###################################################


Scale.default = list(range(12))
Clock.bpm = 60
d0 >> bass([(-60,), (-5,), (-1,), (2,), (-5,), (-7,), (-3,), (0,), (-7,)],dur=[4.0, 0.25, 0.25, 0.25, 1.25, 0.25, 0.25, 0.25, 1.25],amp=[0, 1, 1, 1, 1, 1, 1, 1, 1],chop=1, bpm=60, scale=list(range(12)))
d1 >> blip([(-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-17, -29), (-29,), (-22,), (-29,), (-22,), (-29,), (-22,), (-29,), (-22,), (-31,), (-24,), (-31,), (-24,), (-31,), (-24,), (-31,), (-24,)],dur=[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],shape=0.3, pan=(-1,1), bpm=60, scale=list(range(12)))

fx >> play('TEDX', dur=0.25, amp=1).often('amen')
fx.stop()
d3 >> play("[wwww]",rate=1,dur=8)
d2 >> play("#",rate=-0.5,dur=4,amp=4)

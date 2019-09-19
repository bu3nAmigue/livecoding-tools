
def cambio_de_etapa(f):
    d1.reset()
    m1.reset()
    b1.reset()
    v1.reset()
    v1.stop()
    m1.stop()
    b2.stop()
    f()
    print("CAMBIO DE PARTE")
Scale.default = "minor"
Root.default.set("B")
Clock.bpm=90
def intro():
    m1 >> soprano(PWalk(8),dur=1,sus=2,amp=1,oct=4)
    d3 >> play("#",rate=-1/2,dur=8,amp=3)
    m2 >> gong(var([p2.pitch],4), dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)
def verse1():
    b1 >> sawbass(var([0,1,-1],[12,2,2]),cut=0,sus=0.5, echo=0, echotime=1,decay=0.5,room=0.7, mix=1, amp=[4,2,2,5], dur=1/2,shape=var([0.2,0.3],8), oct=[6,5,5])
def verse2():
    d2 >> play('V-[sV]-').offbeat().sometimes('amen')
    d1 >> play('o|*3|', sample=2, dur=2, amp=4)
    d3 >> play('G', rate=var([-1/2,-1/3,-2/3,-3/5,-2/5,-2/6],1),dur=1, echo=0.5, echotime=1, amp=[PRand(1),PRand(3)])
def prechorus():
    m1 >> charm(P[-3,[1,-2],0], shape=linvar([0.2,0.6],[8,4,2,2]), dur=PDur(8,8), oct=[3,4,(5,6)], room=0.7, mix=0.7, echo=1, echotime=1, amp=linvar([2,0],4), hpf=linvar([200,2002],8)) + var([-1,0,-1,-2])
    b1 >> sawbass(P[0,5,7,3].every(4, 'rotate'),oct=5, dur=[1,1/2], amp=2) + linvar([0,2],4)
    b2 >> gong(p2.pitch, dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)
    m2.stop()
    d1 >> play("+*", dur=PDur(7,4),rate=PRand(10),amp=2)
    d2 >> play("-")
    d2 >> play("KaX",sample=PRand(2))
def chorus():    
    d1 >> play("X ",amp=5,dur=0.125)
    b2 >> prophet(var([0,[1,-2]],1),dur=0.125,amp=8) + var([(0)])

total = 32
aviso_tiempo_previo = 28
def proximo(etapa,tiempo,nombre):
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//4} beats para el {nombre}"),tiempo - aviso_tiempo_previo//4)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//2} beats para el {nombre}"),tiempo - aviso_tiempo_previo//2)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo} beats para el {nombre}"),tiempo - aviso_tiempo_previo)
    Clock.schedule(lambda : cambio_de_etapa(etapa), tiempo)

start = Clock.mod(16) - 0.1
Clock.schedule(intro, start)
# VERSO
proximo(verse, start + total,"verso")
# ESTRIBILLO
proximo(preChorus, start + total*2,"pre-estribillo")
# VERSO
proximo(chorus, start + total*3,"estribillo")
# ESTRIBILLO
proximo(verse2, start + total*5,"verso")
# VERSO
proximo(chorus, start + total*7,"estribillo")
# ESTRIBILLO
proximo(verse, start + total*9,"ultimo estribillo!!!")


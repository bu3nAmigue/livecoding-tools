

pitch1 = Pvar([P[1,1+PRand(1),2+PRand(4),4,var([0,2],4),2+PRand(2),5,7],[0,5,4,2]],[12,4])

b1 >> acid309(pitch1, att=0.001, dur=PDur([4,5,7],[8,16]), amp=0.1,sus=b1.dur*0.1, oct=[4,4,4,5]) + var([0,2],8)

d1 >> play('-',amp=1)

d2 >> play('X(v )X{|A0|[|A0||A0|] }', sample=2,dur=1, amp=2,rate=[0.5,0.5,1])

d1 >> play('X  (O)X O(*  O)',dur=1/4, sample=0)

d4 >> play('M{ |T1| }', dur=PDur([3,4],var([5,7],8),[0,2]), sample=2, amp=2,rate=1, lpf=linvar([200,3000],8))

d4.stop()

Group(v1,d1,v3).solo(0)

b2 >> dirt(var([0,2,1],[4,2,2]),att=0.01,rel=1, dur=var([1/2,1/4],4),shape=0.2, drive=0.3,formant=10, oct=var([4,5],8))

b2.stop()

b1 >> bass(var([0,-1],[8,2]),dur=[4],sus=4,chop=var([8,16],5),amp=1,oct=(5), pan=[(1,-1),(-1,1)],att=0.001, shape=0,drive=0,glide=var([4,-4],8), glidedelay=0.5) + var([0,1],4)

var([0,-1],[8,2])

b1.stop()

co >> combs(var([0,2],4),dur=[8], amp=0.5, sus=0.5)

a1 >> acidOto3091(var([0,2],4), sus=a1.dur*0.07, dur=[1/2,1/4,1/4,1/4,1/4,1/4,1/4], oct=3, att=0.01) + var([0,2],8)

v1.reset()

v1.stop()

v2 >> ambi([0],dur=PSum(6,4),sus=0.2,glide=[0,2,4,7],chop=2,glidedelay=0.2,shape=0.9,drive=0.9,scale=Scale.minorPentatonic)


v2.stop()

Scale.default = "major"

print(SynthDefs)

d2.stop()

d2 >> play("123412",dur=PSum(2,4),rate=[1,1,1.2,1.5])

d1 >> play("X ",sample=2,dur=1,amp=1)

d3 >> play("-",dur=1)

v3 >> sawbass(var([0,2,3,4],4),dur=4,sus=3,formant=0,mix=0.0,room=0.0,chop=4,amp=1,oct=[4])

Clock.future(0, λ: set_amp(d2,1))
Clock.future(16, λ: set_amp(d1,1))
Clock.future(32, λ: set_amp(d3,1))

print(d3.samples)

def set_amp(player, amp_value):
    player.amp=amp_value

print(Clock.now())

print(d1.samples)

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
    d2 >> play('X(v )X{|b0|[|b0||b0|] }', sample=2, amp=1)
    b1 >> sawbass(var([0,1,-1],[12,2,2]),cut=0,sus=0.5, echo=0, echotime=1,decay=0.5,room=0.7, mix=1, amp=[1,0.5,0.5,1.5], dur=1/2,shape=var([0.2,0.3],8), oct=[6,5,5])
def verse2():
    d2 >> play('V-X-', amp=0.7,sample=0).sometimes('amen')
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

d2 >> play('V(v )X{|b0|[|b0||b0|] }', sample=2, amp=1)



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
bb >> play('{[bb] b}{b }{[bb]bb }',dur=1/2, rate=1, amp=PRand(1)).stop()

#ambi cosmico # SIRENAAAAAA
y1 >> ambi(linvar([0,5],16), dur=1/8, cut=0, chop=0, room=0.6, mix=0.8, pan=linvar([-1,1]), amp=linvar([1,1.5,1.5,1]))

d1 >> play('o|*3|', sample=2, dur=2, amp=1)

d1.stop()

v1 >> charm(PWalk(5),amp=2,chop=2,scale=Scale.minorPentatonic)

v2 >> loop("t3v1",P[0:16],mix=0.9,room=0.9,amp=var([1],[4]))

v1 >> loop("o1",P[0:8],mix=0.8,room=0.9,amp=var([1,0],[4]))

m1 >> blip(PWalk(4),dur=1,amp=1)

start = Clock.mod(16) - 0.1
Clock.schedule(intro, start)
proximo(verse1, start + total*1,"verso1")
proximo(verse2, start + total*2,"verso2")
proximo(bridge, start + total*3,"puente")
proximo(prechorus, start + total*3.5,"pre-estribillo")
proximo(chorus, start + total*4.5,"estribillo")

import sounddevice as sd
import soundfile as sf
import threading
import time



def record(bpms,name):
    time.sleep(0.355)
    fs=44100
    duration = bpms*60/Clock.bpm
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1,dtype='float64',device=find_source("system"))
    print("RECORDING")
    sd.wait()
    sf.write(FOXDOT_ROOT + "/snd/_loop_/"+name+".wav", myrecording, fs)
    print("FINISHED RECORDING")
record_thread = lambda bpms, name : threading.Thread(target = lambda : record(bpms,name)).start()

def verboseRecord(bpms,nombre):
    start = Clock.mod(bpms)-0.1
    Clock.schedule(lambda : print("4"), start-4)
    Clock.schedule(lambda : print("3"), start-3)
    Clock.schedule(lambda : print("2"), start-2)
    Clock.schedule(lambda : print("1"), start-1)
    Clock.schedule(lambda : record_thread(bpms,nombre), start)

# Ejemplo de uso

## Dejar sonando algo
m1 >> pluck([0,1,2,3,4,5,6,7])

verboseRecord(4,"test")

## Reproducir la grabación
v1.reload()
v1 >> loop("test",P[0:16])

print(sd.query_devices())

print(list(a))

def find_source(source):  
    a = sd.query_devices()
    for i, v in enumerate(list(a)):
        if v["name"] == source:
            return i

print(find_source("system"))


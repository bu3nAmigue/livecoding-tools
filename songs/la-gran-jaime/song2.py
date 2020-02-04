from .Extensions.VRender import vrender
from .Extensions.Voice import voice
def nextBarX(total):
    return Clock.mod(total) - 0.1
class Section():
    def __init__(self,play,dur):
        self.play = play
        self.dur = dur
def executeSong(sections):
    if len(sections) > 0:
        nextSection = sections[0]
        nextSection.play()
        Clock.future(nextSection.dur, lambda : executeSong(sections[1:]))
    else:
        Clock.clear()
def choirChordProgression(chords,letra="la",dur=[1],model=None,octave=5):
    if model is None:
        voice(chords,lyrics=letra,dur=dur,file='c1',octave=octave)
        voice(incrementar(chords,2),lyrics=letra,dur=dur,file='c2',octave=octave)
        voice(incrementar(chords,4),lyrics=letra,dur=dur,file='c3',octave=octave)
    else:
        voice(chords,lyrics=letra,dur=dur,file='c1',octave=octave,model=model)
        voice(incrementar(chords,2),lyrics=letra,dur=dur,file='c2',octave=octave,model=model)
        voice(incrementar(chords,4),lyrics=letra,dur=dur,file='c3',octave=octave,model=model)
def playChoir(chords,dur=[1],reverb=False,amp=3):
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
def incrementar(notas,inc):
    return list(map(lambda x: x+inc,notas))
def length(chords,dur):
    return sum([ dur[i%len(dur)] for i in range(len(chords))])
    c3.reload()
def stopChoir():
    c1.stop()
    c2.stop()
    c3.stop()
def drums(tranca=True,speed=1):
    if tranca:
        d1 >> play("{-[-(-o)]}x-o", sample=0,dur=1).every([28,4], "trim", 3)
        d2 >> play("(X )( X)N{ xv[nX]}", dur=1)
        d3.stop()
        d4.stop()
    else:
        d1 >> play("{-[-(-o)]}x-o", sample=0,dur=speed).every([28,4], "trim", 3)
        d2 >> play("<|V0|:><  O ><|[--]5|>", sample=1,dur=speed)
        #d2 >> play("(X )( X)N{ xv[nX]}", drive=0.2, lpf=var([0,40],[28,4]),dur=speed).sometimes("sample.offadd", 1, 0.75)
        #d3 >> play("e", amp=var([0,1],[PRand(8,16)/2,1.5]), dur=PRand([1/2,1/4]), pan=var([-1,1],2))
        #d4 >> play("#", dur=32, room=1, amp=2).spread()
def stopDrum():
    d1.stop()
    d2.stop()
    d3.stop()
    d4.stop() 
def chordProgression(chords,tranca=True):
    if tranca:
        b1 >> piano(var(chords,4),dur=PSum(1,4),oct=4,amp=1)
        b2 >> marimba(var([(0,2,[4])])+var(chords,4),dur=PSum(4,4),oct=4)
    else:
        b1 >> piano(var(chords,4),dur=PSum(4,4),oct=4,amp=[0,1.5])
        b2 >> marimba(var([(0,2,[4])])+var(chords,4),dur=PSum(8,4),oct=4,amp=1.5)


Scale.default = Scale.minor

chords=[0,4,3,2]
chords2=[7,4,5,2]
notas = [7,6,5,4]

def a0():
    b1 >> sawbass(var([0,2,3,4],[4]),dur=4,oct=5)
def a1():
    d1 >> play('-x-D',dur=1)
    drums(True)
def a2():
    v1.reload()
    v1 >> loop('v2',P[0:len(notas)],amp=var([1],[1,1]),formant=0)
def a3():    
    drums(False,speed=1)
def a4():
    drums(False,speed=0.5)
    b1 >> sawbass(var([0,2,3,4],[4]),dur=2,oct=5)
    tranca=False
    b2 >> piano(var([0,2,3,4],4)+var([(0,4)],2),dur=1)
def a5():
    v1 >> loop('v2',P[0:len(notas)],dur=PDur(3,4),amp=var([5],[1]),mix=0.5,room=0.5,formant=0)
def a6():
    v1.solo()
    b2 >> piano(var([0,2,3,4],4)+var([(0,4)],2),dur=1)
def a7():
    v1.solo(0)
    d3 >> play("x-x-",amp=50)
    v3.reload()
    v3 >> loop('v1',P[0:16],formant=0,amp=var([3],[4]),mix=0.9,room=0.9)
    drums(True)
def a8():
    v1 >> loop('v1',P[0:12],dur=1,amp=4)
    d3.stop()
    v3.stop()
def a9():
    b1 >> sawbass(var([0,2,3,4],[4]),dur=2,oct=5)
    tranca=False
    drums(tranca,speed=0.5)
    b2 >> piano(var([0,2,3,4],4)+var([(0,4)],2),dur=1)
def a10():
    playChoir([0,2,3,4],dur=[4],reverb=True,amp=3)
def a11():
    v2 >> loop('v2',P[0:len(notas)],dur=1,amp=var([5,0],[4]),mix=0.5,room=0.5,formant=0)
def a12():
    v3.stop()

# Mejorar partes bruscas
# Agregar bajo y mas cosas para momento culmine
# Mejor bateria
# Sincopas
# Agregar algun detalle a la base
# Cambiar bajo

s0 = Section(a0,16)
s1 = Section(a1,16)
s2 = Section(a2,16)
s3 = Section(a3,16)
s4 = Section(a4,16)
s5 = Section(a5,16)
s6 = Section(a6,16)
s7 = Section(a7,16)
s8 = Section(a8,16)
s9 = Section(a9,16)
s10 = Section(a10,16)
s11 = Section(a11,16)
s12 = Section(a12,16)
sections = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11]*2
Clock.future(nextBarX(12,16), lambda: executeSong(sections))

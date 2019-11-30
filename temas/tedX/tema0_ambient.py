#from .Extensions.Voice import voice


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

v1 >> loop("t1v2",P[0:16],dur=PSum(4,4),mix=0.1,room=0.0,amp=1,formant=0)

b2 >> bass(dur=4,chop=3,sus=3, amp=0.6)
d2 >> play("b", amp=0.6)
d1 >> play("X   ",sample=4, amp=1)

v2 >> viola(PWalk(4),dur=[4],sus=2,scale=Scale.minorPentatonic,amp=[1])

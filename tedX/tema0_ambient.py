from .Extensions.Voice import voice

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
def playChoir(chords,dur,reverb=True,amp=3):
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
choirProgression([0,2,3,4],dur=[4], letra="tedex san isi dro")

notas = (PWalk(4))[:20]
voice(notas,dur=[4]*20,lyrics="bien ve ni dos los amo",file="t1v2",octave=7,scale=Scale.minorPentatonic)


# Play music

#stopChoir()

b1 >> ambi([0,4,6,3,2],dur=4)

v1.reload()
v1 >> loop("t1v2",P[0:64],mix=0.9,room=0.9,amp=2,formant=6)

playChoir([0],[4])

v1 >> viola(PWalk(4),dur=[1,3],scale=Scale.minorPentatonic,amp=[0,1])

b2 >> bass(dur=4,chop=3,sus=3)

d2 >> play("-")

d1 >> play("X   ",sample=4)

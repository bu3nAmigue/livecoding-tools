Clock.bpm=90

Scale.default='minorPentatonic'


ritmo1 = var([0,-2,1],[12,2,2])
ritmo2 = P[0,1]|P+[0,2]
p1 >> blip([[0,1,0,-2],ritmo2,1+PRand(2),4], dur=var([[1/2,1],[rest(0.5),1/4,1/2]],1/(PRand(4)+1)), amp=[1,1,1,0], oct=[(5,6),var([P(4,5),5],8)+PRand(2)]).often('stutter',2, dur=1/2)
p2 >> play('{x[xx]} (---[--]) ')
p3 >> sawbass(ritmo1, dur=1/2, amp=0.4, lpf=14444, formant=linvar([0,2],8))
p1.pitch=[0,[0],3,0,PRand(4)]
p4 >> gong(p1.pitch, dur=[1/2,rest(1/4)], pan=[-1,0,1,0]).every(3, 'offadd',2)

def onda():
    p1.dur=1/4
    print('Le pongo onda')
def no_onda():
    p1.dur=var([[1/2,1],[rest(0.5),1/4,1/2]],1/(PRand(4)+1))
    print('Le saco onda')
def onda_onda():
    onda()
    Clock.future(16, λ: no_onda())
    Clock.future(32, λ: onda_onda())

onda_onda()

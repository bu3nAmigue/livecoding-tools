def note2index(note):
    scale = list(Scale.default)
    return scale[note]

def sample2notes(notas,sample="b",dur=1,oct=0):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    p1 >> loop(sample,dur=var(dur,4), rate=var(rates,dur),amp=1)

def play2notes(notas,sample="b",dur=1,ritmo=8,oct=0):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    p2 >> play(sample,dur=var(ritmo,dur), rate=var(rates,dur),amp=0.5,sample=2)

sample2notes([0,5,4,2],"w",1)

sample2notes([0,7,3,2,5],"<{w[ww]}><(k[sk])><{[--][-*]}>",string_to_durs('ELPITYVIEJA', 1/4, 1))

d1 >> play("X ",amp=5)
play2notes([2,-1,0,-2]," Q [O123]",dur=4,ritmo=[1],oct=-2)

'''

def note2index(note):
    scale = list(Scale.default)
    return scale[note]
def sample2notes(notas,sample="b",dur=1,amp=amp):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,nota/12))
    p1 >> loop(sample,dur=dur, rate=var(rates,dur),amp=amp)
    
notas = [-60, -5, -1, 2, -5, -7, -3, 0, -7]
dur = [4.0, 0.25, 0.25, 0.25, 1.25, 0.25, 0.25, 0.25, 1.25]
amp = [0, 1, 1, 1, 1, 1, 1, 1, 1]

sample2notes(notas,"pruebita",dur,amp)

'''
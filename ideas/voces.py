from .Extensions.Voice import voice

voice([0,4,3,2,3,0],dur=[1],lyrics="Tec Flow",file="o2",octave=5,scale=Scale.minorPentatonic)


notas = PWalk(4)[:16]
voice(notas,dur=[1],lyrics="des mi ti fi can do da ta",file="o1",octave=6,scale=Scale.minorPentatonic)

v2.reload()
v2 >> loop("o2",P[0:16])


v1.reload()
v1 >> loop("o1",P[0:16])

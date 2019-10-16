base1=var([1,2,3,4],PRand(4))
base2=var([0,1,2],[8,2,2])
x1 >> sawbass(var([base1, base2],32), dur=1/4, shape=0.15, hpf=linvar([100,500],4))
x2 >> play('x-o(-[--] -)', sample=2, lpf=2000)

Scale.default='minorPentatonic'

def melo1():
    x3 >> saw(base1, dur=1/4, cut=0.7, oct=[4,5,6]) + var([0,1,-2],4)
    x1.dur=1/2
    Clock.future(20, lambda: melo2())
    print('En 20 melo2')

def melo2():
    x3 >> saw(base2, dur=1/4, cut=0.7, oct=[4,5,6]) + var([0,1,-2],4)
    x1.dur=1/4
    Clock.future(20, lambda: melo1())
    print('En 20 melo1')

melo1()




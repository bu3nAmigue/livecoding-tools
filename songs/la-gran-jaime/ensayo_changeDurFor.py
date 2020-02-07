#=======================================FoxDot=========================================

Scale.default = Scale.minorPentatonic

d1 >> play("X ")

d2 >> play(' [--](*--)([--][----])')

b1 >> ambi([(0,2,4)],dur=PSum(3,4),chop=2,oct=4,drive=0.1) + var([4,4,5,3],4)

b1 >> ambi([(0,2,4)],dur=PSum(8,4),chop=0,oct=4,drive=0.1) + var(PWalk(4)+4,4)

m1.reset() >> piano([(0,-2,-4),[-4,3],[PWalk(4),PWalk(-4)]], dur=[0.5,1,2.5], oct=[5,5], lpf=0) + m1_prog

m1_prog = var(P[[3,2],[5,6,7,4]],2)

changeDur(2,b_all)

def progressiveChange(change,times,intervalo,group=d_all):
    changeDurFor(change,intervalo*times,group)
    Clock.future(intervalo,lambda : progressiveChange(change,times-1,intervalo,group))

progressiveChange(0.5,4,4)

def changeDurFor(change, intervalo,group=d_all):
    changeDur(change,group=group)
    Clock.future(intervalo, lambda: changeDur(1/change,group=group))
    


changeDurFor(2,16,d_all)


print(funciones_extra)

abajoarriba(4)

m1.dur=0.5
m1.pitch=[(0,-2,4),[-5],5] + m1_prog


print(SynthDefs)

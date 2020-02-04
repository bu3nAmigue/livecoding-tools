Clock.bpm=144
def intro(duracion = 1):
    p1 >> blip(var([0,-1,1],[8,2,2]),oct=3, dur=1/4, sus=1, amp=[1,1,1,0])
    p2 >> play('X-*-', sample=PRand(var([4,7],4)))
def verso(duracion = 1):
    p1 >> blip(var([0,2,1],[8,2,2]),oct=[3,4,3], dur=1/4, sus=1, amp=[1,1,1,1])
    p2 >> play('-X-*`', sample=PRand(var([4,7],4)))
    p3 >> feel(var([0,2,1],[8,2,2]),dur=1,sus=0.5,oct=4,amp=[4,0])
def estribillo(duracion=1):
    p4 >> feel(PWalk(5),dur=0.5,scale=Scale.majorPentatonic)
    p5 >> gong(var([0,3,4,2],P[8,2,2].every(4,'shuffle')), dur=1/2, oct=P[3,4,5].palindrome())
def cierre(duracion=4):
    p4.stop()
    p3.stop()
    p1 >> blip(var([0,-1,1],[8,2,2]),oct=[3,4,3], dur=1/4, sus=1, amp=[1,1,1,1])

total = 48
start = Clock.mod(8) - 0.1
Clock.schedule(intro, start + total*0)
# VERSO
Clock.schedule(verso, start + total*1)
# ESTRIBILLO
Clock.schedule(estribillo, start + total*2)
# FINAL
Clock.schedule(cierre, start + total*3)
Clock.schedule(lambda : Clock.clear(), start + total*4)

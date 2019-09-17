
Clock.bpm=90
p1 >> sawbass(var([0,1,-1],[12,2,2]),cut=0,sus=0.5, echo=0, echotime=1,decay=0.5,room=0.7, mix=1, amp=[4,2,2,5], dur=1/2,shape=var([0.2,0.3],8), oct=[6,5,5])
d2 >> play('V-[sV]-').offbeat().sometimes('amen')
p3 >> play('o|*3|', sample=2, dur=2, amp=4)


f1 >> play('G', rate=var([-1/2,-1/3,-2/3,-3/5,-2/5,-2/6],1),dur=1, echo=0.5, echotime=1, amp=[PRand(1),PRand(3)])
f1.stop()



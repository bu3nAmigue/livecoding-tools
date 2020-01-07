
def changeDur(rate,group=d_all):
    for i in range(len(group)):
        if (not group.players[i].synthdef is None) and (group.players[i].name in list(map(lambda x:x.name,Clock.playing))):
            try:
                print("modifico a",group.players[i])
                group.players[i].dur = float(group.players[i].dur)*rate
            except:
                print("ERROR")
                print(group.players[i].dur)
                print(help(group.players[i].dur))

def changeAmp(rate, group=d_all):
    for i in range(len(group)):
        if (not group.players[i].synthdef is None) and (group.players[i].name in list(map(lambda x:x.name,Clock.playing))):
            try:
                print("modifico a",group.players[i])
                group.players[i].amp = float(group.players[i].amp)*rate
            except:
                print("ERROR")
                print(group.players[i].amp)
                print(help(group.players[i].amp))

d1 >> play("x")

changeDur(2) # Mas lento

changeDur(0.5) # Mas rapido

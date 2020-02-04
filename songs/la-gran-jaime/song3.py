def cambio_de_etapa(f):
    d1.reset()
    m1.reset()
    b1.reset()
    v1.reset()
    v1.stop()
    m1.stop()
    f()
    print("CAMBIO DE PARTE")
Scale.default = 'minor'
Clock.bpm = 90
def intro(duracion = 1):
    d1 >> play('<-><  K ><Xs  >', dur=duracion, amp=2)
    b1 >> dbass(var([0,2,3,4],4), dur=duracion,sus=0.5, amp=[0.9],oct=5)
def verso(duracion = 1):
    chords = P[0,2,3,4]
    b1 >> dbass(var(chords,4),dur=[duracion],sus=1)
    d1 >> play("{x*xb}",dur=duracion/4,amp=0.5)
def estribillo(duracion=1):
    chords = P[0,5,4,2]
    b1 >> dbass(var(chords,1),dur=duracion/2, sus=1,oct=5)
    d1 >> play("<V([sV][{[--]-bb-b}])><#  b>",dur=duracion/2, sample=[1,2,3],amp=1.5)
def cierre(duracion=4):
    d1 >> play('[bbbb] ',dur=duracion)
    b1 >> dbass([0], dur=duracion, sus=duracion,amp=0.6)

# Arrancar de una con bateria
# Corregir volumenes

total = 48
aviso_tiempo_previo = 32
def proximo(etapa,tiempo,nombre):
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//4} beats para el {nombre}"),tiempo - aviso_tiempo_previo//4)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo//2} beats para el {nombre}"),tiempo - aviso_tiempo_previo//2)
    Clock.schedule(lambda : print(f"faltan {aviso_tiempo_previo} beats para el {nombre}"),tiempo - aviso_tiempo_previo)
    Clock.schedule(lambda : cambio_de_etapa(etapa), tiempo)

start = Clock.mod(16) - 0.1
Clock.schedule(intro, start + total*0)
# VERSO
proximo(verso, start + total*1,"verso")
# ESTRIBILLO
proximo(estribillo, start + total*2,"estribillo")
# VERSO
proximo(verso, start + total*3,"verso")
# ESTRIBILLO
proximo(estribillo, start + total*4,"estribillo")
# VERSO
proximo(verso, start + total*5,"verso")
# ESTRIBILLO
proximo(estribillo, start + total*6,"ultimo estribillo!!!")
# CIERRE
proximo(cierre, start + total*7,"cierre")




# COSO MATRIX

def progresion_matriz(acorde,efectos_matriz):
    original = acorde
    transformacion = []
    efectos_lista = []
    for efecto in efectos_matriz:
        for nota in efecto:
            efectos_lista += [nota]    
    acorde_lista = acorde * len(efectos_matriz)
    transformacion = Pattern(acorde_lista) + Pattern(efectos_lista)
    print(f'Armando progresion {transformacion}')
    return transformacion
    
Scale.default='minor'

progresion = [0,0,0,0,-13]
efectos_matriz = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
p1.reset() >> piano(progresion_matriz(progresion, efectos_matriz), dur=P[1,1,1,1,rest(2)]*2,echo=0, glide=[-5,-2,0], glidedelay=[0.5,0], chop=0,oct=5, amp=1)

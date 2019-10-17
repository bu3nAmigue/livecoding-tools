# Ups, downs & stays
# Genera una lista de pitches a partir de un string y (opcional) una raiz
# '=' -> hace que divague en el mismo tono
# '+' -> hace que suba un tono
# '-' -> hace que baje un tono

#las variaciones estan armadas por sets de go que bajan suben o se quedan


#go up
def go_up(nota_base):
    nuevo_up = []
    nuevo_up.append(nota_base + 1)
    nuevo_up.append(nota_base + 1 + PRand(1))
    nuevo_up.append(nota_base + 2 + PRand(2))
    nuevo_up.append(nota_base + 3 + PRand(3))
    return nuevo_up
#go down
def go_down(nota_base):
    nuevo_down = []
    nuevo_down.append(nota_base - 1)
    nuevo_down.append(nota_base - 1 - PRand(1))
    nuevo_down.append(nota_base - 2 - PRand(2))
    nuevo_down.append(nota_base - 3 - PRand(3))
    return nuevo_down
#just stay
def go_stay(nota_base): 
    nuevo_stay = []
    nuevo_stay.append(nota_base + PRand(1) + 1)
    nuevo_stay.append(nota_base)
    nuevo_stay.append(nota_base + PRand(1) + 1)
    nuevo_stay.append(nota_base)   
    return nuevo_stay
#la funcion variaciones transforma un string en un pitch juntando los sets de go
def variaciones(variation_string, raiz=0):
    final_pitch = []
    notita = raiz
    for each in variation_string:
        if each == '+':
            for stuff in go_up(notita):
                final_pitch.append(stuff)
            notita = notita + 3
        elif each == '-':
            for stuff in go_down(notita):
                final_pitch.append(stuff)
            notita = notita - 3
        elif each == '=':
            for stuff in go_stay(notita):
                final_pitch.append(stuff)
    return final_pitch              

#Ejemplo
Scale.default = 'blues'
p1 >> piano(variaciones('====+===+===', raiz=0))
#cada '=' son 4 notas en el tono
#cada '+' es una escalera y aumenta la nota base +3

#Ocupa el pitch de un player, pero se puede mezclar con Root
p1 >> piano(variaciones('+++---===---===+++', raiz=0), root=var([0,1],0.25), dur=1/4, oct=(4,5))

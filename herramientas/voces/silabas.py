import pyphen

pyphen.language_fallback('es_ES_variant1')

dic = pyphen.Pyphen(lang='es')

def esVocal(texto):
    return texto in "aeiouáéíóú"

def findSmallers(silabas):
    smallers = -1
    min = 1000000
    for i in range(len(silabas)-1):
        if min > len(silabas[i]) + len(silabas[i+1]):
            min = len(silabas[i]) + len(silabas[i+1])
            smallers = i
    return i   

def silabas(text,n):
 silabas = list(filter(lambda x : len(x) > 0, dic.inserted(text).replace(" ", "").split("-")))
 if len(silabas) == n:
     return silabas
 elif len(silabas) < n:
     index = 0
     while(len(silabas) < n):
        index = (index + 1) % len(silabas)         
        if esVocal(silabas[index][-1]) and len(silabas[index]) > 1:
            silabas = silabas[:index+1] + [silabas[index][-1]] + silabas[index+1:]
     return silabas
 else:
     while(len(silabas) > n):
         i = findSmallers(silabas)
         silabas = silabas[:i] + [silabas[i] + silabas[i+1]] + silabas[i+2:]
     return silabas


# Ejemplo de uso
## Letra generada con redes neuronales

verse = ["Quiero bailar","Porque si pudiera bailar","Me gustaría hacerlo con vos","Porque soy tu amante","Pero no es asi","no lo es, no lo puedo alejar"]
est = ["Cuando te diga que quiero que bailes","Estarás asombrado","Y te reirás","Porque habrás bailado conmigo"]

flat_list = lambda x: [item for sublist in x for item in sublist]
verse = " ".join(flat_list(map(lambda x : silabas(x,7),verse)))
print(verse)

frase = "Cuando te diga que quiero que bailes Estarás asombrado Y te reirás Porque habrás bailado conmigo"
notas = [-2, 0, -5, -2, 0, 2, 0, 0,0, 0, -2, 2, 0, -2, 0, 2, 0, -2]
frase = " ".join(silabas(frase,len(notas)))
print(frase)
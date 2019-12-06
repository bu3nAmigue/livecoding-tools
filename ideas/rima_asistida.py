import requests, json

def get_rhymes(palabra, cantidad=10):
    response = requests.get(f'https://api.datamuse.com/words?rel_rhy={palabra}&v=es')
    content = json.loads(response.content)[:cantidad]
    palabras = []
    for each in content:
        palabras.append(each['word'])
    return palabras
    
def rimar_ultima(letra):
    letra_split = letra.split(" ")
    ultima_palabra = letra_split[-1]
    nuevas_palabras = get_rhymes(ultima_palabra)
    nuevas_letras = []
    for each in nuevas_palabras:
        nueva_letra = " ".join(letra_split[:-1]+[each])
        nuevas_letras.append(nueva_letra)
        print(nueva_letra)
    return nuevas_letras
    
rimar_ultima("estaba codeando mi disco cuando cayo la tormenta")

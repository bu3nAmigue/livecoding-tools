
#### make_choral() genera acordes a partir de una lista de notas
#
#          
#

Scale.default='minor'

def make_choral(notes, interval=2):
    note_progresion = notes
    chord_interval = interval
    choral_split = []
    for note in note_progresion:
        choral_split.append(note - chord_interval)
        choral_split.append(note)
        choral_split.append(note + chord_interval)
    choral_tuples = []
    for note in note_progresion:
        choral_tuples.append((note - chord_interval, note, note + chord_interval))
    choral_dict = {}
    choral_dict['split'] = choral_split
    choral_dict['tuples'] = choral_tuples
    print(f'Creado choral de {note_progresion}')
    return choral_dict

a = make_choral([0,5,4,2])
p1 >> piano(a['split'], dur=[2/2,3/2])
p2 >> piano(a['tuples'],dur=4)












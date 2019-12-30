
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

Scale.default='major'
a = make_choral([0,7,0,3,0,5,4,2])
p1 >> space(a['split'][8:16],dur=1/2, oct=4, amp=3) + var([0,3,2,1],4)
p2 >> ambi(a['tuples'][3:],dur=4)
p3 >> play('(x|u1|) ', sample=3)
p4 >> piano(Pattern(a['split']).reverse(), dur=8, sus=8, drive=0.4, glide=2, glidedelay=0,vib=0.1, lpf=666)
b = make_choral([0,-1,-2,1])
b1 >> blip(b['tuples'],dur=[1/2,1/4,1/4,rest(1/2)], amp=1).every(8,'stutter',16,dur=8,pan=[1,-1]) + var([0,1,2,3,2,3,4,5],2)

Scale.default='zhi'
c = make_choral([0,4,7,6,4,2],interval=5)
c1 >> karp(c['split'][4:12],dur=[1/2,[rest(1/2),1/2]],amp=2, glide=2, glidedelay=0.8) + var([0,2],8)
c2 >> bell(c['split'][:32],dur=1/2, sus=1/2, oct=4)
c3 >> play('S', sample=3, dur=3)
c4 >> play('X   ',sample=3)

print(Pattern(a['split']))
print(Pattern(b['tuples']))










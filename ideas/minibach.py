Scale.default='major'

#miniBach
base=[0,2]
parte1 = base+[4,7,9]*2
parte2 = base+[5,8,10]*2
parte3 = base+[4,8,10]*2
b1 >> piano(P[parte1*2
    +parte2*2
    +parte3*2
    +parte1*2]
    , dur=1/2)

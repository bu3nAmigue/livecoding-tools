import random as Random
def improvise_drums(sample_list, largo=16, semilla=0):
    Random.seed(semilla)
    drum_base = ''
    generated_drums = []
    for each in sample_list:
        generated_drums.append(each)
    print(f'Improvisando con los samples: {generated_drums}')
    for each in range(largo):
        random_sample = generated_drums[Random.randint(0,len(generated_drums)-1)]
        if Random.randint(0,100) > 70:
            drum_base += (f'[{random_sample}{random_sample}]')
        else:
            drum_base += random_sample
    print(f'Suena: {drum_base}')
    return drum_base
    
dx >> play(improvise_drums('KXr-',semilla=1))

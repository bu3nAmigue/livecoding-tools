import sounddevice as sd
import soundfile as sf
import threading
import time

def find_source(source):  
    devices = sd.query_devices()
    for i, v in enumerate(list(devices)):
        if v["name"] == source:
            return i
print(find_source("system"))

def record(bpms,name):
    time.sleep(0.355)    #time.sleep(1)
    fs=44100
    duration = bpms*60/Clock.bpm
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1,dtype='float64',device=find_source("system"))
    print("RECORDING")
    sd.wait()
    sf.write(FOXDOT_ROOT + "/snd/_loop_/"+name+".wav", myrecording, fs)
    print("FINISHED RECORDING")
record_thread = lambda bpms, name : threading.Thread(target = lambda : record(bpms,name)).start()

def verboseRecord(bpms,nombre):
    start = Clock.mod(bpms)-0.1
    Clock.schedule(lambda : print("4"), start-4)
    Clock.schedule(lambda : print("3"), start-3)
    Clock.schedule(lambda : print("2"), start-2)
    Clock.schedule(lambda : print("1"), start-1)
    Clock.schedule(lambda : record_thread(bpms,nombre), start)

# Ejemplo de uso

## Dejar sonando algo
m1 >> pluck([0,1,2,3,4,5,6,7])

## Grabar durante 8 beats
verboseRecord(8,"test")

## Reproducir la grabación
v1.reload()
v1 >> loop("test",P[0:8])
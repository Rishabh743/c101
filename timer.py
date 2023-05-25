import time 
from playsound import playsound

def countdown(seconds):
    while seconds>0:
        min=int(seconds/60)
        sec=int(seconds%60)
        print(str(min)+":"+str(sec))
        seconds-=1
        time.sleep(1)
    print("timeup")
    playsound("mixkit-sound.wav")
countdown(100)
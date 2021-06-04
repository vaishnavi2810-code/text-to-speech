from tkinter import *
from gtts import gTTS
from playsound import playsound
import pyttsx3

root=Tk()
root.geometry("350x350")
root.title("Text-to-speech")
engine=pyttsx3.init()

Msg=StringVar()
l1=Label(root,text="TEXT-TO-SPEECH")
l1.place(x=20,y=30)
l2=Label(root,text="Enter the text").place(x=20,y=60)
entry_field=Entry(root,textvariable=Msg,width='50')
entry_field.place(x=20,y=100)

def Text_To_Speech():
    Message=entry_field.get()
    engine.say(Message)
    engine.runAndWait()
    #speech=gTTS(text=Message)
    #speech.save('speech.mp3')
    #playsound('speech.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root,text="PLAY",width='4',command=Text_To_Speech).place(x=25,y=140)
Button(root,text="EXIT",width='4',command=Exit).place(x=100,y=140)
Button(root,text="RESET",width='4',command=Reset).place(x=175,y=140)

root.mainloop()

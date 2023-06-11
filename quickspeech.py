import pyttsx3
import speech_recognition as sr 
from time import sleep 
import pyautogui as pg

r = sr.Recognizer()
def Speak(command):
    run = pyttsx3.init()
    run.say(command)
    run.runAndWait()

MyText = ""
def main():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
            Speak(MyText)

            #commands ______________
            #COMMAND OPEN TAB
            if MyText == "open":
                def open():
                    Speak("Name the name of the website you would like to open: ")
                    sleep(2)
                    with sr.Microphone() as source:
                        print("Listening...")
                        audio = r.listen(source)
                        try:
                            tab = r.recognize_google(audio)
                            tab = tab.lower() 
                            pg.press("win")
                            sleep(1)
                            pg.write(tab + ".com")
                            pg.press("Enter")
                        except:
                            Speak("Sorry, could not recognize what you said")
                open()
            #COMMAND SPAM FRIEND BECAUSE WHY NOT?!
            if MyText == "spam":
                def spam():
                    Speak("Please say your message app of choice")
                    with sr.Microphone() as source:
                        print("Listening...")
                        audio = r.listen(source)
                        try:
                            tab = r.recognize_google(audio)
                            tab = tab.lower() 
                            pg.press("win")
                            sleep(1)
                            pg.write(tab)
                            pg.press("Enter")
                            Speak("Please click on the person you would like to spam")
                            sleep(5)
                            for i in range(50):
                                pg.write("Hello. YOU ARE SO MID!!!")
                                pg.press('enter')
                        except:
                            Speak("Sorry, could not recognize what you said")
                spam()
            #COMMAND AUTO SCROLL
            if MyText == "scroll":
                def scroll():
                    Speak("This will scroll for one minute. If you would like to re scroll, just say scroll again. Also, if you would like to temporarily pause the scrolling then hold ctrl on your computer and it will continue the time but not the scrolling so long as you are holding it!")
                    for i in range(120):
                        pg.scroll(-25)
                        sleep(0.5)
                scroll()
            #COMMAND MUSIC 
            if MyText == "music":
                def music():
                    Speak("Please say your music app of choice")
                    with sr.Microphone() as source:
                        print("Listening...")
                        audio = r.listen(source)
                        try:
                            tab = r.recognize_google(audio)
                            tab = tab.lower() 
                            pg.press("win")
                            sleep(1)
                            pg.write(tab)
                            pg.press("Enter")
                        except:
                            Speak("Sorry, could not recognize what you said")
                music()
            #Command talk typing
            if MyText == "voice text":
                def voicetxt():
                    Speak("Speak and whatever you say will be converted into text and written")
                    sleep(2)
                    with sr.Microphone() as source:
                        print("Listening...")
                        audio = r.listen(source)
                        try:
                            tab = r.recognize_google(audio)
                            tab = tab.lower() 
                            sleep(1)
                            pg.write(tab)
                        except:
                            Speak("Sorry, could not recognize what you said")
                voicetxt()
        
        except:
            Speak("Sorry, could not recognize what you said")
while MyText != "quit":
    main()

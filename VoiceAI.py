import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime as dt
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random as r2
import sys
import wolframalpha
import sqlite3 as sq
import customtkinter as ctk
from threading import *
import random as r
import wave as we



from tkinter import *

ctk.set_appearance_mode("dark")

# Create the main window
win = ctk.CTk()
win.title('Gideon AI')
win.geometry('630x700')
win.configure(bg="black")

conn = sq.connect('database.db')
cursor=conn.cursor()

#eid=cursor.execute('''SELECT email_id FROM maildat WHERE U_Name='Aditya';''')
'''eid=str(cursor.fetchone())
eid=eid[2:(len(eid)-3):1]'''
#enc=cursor.execute('''SELECT password FROM maildat WHERE U_Name='Aditya';''')
'''enc=str(cursor.fetchone())
enc=enc[2:(len(enc)-3):1]'''

usertext=StringVar()
comtext=StringVar()

def new_GUI():

    root = ctk.CTk()
    root.geometry('650x700')
    root.title('Commands List')

    cmds="""                 

    1) Search Google keyword
        example: search google python or search google AI assistant
                
    2)Search Wikipedia keyword
        example: search Wikipedia python or search Wikipedia AI

    3)  email to recipient
            recipient-> ROSHAN,ABHISHEK,RANA
            example-> email to roshan

    4)API services-> WOLF-RAM-ALPHA

    5)Google maps keyword
        example: google map delhi

    6)Open Code-> To open Microsoft Visual Code

    7)Open C Drive-> To Open C Drive   

    8)Open D drive-> To Open D Drive

    9)Play music-> To play Music

    10)Play video-> To play Video

    11)Search Youtube keyword
        example: search youtube python or search youtube AI assistant

    12)Open google-> To open google on browser

    13)Open Youtube-> To open youtube on browser

    14)Go Offline/Nothing/Bye-> To close Application

    15)Shutdown-> To shutdown the Operating System 

    16)open ppt-> To Open PowerPoint File

    17)open word-> To Open Word File

    18)open excel-> To Open Excel sheet

    """

    hpframe=LabelFrame(
        root,
        text="Commands:- ",
        font=('young shreiff',12,'bold'),
        highlightthickness=3)
    hpframe.pack(fill='both',expand='yes')

    hpmsg=Message(
        hpframe,
        text=cmds,
        bg='black',
        fg='#7ddbdb'
        )
    hpmsg.config(font=('young shreiff',10,'bold'),justify="left")
    hpmsg.pack(fill='both',expand='no')


    exitbtn = Button(
        root, 
        text='EXIT', 
        font=('#7ddbdb', 11, 'bold'), 
        bg='red', 
        fg='white',
        borderwidth=5,
        command=root.destroy).pack(fill='x', expand='no')

    root.mainloop()


compframe=LabelFrame(
    win,
    text="Gideon ",
    font=('young shreiff',10,'bold'),
    highlightthickness=2)
compframe.pack(fill='both',expand='yes')

left2=Message(
    compframe,
    textvariable=comtext,
    bg='#7ddbdb',
    fg='black',
    justify='left'
    )

left2.config(font=('young shreiff',12,'bold'),aspect=250)
left2.pack(fill='both',expand='yes')

userframe=LabelFrame(
    win,
    text="User",
    font=('young shreiff',10,'bold'),
    highlightthickness=2,)
    
userframe.pack(fill='both',expand='yes')

left1=Message(
    userframe,
    textvariable=usertext,
    bg='black',
    fg='#7ddbdb',
    justify='left'
    )
left1.config(font=('young shreiff',12,'bold'),aspect=250)
left1.pack(fill='both',expand='yes')




engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('497K74-LQ93WJ8229')

voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
comtext.set("""Hello! 
I am your Personal Assistant Gideon 

Click on Start button to give your Commands"""
            )
usertext.set(' ')

def printo(shan):
    global comtext
    comtext.set(shan)
    
 
def speak(audio):
    
    printo(audio+"\n")
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! " +name)

    elif hour>=12 and hour<18:
        speak("Good Afternoon! " +name)   

    else:
        speak("Good Evening! " +name)
        
    speak("""Hello {} 
How can I help you?""".format(name))
    #speak("Click start speaking button to give Commands")
    usertext.set('''  Click start speaking button to give Commands''')


def Name():
    #It takes microphone input from the user and returns string output
    global r,source,audio,query,name
    name=" "
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What is your name")
        printo("Please tell me Your name\n")
        printo("Listening...\n")
        #r.pause_threshold = 1 #bolne a time ruk gaye to 2 sec ruk kar execute karega taki pura phrase complete hojaye
        audio = r.listen(source)

    try:
        printo("Recognizing...\n")    
        name = r.recognize_google(audio, language='en-in') #voice recognize hogi isme english-india mai
        #print(f"User said: {name}\n") #fstring use kiya hai
        

    except Exception as e:
        printo(e)    
        printo("Say that again please...\n") 
        speak("Say that again please...")
        Name() 
        return None
    return name
    wishMe()

def Commands():
    global r,source,audio,query,usertext
    r = sr.Recognizer()
    r.energy_threshold=2500
    with sr.Microphone() as source:
        printo("Listening...\n")
        r.pause_threshold = 1 #bolne a time ruk gaye to 2 sec ruk kar execute karega taki pura phrase complete hojaye
        audio = r.listen(source)

    try:
        printo("Recognizing...\n")
        query = r.recognize_google(audio, language='en-in') #voice recognize hogi isme english-india mai
        usertext.set("User said:"+query+"\n") #fstring use kiya hai

    except Exception as e:
        # print(e)    
        printo("Say that again please...\n") 
        speak("Say that again please...")
        Commands() 
        return query
    return query

def ppt():
    def open_pptx(file_path):
        os.startfile(file_path)
    
    def recognize_speech():
        recognizer = sr.Recognizer()

        try:
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:
                printo("Say the name of the PowerPoint file to open:")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            printo("listening")
            printo("You said : {}\n".format(keyword))
            
            printo("Say the name of the PowerPoint file to open:")
            printo("You said : {}\n".format(keyword))   
            speak('searching on google' +" "+ keyword)

            try:
                text = recognizer.recognize_google(audio).lower()
                return text
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return None
            except sr.RequestError as e:
                print(f"Error connecting to Google API: {e}")
                return None
        except:
            printo("opening\n")

        try:
            text = recognizer.recognize_google(audio).lower()
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")
            return None
    
    def main():
        while True:
            file_name = recognize_speech()

            if file_name:
                # Assuming the PowerPoint files are in the current working directory
                file_path = os.path.join(os.getcwd(), f"{file_name}.pptx")

                if os.path.isfile(file_path):
                    print(f"\nOpening file: {file_path}")
                    open_pptx(file_path)
                    break
                else:
                    print(f"File not found: {file_path}")
    
    if __name__ == "__main__":
        main()



def word():
    def open_pptx(file_path):
        os.startfile(file_path)
    
    def recognize_speech():
        recognizer = sr.Recognizer()

        try:
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:
                printo("Say the name of the Word file to open:")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            printo("listening")
            printo("You said : {}\n".format(keyword))
            
            printo("Say the name of the PowerPoint file to open:")
            printo("You said : {}\n".format(keyword))   
            speak('searching on google' +" "+ keyword)

            try:
                text = recognizer.recognize_google(audio).lower()
                return text
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return None
            except sr.RequestError as e:
                print(f"Error connecting to Google API: {e}")
                return None
        except:
            printo("opening\n")

        try:
            text = recognizer.recognize_google(audio).lower()
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")
            return None
    
    def main():
        while True:
            file_name = recognize_speech()

            if file_name:
                # Assuming the PowerPoint files are in the current working directory
                file_path = os.path.join(os.getcwd(), f"{file_name}.docx")

                if os.path.isfile(file_path):
                    print(f"\nOpening file: {file_path}")
                    open_pptx(file_path)
                    break
                else:
                    print(f"File not found: {file_path}")
    
    if __name__ == "__main__":
        main()



def excel():
    def open_pptx(file_path):
        os.startfile(file_path)
    
    def recognize_speech():
        recognizer = sr.Recognizer()

        try:
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:
                printo("Say the name of the Word file to open:")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            printo("listening")
            printo("You said : {}\n".format(keyword))
            
            printo("Say the name of the PowerPoint file to open:")
            printo("You said : {}\n".format(keyword))   
            speak('searching on google' +" "+ keyword)

            try:
                text = recognizer.recognize_google(audio).lower()
                return text
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return None
            except sr.RequestError as e:
                print(f"Error connecting to Google API: {e}")
                return None
        except:
            printo("opening\n")

        try:
            text = recognizer.recognize_google(audio).lower()
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")
            return None
    
    def main():
        while True:
            file_name = recognize_speech()

            if file_name:
                # Assuming the PowerPoint files are in the current working directory
                file_path = os.path.join(os.getcwd(), f"{file_name}.xlsx")

                if os.path.isfile(file_path):
                    print(f"\nOpening file: {file_path}")
                    open_pptx(file_path)
                    break
                else:
                    print(f"File not found: {file_path}")
    
    if __name__ == "__main__":
        main()




def srch_google():
    #speak("Seaching on Google.....\n")
    #printo("Seaching on Google.....\n")
    #audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        keywords=(text.split(" "))
        printo(keywords)
        del keywords[0]
        del keywords[0]
        printo(keywords)
        
        def listosrting(s):
            str1=" "
            new=str1.join(s)
            return new
        printo(listosrting(keywords))
        keyword=listosrting(keywords)

        printo("You said : {}\n".format(keyword))
        url='https://www.google.co.in/search?q='
        search_url=f'https://www.google.co.in/'+keyword
        speak('searching on google' +" "+ keyword)
        webbrowser.open(search_url)
    except:
        printo("Can't recognize\n")

def a():
    #speak("Seaching on Google.....\n")
    #printo("Seaching on Google.....\n")
    #audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        keywords=(text.split(" "))
        printo(keywords)
        del keywords[0]
        del keywords[0]
        printo(keywords)
        
        def listosrting(s):
            str1=" "
            new=str1.join(s)
            return new
        printo(listosrting(keywords))
        keyword=listosrting(keywords)

        printo("You said : {}\n".format(keyword))
        url='https://in.pinterest.com/search?q='
        search_url=f'https://in.pinterest.com/search?q='
        speak('open pintrest')
        webbrowser.open(search_url)
    except:
        printo("Can't recognize\n")



def srch_google_map():
    #speak(" Searching on Google Map.....")
    #printo("Searching on Google Map.....\n")
    #audio=r.listen(source)
    try:
        text2=r.recognize_google(audio)
        #text="gooe map Taj mahal"
        keywords=(text2.split(" "))
        print(keywords)
        del keywords[0]
        del keywords[0]
        #del keywords[0]
        print(keywords)
        
        def listosrting(s):
            str1=" "
            new=str1.join(s)
            return new
        printo(listosrting(keywords))
        keyword=listosrting(keywords)

        print("You said : {}\n".format(keyword))
        #url='https://www.google.com/maps/place/?'
        search_url=f'http://maps.google.com/?q='+keyword
        speak('searching on google map' +" "+ keyword)
        webbrowser.open(search_url)
    except:
        printo("Can't recognize\n")


def search_yt():
    #speak("searching on youtube.....\n")
    #printo("searching on youtube.....\n")
    try:
        text=r.recognize_google(audio)
        key=(text.split(" "))
        #print(keywords)
        del key[0]
        del key[0]
        #print(keywords)
        
        def lis(s):
            str1=" "
            new=str1.join(s)
            return new
    
        key=lis(key)

        print("You said : {}".format(key))
        url='http://www.youtube.com/results?search_query='
        search_url=f'http://www.youtube.com'+key
        speak('searching on youtube ' +" "+ key)
        webbrowser.open(search_url)
    except:
        print("Can't recognize")

def sendEmail(to, content):
    global eid,enc
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(eid,enc)
    server.sendmail('your email', to, content)
    server.close()

    

def mainfn():
    global query
    if __name__ == "__main__":
        Name()
        wishMe()
    # while True: #while use kiya taki vo jabtak command nahi samjhe tabtak bar bar chale say that again vala
    # if 1:
    
def reco():   
    query = Commands().lower()
    print(query)
    # Logic for executing tasks based on query
    
    if 'search google' in query:
        srch_google()

    elif 'search youtube' in query:
            search_yt()

    elif 'open ppt' in query:
            ppt()
    
    elif 'open word' in query:
            word()

    elif 'open excel' in query:
            excel()

    elif 'search pintrest' in query:
            a()

    elif 'open w3schools' in query:
        speak("opening w3schools ")
        pin='https://www.w3schools.com/'
        webbrowser.open(pin)

    elif 'open qt python' in query:
        speak("opening qt python ")
        pin='https://www.qt.io/qt-for-python/'
        webbrowser.open(pin)

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        printo(results+"\n")
        speak(results)

    elif 'open youtube' in query:
        speak("opening youtube ")
        url='http://www.youtube.com/'
        webbrowser.open(url)

    elif 'open google slides' in query:
        speak("opening google slides ")
        url='https://www.google.com/slides/about/'
        webbrowser.open(url)


    elif 'open national portal' in query:
        speak("opening National portal of India ")
        url='https://www.india.gov.in/'
        webbrowser.open(url)

    elif 'google map' in query:
        srch_google_map()

    elif 'open google' in query:
        speak('opening google')
        webbrowser.open("google.com")

    elif 'go offline' in query:
        speak('ok '+name)
        quit()
        win.destroy()

    elif 'shutdown' in query:
        #self.compText.set('okay')
        speak('okay')
        os.system('shutdown -s')


    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(r2.choice(stMsgs))
    
    elif 'play music' in query:
        music_folder = "C:/Users/Rohit Tambitkar/OneDrive/video/music1.mp3"
        music = ['music1','music2','music3','music4','music5']
        random_music = music_folder + r2.choice(music) + '.mp3'
        os.system(random_music)
        speak('Okay, here is your music! Enjoy!')
    elif 'play video' in query:
            video_folder = "C:/Users/Rohit Tambitkar/Downloads/Luffy vs Kaido [ AMV ] MIDDLE OF THE NIGHT.mp4"
            video = ['Luffy vs Kaido [ AMV ] MIDDLE OF THE NIGHT','video2','video3','video4','video5']
            random_video = video_folder + r2.choice(video) + '.mp4'
            os.system(random_video)
            speak('Okay, here is your video! Enjoy!')


    elif 'open code' in query:
        codePath = "code path"
        os.startfile(codePath)
            
    elif 'open c drive' in query:
        cdrive = "C:"
        speak("openning C Drive....")
        os.startfile(cdrive)

    elif 'open d drive' in query:
        ddrive = "D:"
        speak("openning C Drive....")
        os.startfile(ddrive)
            
    elif 'email to Recievers name' in query:
        try:
            speak("What should I say?")
            content =Commands()
            to = "Recievers Email"    
            sendEmail(to, content)
            speak("Email has been sent!")
            printo("Email has been sent!\n")
        except Exception as e:
            printo(e)
            speak("Sorry! I am unable to send your message at this moment!\n")    

   

    elif 'nothing' in query or 'abort' in query or 'stop' in query:
        speak('okay')
        speak('Bye'+name+', have a good day.')
        win.destroy()
        quit()
        
           
    elif 'hello' in query:
        speak('Hello '+name)

    elif 'bye' in query:
        speak('Bye'+name+', have a good day.')
        win.destroy()
        quit()
        
        #elif 'calculate' or 'solve' or 'what' in query:

    else:
        query = query
        try:
            speak('Searching in API...')
            res = client.query(query)
            results = next(res.results).text
            speak('API says - ')
            speak('please wait.')
            speak(results)
                
        except Exception as e:
                #print(e)
            speak("sorry sir. i can't recognize your command maybe google can handle this should i open google for you?")
            ans=Commands()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                webbrowser.open('www.google.com')
            elif 'no' in str(ans) or 'nah' in str(ans):
                speak("ok disconnecting")
                sys.exit()
            else:
                speak("no respnse i am disconnecting")
                sys.exit()

def exit():
    win.destroy()
    sys.exit()
    #pass

def start():
    Thread(target=mainfn).start()

def speakingbtn():
    Thread(target=reco).start()

# Create a status label
status_label = ctk.CTkLabel(win, text="Welcome to Gideon AI!", font=('#7ddbdb', 12, 'bold'), text_color='#7ddbdb')
status_label.pack(pady=10)

# Create entry fields for user input




# Create buttons using CTkButton
btn = ctk.CTkButton(
    master=win, 
    text='Start!', 
    font=('#7ddbdb', 11, 'bold'), 
    fg_color='black', 
    text_color='#7ddbdb',
    border_width=5,
    command=start)
btn.pack(fill='x', expand=False, pady=5)

btn1 = ctk.CTkButton(
    master=win, 
    text='Start Speaking!', 
    font=('#7ddbdb', 11, 'bold'), 
    fg_color='black', 
    text_color='#7ddbdb',
    border_width=5,
    command=speakingbtn)
btn1.pack(fill='x', expand=False, pady=5)

btn2 = ctk.CTkButton(
    master=win, 
    text='Command List', 
    font=('#7ddbdb', 11, 'bold'), 
    fg_color='black', 
    text_color='#7ddbdb',
    border_width=5,
    command=new_GUI)
btn2.pack(fill='x', expand=False, pady=5)

btn3 = ctk.CTkButton(
    master=win, 
    text='EXIT', 
    font=('#7ddbdb', 11, 'bold'), 
    fg_color='red', 
    text_color='white',
    border_width=5,
    command=exit)
btn3.pack(fill='x', expand=False, pady=5)

# Add a status bar
status_bar = ctk.CTkLabel(win, text="Ready", font=('#7ddbdb', 10), text_color='#7ddbdb', fg_color='black')
status_bar.pack(side='bottom', fill='x')

# Start the main loop
win.mainloop()


import gtts
from gtts import gTTS
#print(dir(gtts))
a = gTTS("Love you Zindagi")
print(a)
a.save("hello.mp3")
'''
from gtts import gTTS
import speech_recognition as sr
import playsound
import uuid
import os
from time import ctime
import webbrowser
import smtplib
#to make sure it listens
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now")
        audio = r.listen(source,phrase_time_limit=5)
    data = ""
    #Exception Handling
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
#listen()

#Responding where we will make our virtual assistant to speak

def respond(String):
    print(String)
    tts = gTTS(text = String,lang = 'en-US')
    tts.save("speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
#Virtual Assistant actions
def virtual_assistant(data):
    """give your actions"""
    if "how are you" in data:
        listening = True
        respond("Good and doing well")
    if "time" in data:
        listening = True
        respond(ctime())
    if "open google" in data.casefold():
        listening = True
    if "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen()
        edict = {'hello':'','new':''} #give mail ids
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("What should i tell that person?")
        message = listen()
        content = 'Subject :{}\n\n{}'.format(subject,message)
        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)
        #identify the server
        mail.ehlo()
        mail.starttls()
        #login
        mail.login('','') #enter mailid and password make sure you enable less secure app access
        mail.sendmail('',toaddr,content) #enter your gmail username
        mail.close()
        respond('Email Sent')
    if "locate" in data:
        webbrowser.open('https://www.google.com/maps/search/'+data.replace("locate",""))
        result = "Located"
        respond("Located {}".format(data.replace("locate","")))
    if "search google" in data.casefold():
        listening = True
        reg_ex = re.search('search google(.*)',data.casefold())
        print(data)
        url = "https://www.google.com/search?q="
        if reg_ex:
            sub = reg_ex.group(1)
            print(sub,type(sub))
        webbrowser.open(url + sub)
        result = "Success"
        respond("Search for {} complete".format(sub))  
    if "stop" in data:
        listening =False
        print("Listening Stopped")
        respond("Okay done take care...")
    try:
        return listening
    except UnboundLocalError:
        print("Timedout")
#time.sleep(8)
respond("Hey! how are you")
listening = True
while listening ==True:
    data = listen()
    listening = virtual_assistant(data)
'''    











    
    
        
    








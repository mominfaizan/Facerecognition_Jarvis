import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import numpy
import pyautogui as p 
import cv2

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


# speaking voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wishing 

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good morning sir")
    if hour >=12 and hour<18:
        speak("Good Afternoon sir")
    if hour >=20 and hour<24:
        speak("Good night sir") 
    speak("i am jarvis, how can i help you")

# command of task 

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        # r.energy_threshold=200
        audio =r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print("User said:",query)
    except Exception as e:
        # print(e)
        print("Sorry, something went wrong please say again....")
        return "None"
    return query



def taskmanger(flag):
  if not flag:
        return
  elif flag:  
    wishMe() 
    while True:
        speak("hello faizan how are you")
        query= takecommand().lower()
     
        if query == 'stop':
          break
 

        if 'how are you' in query:
           speak("I am find sir how are you?")
        
        elif 'i am fine' in query:
           speak("glad to know that you are great")   
        elif  'tell me about yourself' in query or 'who are you' in  query:
           speak("i am jarvis ai.which made by mohammadfaizan. i try to make thing easy")
         
        elif 'you need to break' in query:
           speak("ok sir you can call me anytime")
           break
 
    #   open web site
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")       
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open mail' in query:
            webbrowser.open("mail.com")       
        
        # music 
        elif 'play music' in query:
            music_dr='C:\\music'
            songs=os.listdir(music_dr)
            # print(songs)
            if 'basti' in query:
             os.startfile(os.path.join(music_dr,songs[0]))
            if 'tarfa' in query:
             os.startfile(os.path.join(music_dr,songs[1]))
            if 'kahani' in query:
             os.startfile(os.path.join(music_dr,songs[2]))
            if 'ishq' in query:
             os.startfile(os.path.join(music_dr,songs[3]))
            if 'sochta' in query:
             os.startfile(os.path.join(music_dr,songs[4]))
            else:
             os.startfile(os.path.join(music_dr,songs[3]))
            break


def main():
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trained_model2.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    names = ['FAIZAN']  # Add names of recognized persons here

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(converted_image, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])

            if id < len(names):
                if accuracy < 70:  # Adjust the recognition confidence threshold as needed (e.g., 70 or 80)
                    name = names[id]
                    # person=False
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    # flag=True
                    print(name)
                    break   
                else:
                    name = "Unknown"
                    print(name)
                    accuracy = "  {0}%".format(round(100 - accuracy))
            else:
                name = "Unknown"
                print(name)
                accuracy = "  {0}%".format(round(100 - accuracy))

            cv2.putText(img, name, (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == ord('q'):  # Press 'q' to quit
            break
        # taskmanger(flag)
    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()    
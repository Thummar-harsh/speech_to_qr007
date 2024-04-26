import qrcode
import speech_recognition as sr
import pyaudio 
def takeAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
        
        print('recg...')
        q = r.recognize_google(audio,language = 'en-in')
        print(q)
    return q
X=takeAudio()

img = qrcode.make(X)
type(img)  # qrcode
img.save("nova.png")
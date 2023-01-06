#Importing gTTs for converting the text entered, into audio which can be saved as a mp3 file 
from gtts import gTTS

#open the text file to convert to an audio file 
file = open('demo.txt','r')
file = file.read().replace('\n',' ') 
language = "en" 
speech = gTTS(text=str(file), lang=language , slow=False) 
print(speech)
speech.save("audio.mp3")
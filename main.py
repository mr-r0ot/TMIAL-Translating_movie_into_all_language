import os


os.system("pip install moviepy")
os.system("pip install moviepy --upgrade")
os.system("pip install SpeechRecognition")
os.system("pip install googletrans==4.0.0-rc1")
os.system('cls || clear')


print("""
      
      
      
      Translation of the film into all languages!


       coded By @black_nicola(TELEGRAM)
      
      
      
    """)


from moviepy.editor import VideoFileClip
import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator



video_path = input("Enter the path to the video file: ")
video = VideoFileClip(video_path)



audio = video.audio
audio.write_audiofile("audio.mp3")


recognizer = sr.Recognizer()
audio_file = sr.AudioFile("audio.mp3")

with audio_file as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)

with open("audio.txt", "w") as file:
    file.write(text)


translator = Translator()
destination_language = input("Enter the destination language: ")
translated_text = translator.translate(text, dest=destination_language).text

with open("trans_audio.txt", "w") as file:
    file.write(translated_text)


subclip = mp.TextClip(translated_text, fontsize=70, color='white', bg_color='black').set_pos('center')
video = mp.CompositeVideoClip([video, subclip.set_duration(video.duration)])
video.write_videofile("output.mp4", codec="libx264")
print('Ok!')

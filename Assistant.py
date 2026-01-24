import tkinter as tk
import threading
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

recognizer = sr.Recognizer()

def speak(text):
    tts = gTTS(text)
    tts.save("voice.mp3")
    playsound.playsound("voice.mp3", True)
    os.remove("voice.mp3")

def assistant_loop():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        speak("How can I assist you")

        while True:
            try:
                app.after(0, lambda: status_label.config(text="Listening"))
                audio = recognizer.listen(source, phrase_time_limit=4)

                app.after(0, lambda: status_label.config(text="Recognizing"))
                command = recognizer.recognize_google(audio).lower()

                if command == "hello":
                    speak("Hello. How can I assist you")

                elif command == "time":
                    now = datetime.now()
                    speak(f"The time is {now.strftime('%I:%M %p').lstrip('0')}")        

                elif command == "date":
                    speak(datetime.now().strftime("Today's date is %d %B %Y"))

                elif command == "exit":
                    speak("Goodbye")
                    stop()

                else:
                    speak("Command not recognized")

            except sr.UnknownValueError:
                speak("I could not understand that")

            except sr.RequestError:
                speak("Speech service unavailable")


def stop():
    global running
    running = False
    app.quit()


app = tk.Tk()
app.title("Online Voice Assistant")
app.geometry("300x150")

status_label = tk.Label(app, text="Idle", font=("Arial", 12))
status_label.pack(pady=20)

exit_button = tk.Button(app, text="Exit", command=stop)
exit_button.pack()

threading.Thread(target=assistant_loop, daemon=True).start()

app.mainloop()

import speech_recognition as sr

def get_voice_command():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Speak your command...")
            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command

    except sr.WaitTimeoutError:
        print("No speech detected (timeout)")
        return ""

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError:
        print("API error")
        return ""

    except OSError:
        print("Microphone not available")
        return ""
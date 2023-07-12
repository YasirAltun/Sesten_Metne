import speech_recognition as sr

r = sr.Recognizer()

a = sr.AudioFile('videoplayback.WAV')

with a as source:
    audio = r.listen(source)
    try:
        text = r.recognize_sphinx(audio,language="en-US")
        print("Dönüşüm başarılı:")
        print(text)
    except sr.UnknownValueError as e:
        print("Ses tanınamadı: {0}".format(e))
    except sr.RequestError as e:
        print("Ses tanıma servisine erişilemiyor; {0}".format(e))
    except Exception as e:
        print("Bir hata oluştu: {0}".format(e))
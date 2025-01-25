import requests
import pyttsx3

# api url
url = "https://zenquotes.io/api/random"
response = requests.get(url)
engine = pyttsx3.init() # implement a audio model 

key = int(input("To Generate a rondom quote press 1 :"))

if(key == 1):
    if(response.status_code == 200):
        data = response.json()
        quote = f"{data[0]['q']} -- {data[0]['a']}"
        print(quote)
        engine.say(quote)
        engine.runAndWait()
    else:
        print("Error")
else:
    print("Error")


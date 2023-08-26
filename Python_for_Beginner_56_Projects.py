# 1. Number Guessing Game

import random

n = random.randrange(1, 10)
guess = int(input("Enter any number: "))
while n != guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    if guess > n:
        print("Too high")
        guess = int(input("Enter number again: "))
    else:
        break
      
print("You guessed it right!")
print(n)

# -------------------------------------------------------- #

# 2. Caculate Mean, Median and Mode

# Mean
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1)/len(list1)
print("mean: ", mean)

# Median
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
  
print("median: ", median)

# Mode
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i] += 1

mode = -1
frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
      
print("mode: ", mode)
print("frequency: ", frequency)

# -------------------------------------------------------- #

# 3. Password Authentication System (He thong xac thuc mat khau)

import getpass
import pwinput

database = {"anhtu1": "123456", "anhtu2": "654321"}
username = input("Enter Your Username : ")
# password = getpass.getpass("Enter Your Password : ")
password = pwinput.pwinput("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            # password = getpass.getpass("Enter Your Password Again : ")
            password = pwinput.pwinput("Enter Your Password Again : ")
        break
      
print("Verified")

# -------------------------------------------------------- #

# 4. Send Automatic Emails

import os
import random
import smtplib

def automatic_email():
    user = input("Enter Your Name >>: ")
    email = input("Enter Your Email >>: ")
    message = (f"Dear {user}, Welcome to Thecleverprogrammer")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your Gmail Account", "Your App Password")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!")

automatic_email()

# -------------------------------------------------------- #

# 5. Age Calculator

def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)

ageCalculator(1999, 8, 22)

# -------------------------------------------------------- #

# 6. Group Anagrams (Dao ngu)

from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]

print(group_anagrams(words))

# -------------------------------------------------------- #

# 7. Find Missing Number

def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output

listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(findMissingNumbers(listOfNumbers))

# -------------------------------------------------------- #

# 8. Group Elements of Same Indices

inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputLists = []
index = 0

for i in range(len(inputLists[0])):
    outputLists.append([])
    for j in range(len(inputLists)):
        outputLists[index].append(inputLists[j][ index])
    index = index + 1
  
a, b, c = outputLists[0], outputLists[1], outputLists[2]
print(a, b, c)

# -------------------------------------------------------- #

# 9. Calculate Execution Time of a Python Program

from time import time
start = time()

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)

# -------------------------------------------------------- #

# 10. Count Number of Words in a Column

import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding = 'latin1')
print(data.head())

data["Number of Words"] = data["Article"].apply(lambda n: len(n.split()))
print(data.head())

# -------------------------------------------------------- #

# 11. Rock Paper Scissors Game (da, giay, keo)

import random

choices = ["Rock", "Paper", "Scissors"]
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    computer = random.choice(choices)
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break

# -------------------------------------------------------- #

# 12. Print Emojis (bieu tuong cam xuc)

import emoji

print(emoji.emojize("I love reading books:books:"))
print(emoji.emojize("Some people have a very sensitive heart:red_heart:, please be kind with them.:hibiscus:"))

# -------------------------------------------------------- #

# 13. Correct Spellings (sua loi chinh ta)

from spellchecker import SpellChecker
corrector = SpellChecker()

word = input("Enter a Word : ")
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)

# -------------------------------------------------------- #

# 14. Scraping GitHub Profile (lấy avatar trong github)

import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/Artubk"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]

print(profile_picture)

# -------------------------------------------------------- #

# 15. Visualizing Linear Relationships

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv", encoding = 'latin1')
data = data.dropna()
print(data.head())

# figure = px.scatter(data_frame = data,
#                     x="Impressions",
#                     y="Likes",
#                     size="Likes",
#                     trendline="ols",
#                     title = "Relationship Between Likes and Impressions")
# figure.show()

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Relationship Bewtween Likes & Impressions")
sns.regplot(x="Impressions", y="Likes", data=data)
plt.show()

# -------------------------------------------------------- #

# 16. Generate Text (tu dong tao van ban)

from transformers import pipeline
model = pipeline("text-generation", model = "gpt2")

sentence = model("Hi, My name is Anh Tu, I am here",
                 do_sample=True, top_k=50,
                 temperature=0.9, max_length=100,
                 num_return_sentences=2)

for i in sentence:
  print(i["generated_text"])

# -------------------------------------------------------- #

# 17. Scrape Table from a Website

import urllib.request
import pandas as pd

url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

with urllib.request.urlopen(url) as i:
    html = i.read()

data = pd.read_html(html)[0]
print(data.head())

data.to_csv("programming.csv")

# -------------------------------------------------------- #

# 18. Extract Text From PDF (trich xuat van ban tu PDF)

import PyPDF2
pdf = open("CV.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)
page = reader.pages[0]
print(page.extract_text())

# -------------------------------------------------------- #

# 19. Reverse a String

def reverse_string(string):
    return string[::-1]

a = "uT hnA neyugN"
print(reverse_string(a))

# -------------------------------------------------------- #

# 20. SequenceMatcher

from difflib import SequenceMatcher
text1 = "My Name is Anh Tu"
text2 = "Hi, My Name is Anh Tu"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")

text3 = "My Name is Anh Tu"
text4 = "I like Artificial Intelligence"
sequenceScore = SequenceMatcher(None, text3, text4).ratio()
print(f"Both are {sequenceScore * 100} % similar")

# -------------------------------------------------------- #

# 21. QA Code

import pyqrcode
import png
link = "https://www.instagram.com/_nguyenphuongnhi_02/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)

# -------------------------------------------------------- #

# 22. Decode a QR Code

from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR = decode(Image.open('instagram.png'))
print(decocdeQR[0].data.decode('ascii'))

# -------------------------------------------------------- #

# 23. Create Dummy Data (tao data gia)

from faker import Faker
import pandas as pd
fake = Faker()

print(fake.name())
print(fake.address())
print(fake.text())

data = [fake.profile() for i in range(50)]
data = pd.DataFrame(data)
print(data.head())

# -------------------------------------------------------- #

# 24. Remove Cuss Words

from better_profanity import profanity
text = "Please leave me alone and just piss off"
censored = profanity.censor(text)
print(censored)

# -------------------------------------------------------- #

# 25. Find Duplicate Values

def find_duplicates(x):
    length = len(x)
    duplicates = []
    for i in range(length):
        n = i + 1
        for a in range(n, length):
            if x[i] == x[a] and x[i] not in duplicates:
                duplicates.append(x[i])
    return duplicates
names = ["Aman", "Akanksha", "Divyansha", "Devyansh",
         "Aman", "Diksha", "Akanksha"]
print(find_duplicates(names))

# -------------------------------------------------------- #

# 26. Detect Questions

import nltk
# nltk.download()
nltk.download('punkt')

from nltk.tokenize import word_tokenize
question_words = ["what", "why", "when", "where",
             "name", "is", "how", "do", "does",
             "which", "are", "could", "would",
             "should", "has", "have", "whom", "whose", "don't"]

question = input("Input a sentence: ")
question = question.lower()
question = word_tokenize(question)

if any(x in question[0] for x in question_words):
    print("This is a question!")
else:
    print("This is not a question!")

# -------------------------------------------------------- #

# 27. Voice Recorder

import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    print("Recording Started…")
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording Finished")

voice_recorder(10, "record.wav")

# -------------------------------------------------------- #

# 28. Reading and Writing CSV Files

import csv
import pandas as pd

writing a csv file
data = {"Name": ["Aman", "Diksha", "Akanksha", "Sajid", "Akshit"],
        "Age": [23, 21, 25, 23, 22]}
data = pd.DataFrame(data)
data.to_csv("age_data.csv", index=False)
print(data.head())

reading a csv file
data = pd.read_csv("age_data.csv")
print(data.head())

# -------------------------------------------------------- #

# 29. Box Plot

import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")
print(data.head())

import plotly.express as px
fig = px.box(data, y="Radio")
fig.show()

# -------------------------------------------------------- #

# 30. Send Instagram Messages

from instabot import Bot
bot = Bot()

bot.login(username="Your Username", password="Your Password")
bot.send_message("Hi Brother", ["Receiver's Username"])

# -------------------------------------------------------- #

# 31. LCM(Least Common Multiple): tim so nho nhat la boi cua nhieu so

def least_common_multiple(a, b):
    greater = 0
    if a > b:
        greater = a
    elif b > a:
        greater = b
    while(True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm

print(least_common_multiple(10, 12))

# -------------------------------------------------------- #

# 32. Price Elasticity of Demand

import pandas as pd

data = pd.DataFrame({"Demand": [20, 30, 31, 33, 30, 33, 35],
                     "Price": [2000, 1800, 1850, 1700, 1800, 1700, 1600]})
print(data)

data["% Change in Demand"] = data["Demand"].pct_change()
data["% Change in Price"] = data["Price"].pct_change()
print(data)

data["Price Elasticity"] = data["% Change in Demand"] / data["% Change in Price"]
print(data)

# -------------------------------------------------------- #

# 33. Find the Most Frequent Words in a File

words = []
with open("path_file.txt", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
top5 = counts.most_common(5)
print(top5)

# -------------------------------------------------------- #

# 34. Find the Number of Capital Letters in a File

with open("path_file.txt") as file:
    count = 0
    text = file.read()
    for i in text:
        if i.isupper():
        # if i.islower():
            count += 1
    print(count)

# -------------------------------------------------------- #

# 35. Index of Maximum Value in a Python List

def maximum(x):
    maximum_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] > x[maximum_index]:
            maximum_index = current_index
        current_index = current_index + 1
    return maximum_index
a = [23, 76, 45, 20, 70, 65, 15, 54]
print(maximum(a))

# -------------------------------------------------------- #

# 36. Index of Minimum Value in a Python List

def minimum(x):
    minimum_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] < x[minimum_index]:
            minimum_index = current_index
        current_index = current_index + 1
    return minimum_index
a = [23, 76, 45, 20, 70, 65, 15, 54]
print(minimum(a))

# -------------------------------------------------------- #

# 37. Animated Scatter Plot

import plotly.express as px
data = px.data.gapminder()
print(data.head())

fig = px.scatter(data, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="country", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
fig.show()

# -------------------------------------------------------- #

# 38. Create Font Art

import pyfiglet
font = pyfiglet.figlet_format('Nguyen Anh Tu')
print(font)

# -------------------------------------------------------- #

# 39. Collage Maker
# ????????????????????????????????????????????????????????? #
from PIL import Image
import numpy as np
def collage_maker(image1, image2, name):
    i1 = np.array(image1)
    i2 = np.array(image2)
    collage = np.vstack([i1, i2])
    image = Image.fromarray(collage)
    image.save(name)

# To Run The Above Function
collage_maker("image1.jpg", "image2.jpg", "new.jpg")
# ????????????????????????????????????????????????????????? #

# from PIL import Image
# image = Image.open('hinh-nen-rong-dragon-fantasy-2.jpg')
#
# from numpy import asarray
# data = asarray(image)
# print(data)
# print(data.shape)
#
# from keras.preprocessing.image import load_img
# from keras.preprocessing.image import img_to_array
# img = load_img("aman.png")
# data = img_to_array(img)
# print(data)

# -------------------------------------------------------- #

# 40. Phone Number Details

import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number = "+9185XXXXXXXX"
number = ph.parse(number)
print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number, "en"))
print(geocoder.description_for_number(number, "en"))

# -------------------------------------------------------- #

# 41. Print a Calendar

import calendar
print(calendar.month(2023, 8))

# -------------------------------------------------------- #

# 42. Internet Speed Test

import numpy as np
import speedtest

wifi  = speedtest.Speedtest()
print("Wifi Download Speed is ", np.around(wifi.download()/1e6, 2), "Mbps")
print("Wifi Upload Speed is ", np.around(wifi.upload()/1e6, 2), "Mbps")

# -------------------------------------------------------- #

# 43. Text to Handwriting

import pywhatkit as kit
import cv2

kit.text_to_handwriting("Hope you are doing well", save_to="handwriting.png")
img = cv2.imread("handwriting.png")
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -------------------------------------------------------- #

# 44. Shutdown Computer

import os
def shutdown_PC():
    # os.system("shutdown /s /r /t 0 /f")
    # os.system("shutdown /s /t 60 /c May tinh se tat hay luu lai cong viec cua ban")
    os.system("shutdown /s /t 60")
shutdown_PC()

def cancel_shutdown_PC():
    os.system("shutdown /a")
cancel_shutdown_PC()

# -------------------------------------------------------- #

# 45. Defang IP Address

def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
ipaddress = ip_address("1.1.2.3")
print(ipaddress)

# -------------------------------------------------------- #

# 46. Count Character Occurrences

def count_characters(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
print(count_characters("Nguyen Anh Tu"))

# -------------------------------------------------------- #

# 47. Pyramid Pattern

def pyramid_pattern(n):
    a = 2 * n-2
    for i in range(0, n):
        for j in range(0, a):
            print(end=" ")
        a = a-1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
print(pyramid_pattern(10))

# -------------------------------------------------------- #

# 48. Plotting Annotations

import matplotlib.pyplot as plt
x = [3, 5, 7, 8, 4]
y = [5, 3, 7, 8, 2]
labels = ["Jan", "Feb", "Mar", "April", "May"]
plt.scatter(x, y)
for i, j in enumerate(labels):
    plt.annotate(j, (x[i]+0.10, y[i]), fontsize=10)
plt.show()

# -------------------------------------------------------- #

# 49. Create Acronyms

user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

# -------------------------------------------------------- #

# 50. Alarm Clock

import os
from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    print(now)
    print(current_hour)
    print(current_minute)
    print(current_seconds)
    print(current_period)

    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    audio_file = os.path.dirname(__file__) + '\\Analog-watch-alarm-sound.mp3'
                    playsound(audio_file)
                    break

# 09:12:30 AM

# -------------------------------------------------------- #

# 51. Email Slicer

email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)

# -------------------------------------------------------- #

# 52. Generate Password

import random
passlen = int(input("enter the length of password: "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)

# -------------------------------------------------------- #

# 53. Create a Quiz Game

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again \n")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is: ", answer)

score = 0
print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? \n")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? \n")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the larget animal? \n")
check_guess(guess3, "Blue Whale")
print("Your Score is " + str(score))

# -------------------------------------------------------- #

# 54. Print Colored Text

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+"Hi My name is Anh Tu "+ Fore.YELLOW+ Back.BLUE+"I am learning python")
print(Back.CYAN+"Hi My name is Anh Tu")
print(Fore.RED + Back.GREEN+ "Hi My name is Anh Tu")

# -------------------------------------------------------- #

# 55. BMI Calculator

Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)

if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else: print(("enter valid details"))

# -------------------------------------------------------- #

# 56. Treemap

import plotly.graph_objects as go
fig = go.Figure(go.Treemap(
    labels = ["A","B", "C", "D", "E", "F", "G", "H", "I"],
    parents = ["", "A", "A", "C", "C", "A", "A", "G", "A"]
))
fig.show()

# -------------------------------------------------------- #

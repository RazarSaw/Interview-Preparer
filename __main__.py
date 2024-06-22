import pyttsx3 #type: ignore
import random
import os

engine = pyttsx3.init() # object creation

questions = [
"Why do you want to work for this company?",
"What are you looking to gain from working with our company?",
"What are your greatest strengths?",
"What do you consider to be your weakness?",
"Why should we hire you?",
"Why do you want this job?",
"Tell me about a challenge or conflict you ve faced, and how you dealt with it.",
"How do you deal with pressure or stressful situations?",
"If a customer comes back and yells at you for making a mistake, how are you going to deescalate the situation? What steps are you going to take?",
"What do you do with your personal time?"
]

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 160)     # setting up new voice rate
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[random.randint(0, 1)].id)

engine.say("Tell me about yourself")
engine.runAndWait()

input("Press any key to continue | ")

available_numbers = list(range(len(questions)))  # Numbers from 0 to 10
picked_numbers = set()  # To keep track of picked numbers

for x in range(random.randint(5, 8)):
  number = random.choice(available_numbers)
  print(questions[number])
  engine.say(questions[number])
  engine.runAndWait()
  
  os.system('cls' if os.name == 'nt' else 'clear')
  input("Press any key to continue | ")
  
  picked_numbers.add(number)
  available_numbers.remove(number)
  
engine.say("Do you have any questions for me?")
engine.runAndWait()

# Task 1 code correction
weather = "sunny"

if weather == "sunny":
   print("Wear sunglasses!")
else:
   print("Take an umbrella!")




# task 2 your mood today
user = input("are you happy or sad\n")

if user == "sad":
   print("I hope your day gets better!")
elif user == "happy":
  print( "That's great to hear!")



#  task 1 and 2  did this myself i got bored lol
name = input("what is your name\n")
user = input(f"are you happy or sad {name}?\n")
weather = input(f"is it sunny or raining {name}?\n")
emotions = ["angry", "excited"]

 

if user.lower() in emotions:
   print(f"I see you're {user.lower()}, {name}")
if user.lower() == "happy":                                         
   print(f"That's great to hear {name}!")
elif user.lower() == "sad":
   print(f"I hope your day gets better {name}!")
else:
   print(f"I didn't understand {name}\n {user} :( is not  happy or sad")
if weather.lower() == "sunny":
    print(f"Wear sunglasses {name} !it is {weather}")
elif weather.lower() == "raining":
   print(f"and Take an umbrella {name}! it is {weather}")
else:
   print(f"I didn't recognize that {name}\n {weather} is not a response \n please respond with sunny or raining")




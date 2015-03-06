'''
Student: Laura Moser
Project: Mad-Lib Assignment
Class: Design Patterns for Web Programming
'''

print("I would like to tell you an original fairytale story, but first I need you to answer some questions! I'll keep it"
      " short promise, but it'll be worth it in the end! ")

#User Inputs

first_name = raw_input("Enter your first name: ")

friend_name = raw_input("Enter a friend's name: ")

gender = raw_input("Enter your gender (Male or Female): ")

age = raw_input("Enter your age: ")

city = raw_input("What city were you born in? ")

num1 = raw_input("Choose a number between 1 and 10: ")

num2 = raw_input("Choose another number between 1 and 5: ")


#Array of Fairy Tale Creatures

creatures = ["Dwarfs", "Elves", "Fairies", "Gnomes", "Ogres", "Trolls"]

#Dictionary of Classic Fairytale Characters

travel = dict() #creates dictionary object
travel = {"Wizard of Oz":"Ruby Red Slippers", "Jack and the Beanstock":"Magic Beans", "Narnia":"Magic Wardrobe"}


#Calculation to figure number of 'Minutes'

minutes = num1 * num2




#Conditional Statements for Gender on rather to use he/she and boy/girl in the story.

pronoun = ""

if gender == "Male":
    pronoun = "He"
elif gender == "Female":
    pronoun = "She"

pronoun2 = ""

if gender == "Male":
    pronoun2 = "boy"
elif gender == "Female":
    pronoun2 = "girl"




#TheStory -------


message = '''
Once upon a time, in a kingdom far away from her own land {pronoun}, awoke with a daze. {pronoun} looked up and
didn't recognize where {pronoun} was at, it was a strange land! After walking for {minutes} minutes, {pronoun} came upon
a dirt road and saw a horse and carriage. {pronoun} waved to get this persons attention.

{friend_name} slowed to a stop and said "What is your name {pronoun2}!?"

{first_name} replied "My name is {first_name}, I am lost - can you help me?"

{friend_name} answered "There is a local tavern north, I am headed that way I will drop you off." {friend_name} not wanting
 any trouble said "That is the best I can offer you."

{first_name} replied "Thank you so much! Can you tell me where I am at, what land is this?"

{friend_name} answered "The Enchanted Forest of course!, What land are you from?"

{friend_name} had climbed on to the carriage, and quickly replied "The ENCHANTED FOREST! I need to find some


'''

message = message.format(**locals())

print(message)
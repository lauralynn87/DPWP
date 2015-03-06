'''
Student: Laura Moser
Project: Mad-Lib Assignment
Class: Design Patterns for Web Programming
'''

print("I would like to tell you an original fairytale story, but first I need you to answer some questions! I'll keep it short promise, but it'll be worth it in the end! ")

#User Inputs

first_name = raw_input("Enter your first name: ")

friend_name = raw_input("Enter a friend's name: ")

gender = raw_input("Enter your gender (Male or Female): ")

age = raw_input("Enter your age: ")

city = raw_input("What city were you born in? ")


#Array of Fairy Tale Creatures

creatures = ["Dwarfs", "Elves", "Fairies", "Gnomes", "Ogres", "Trolls"]





#Conditional Statements for Gender on rather to use he/she and boy/girl in the story.

pronoun = ""

if gender == "Male":
    pronoun = "he"
elif gender == "Female":
    pronoun = "she"

pronoun2 = ""

if gender == "Male":
    pronoun2 = "boy"
elif gender == "Female":
    pronoun2 = "girl"




#TheStory -------


message = '''



'''

message = message.format(**locals())

print(message)
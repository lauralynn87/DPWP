'''
Student: Laura Moser
Project: Mad-Lib Assignment
Class: Design Patterns for Web Programming
'''

print("I would like to tell you an original fairytale story, but first I need you to answer some questions! I'll keep it"
      " short promise, but it'll be worth it in the end! ")

# User Inputs

char1 = raw_input("Enter your first name: ")
char2 = raw_input("Enter a male friend's name: ")
gender = raw_input("Enter your gender (Male or Female): ")
city = raw_input("What city were you born in? ")
num1 = int(input("Enter first number between 1 and 10: "))
num2 = int(input("Enter second number between 1 and 5: "))
char3 = raw_input("Name of your favorite male fairy tale character? ")
story = raw_input("Favorite Disney fairy tale? ")

chant = "There's no place like home\n"*3

#Array of Fairy Tale Creatures

creatures = ["Dwarfs", "Elves", "Fairies", "Gnomes", "Ogres", "Trolls"]

#Dictionary of Magical Transportation Devices

travel = dict()

travel['opt1'] = "ruby red slippers"
travel['opt2'] = "magic beans"
travel['opt3'] = "magic wardrobe"


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


madlib = '''
Once upon a time, in a kingdom far away from her own land, {char1} awoke with a daze. {pronoun} looked up and
didn't recognize where {pronoun} was at, it was a strange land.

After walking for approximately {minutes} minutes, {pronoun} came upon a dirt road and saw a horse and carriage.
{pronoun} waved to get this persons attention.

{char2} slowed to a stop and said "What is your name {pronoun2}!?"

{char1} replied "My name is {char1}, I am lost - can you help me?"

{char2} answered "There is a local tavern north, I am headed that way I will drop you off." {char2} not wanting
any trouble said "That is the best I can offer you."

{char1} replied "Thank you so much! Can you tell me where I am at, what land is this?"

{char2} answered "The Enchanted Forest of course!, What land are you from?"

{char1} had climbed on to the carriage, and quickly replied "The ENCHANTED FOREST! I need to find some {travel[opt1]}, {travel[opt2]}, or {travel[opt3]}!"

{char2} looked at his riding companion strangely, and knew his first instincts were right. Something was not right with this person. He wanted to tell the
Evil Queen at once, so as to maybe get a reward. He hurried on to the local tavern, and they rode in silence.

{char1} realized was not in {city} anymore and would have to relay on her fairytale knowledge, if she wanted to arrive home safely!

After what seemed like hours, they finally arrived at the tavern. {char2} said "This is where I leave you. I'm sorry but I must be going. I wish you safe travels, hope you find your way."

{char1} said "Thank you my friend, I understand."

{char1} stepped into the tavern, and couldn't believe what she say. Never before had she seen real live {creatures} and other mystical creatures before.
{char1} see's {char3} in the corner by himself and recognizes him from {story} that {pronoun} watched as a child.

{char1} goes over too {char3} and says "Hi my name is {char1} and I am lost. I am from another world and need to find my way home. I've heard of tales of your {story} in my world, I was hoping you would help me. I am looking for anything like {travel[opt1]}, {travel[opt2]}, or {travel[opt3]}..Can you help me?" {char1} stops rambling and finally looks at {char3} closely who is shocked, but smirking sort of.

{char3} says "Well it just so happens that I have a pair of {travel[opt1]}, but if you've heard of me, then you know I like making deals, and everything comes at a price... "

{char1} wairy of this person, did know this but was desperate to get home. "What do you want?"

{char3} "That is the beauty of it. For now a I.O.U., I have to come to that world of yours one day, and when I do I'm sure I'll need some assistance. I'll come to collect. Be ready when I do."

The next thing {char1} saw was a note that said "Place the slippers on and repeat this 3x"

{chant}

{char2} Shouts "Hey wake up {char1}!"

{char1} awakes with a jolt and says "Huh?!"

{char2} laughing "You fell asleep watching Once Upon a Time again didn't you?"

"I guess so" {char1} says kinda of dazed, and still sleepy. About to turn back over and go back to sleep, she looks down and notice the red slippers on her feet.

'''

#Printing of the Madlib Story

madlib = madlib.format(**locals())

print madlib
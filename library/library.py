'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Reusable Library (Week 3)
Date: 03/18/15
'''

class TvSize(object):
    def __init__(self):
        #define variables // will need to make private before turning in.
        self.distance = 0
        self.resolution = ""

    def min_size(self):
        #divide user data by 3
        min = distance / 3
        return min

    def max_size(self):
        #divide user data by 1.5
        max = distance / 1.5
        return max

    def reso(self):
        # First checks to see if user data is less than 42 inches - if so will print message.
        # Than checks to see what resolution user selected if they selected 4K Ultra than the message 'You have chosen the recommended resolution'
        if distance < 42 and resolution == "480p" or "720p" or "1080p":
             print ("You need to upgrade to 4K Ultra HD for the best Experience!")
        elif resolution == "4K Ultra":
            print ("You've chosen the correct Resolution for your viewing distance!")
        elif distance > 42:
            print ("The Resolution you've chosen is fine for your viewing distance.")
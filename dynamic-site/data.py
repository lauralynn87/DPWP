'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Dynamic Website (Week 4)
Date: 03/25/15
'''

class Portfolio(object):
    def __init__(self):
        # Sets up the attributes to be called by the objects

        #items will be the images
        self.item1 = ""
        self.item2 = ""
        self.item3 = ""
        self.item4 = ""
        self.item5 = ""
        self.item6 = ""

        #these will display below each image...
        self.title = ""
        self.description = ""
        self.project_type = ""

class Data(object):
    def __init__(self):

        #Show All Instance
        show_all = Portfolio()

        #Logos Instance
        logos = Portfolio()

        #Websites Instance
        websites = Portfolio()

        #Print Designs Instance
        print_designs = Portfolio()

        #Pacakage Designs Instance
        package_designs = Portfolio()



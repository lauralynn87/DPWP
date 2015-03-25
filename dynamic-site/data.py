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


class Data(object):
    def __init__(self):

        #Show All Instance
        show_all = Portfolio()
        show_all.item1 = ""
        show_all.item2 = ""
        show_all.item3 = ""
        show_all.item4 = ""
        show_all.item5 = ""
        show_all.item6 = ""

        #Logos Instance
        logos = Portfolio()
        logos.item1 = ""
        logos.item2 = ""
        logos.item3 = ""
        logos.item4 = ""
        logos.item5 = ""
        logos.item6 = ""

        #Websites Instance
        websites = Portfolio()

        #Print Designs Instance
        print_designs = Portfolio()

        #Pacakage Designs Instance
        package_designs = Portfolio()



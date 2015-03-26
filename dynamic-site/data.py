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
        #Portfolio Attributes
        self.item1 = ""
        self.title1 = ""
        self.project1 = ""
        self.desc1 = "" #description

        self.item2 = ""
        self.title2 = ""
        self.project2 = ""
        self.desc2 = "" #description

        self.item3 = ""
        self.title3 = ""
        self.project3 = ""
        self.desc3 = "" #description


class Data(object):
    def __init__(self):

        #Show All Instance
        show_all = Portfolio()
        #Item 1
        show_all.item1 = "images/img-1.jpg"
        show_all.title1 = "Project Title 1"
        show_all.project1 = "Logo Design"
        show_all.desc1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 2
        show_all.item2 = "images/img-2.jpg"
        show_all.title2 = "Project Title 2"
        show_all.project2 = "Website"
        show_all.desc2 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 3
        show_all.item3 = "images/img-3.jpg"
        show_all.title3 = "Project Title 3"
        show_all.project3 = "Print - Business Card"
        show_all.desc3 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."

        #Logos Instance
        logos = Portfolio()
         #Item 1
        logos.item1 = "images/logo-1.jpg"
        logos.title1 = "Project Title"
        logos.project1 = "Identity Design"
        logos.desc1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 2
        logos.item2 = "images/logo-2.jpg"
        logos.title2 = "Project Title"
        logos.project2 = "Logo Design"
        logos.desc2 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 3
        logos.item3 = "images/logo-3.jpg"
        logos.title3 = "Project Title"
        logos.project3 = "Brand Design"
        logos.desc3 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."


        #Websites Instance
        websites = Portfolio()
         #Item 1
        websites.item1 = "images/img-1.jpg"
        websites.title1 = "Project Title"
        websites.project1 = "Responsive Website"
        websites.desc1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 2
        websites.item2 = "images/img-2.jpg"
        websites.title2 = "Project Title"
        websites.project2 = "Wordpress Website"
        websites.desc2 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 3
        websites.item3 = "images/img-3.jpg"
        websites.title3 = "Project Title"
        websites.project3 = "Simple Website"
        websites.desc3 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."

        #Print Designs Instance
        print_designs = Portfolio()
         #Item 1
        print_designs.item1 = "images/img-1.jpg"
        print_designs.title1 = "Project Title"
        print_designs.project1 = "Poster"
        print_designs.desc1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 2
        print_designs.item2 = "images/img-2.jpg"
        print_designs.title2 = "Project Title"
        print_designs.project2 = "Brochure"
        print_designs.desc2 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 3
        print_designs.item3 = "images/img-3.jpg"
        print_designs.title3 = "Project Title"
        print_designs.project3 = "Business Card"
        print_designs.desc3 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."


        #Pacakage Designs Instance
        package_designs = Portfolio()
         #Item 1
        package_designs.item1 = "images/img-1.jpg"
        package_designs.title1 = "Project Title"
        package_designs.project1 = "Package Design"
        package_designs.desc1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 2
        package_designs.item2 = "images/img-2.jpg"
        package_designs.title2 = "Project Title"
        package_designs.project2 = "Package Design"
        package_designs.desc2 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 3
        package_designs.item3 = "images/img-3.jpg"
        package_designs.title3 = "Project Title"
        package_designs.project3 = "Package Design"
        package_designs.desc3 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."


        self.filters = [show_all, logos, websites, print_designs, package_designs]

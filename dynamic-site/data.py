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
        show_all.item1 = "images/print1.jpg"
        show_all.title1 = "Corporate Identity & Business Card "
        show_all.project1 = "Business Card"
        show_all.desc1 = "Business Card for a Cargo Carrier"
        #Item 2
        show_all.item2 = "images/website1.png"
        show_all.title2 = "BuzzFlix Media"
        show_all.project2 = "Website"
        show_all.desc2 = "Wordpress Website with video."
        #Item 3
        show_all.item3 = "images/logo-1.jpg"
        show_all.title3 = "Market Thyme"
        show_all.project3 = "Logo Design"
        show_all.desc3 = "Logo Design for a restaurant"

        #Logos Instance
        logos = Portfolio()
         #Item 1
        logos.item1 = "images/logo-1.jpg"
        logos.title1 = "Market Thyme"
        logos.project1 = "Identity Design"
        logos.desc1 = "Logo Design for a restaurant"
        #Item 2
        logos.item2 = "images/logo-2.jpg"
        logos.title2 = "OrganiCaffe"
        logos.project2 = "Logo Design"
        logos.desc2 = "Logo Design for a coffee beverage"
        #Item 3
        logos.item3 = "images/logo-3.jpg"
        logos.title3 = "Project Title"
        logos.project3 = "Brand Design"
        logos.desc3 = "Logo Design for a Pest Control company in Florida"


        #Websites Instance
        websites = Portfolio()
         #Item 1
        websites.item1 = "images/website1.png"
        websites.title1 = "Buzz Flix Media"
        websites.project1 = "Responsive Website"
        websites.desc1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
        #Item 2
        websites.item2 = "images/website2.png"
        websites.title2 = "Chiroprator Website"
        websites.project2 = "Wordpress Website"
        websites.desc2 = "Medical Website Design"
        #Item 3
        websites.item3 = "images/website3.png"
        websites.title3 = "Capital Concierge"
        websites.project3 = "Wordpress Website"
        websites.desc3 = "Website and Content design for concierge company based in Tampa."

        #Print Designs Instance
        print_designs = Portfolio()
         #Item 1
        print_designs.item1 = "images/print1.jpg"
        print_designs.title1 = "CJI Enterprise"
        print_designs.project1 = "Business Card"
        print_designs.desc1 = "Business Card and Logo for a Frieght/Cargo Company"
        #Item 2
        print_designs.item2 = "images/print2.jpg"
        print_designs.title2 = "Dental Postcard"
        print_designs.project2 = "PostCard"
        print_designs.desc2 = "How Was Your Visit Post Card from Dental Office"
        #Item 3
        print_designs.item3 = "images/print3.jpg"
        print_designs.title3 = "Corporate Brochure"
        print_designs.project3 = "Multi-Page Brochure"
        print_designs.desc3 = "Layout Design for the brochure"


        #Pacakage Designs Instance
        package_designs = Portfolio()
         #Item 1
        package_designs.item1 = "images/package1.jpg"
        package_designs.title1 = "Jai Ho Beer"
        package_designs.project1 = "Package Design"
        package_designs.desc1 = "Logo and Label Design for Beer beverage"
        #Item 2
        package_designs.item2 = "images/package2.jpg"
        package_designs.title2 = "OrganiCaffe"
        package_designs.project2 = "Package Design"
        package_designs.desc2 = "Package Design for Coffee Beverage"
        #Item 3
        package_designs.item3 = "images/package3.jpeg"
        package_designs.title3 = "Project Title"
        package_designs.project3 = "Package Design"
        package_designs.desc3 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."


        self.filters = [show_all, logos, websites, print_designs, package_designs]

'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Reusable Library (Week 3)
Date: 03/18/15
'''
#

import webapp2

#Necessary Imports
from pages import Form, Results
from library import TvSize

class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = Form() #Forms Class in pages.py
        r = Results() #Results Class in pages.py

        #Gets the data the user entered from form
        #Checks to see if the form is filled out first
        if self.request.GET:
            name = self.request.GET['name'] #pulls the name from the form
            resolution = self.request.GET['resolution'] #pulls the resolution selection from the form
            distance = self.request.GET['distance'] #pulls the distance entered from the user from the form.

        #Create Instance to send info to library
            lib = TvSize()
            lib.distance = distance
            lib.resolution = resolution
            new_min_size = lib.min_size() #creating a variable min_size for function library
            new_max_size = lib.max_size() #creating a variable max_size for function library
            resolution_check = lib.reso() #creates a variable for function reso in library

            #Creates variables and send the info back to results class
            r.name = name
            r.distance = distance
            r.resolution = resolution_check
            r.new_min_size = new_min_size
            r.new_max_size = new_max_size

            #Prints page with form data
            self.response.write(r.print_out())

        else: #ELSE - if form isn't filled out this is what is the result:
            #Print the Form Page
            self.response.write(f.print_out())



#do not write below this line
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

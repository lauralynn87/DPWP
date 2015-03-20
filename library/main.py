'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Reusable Library (Week 3)
Date: 03/18/15
'''
#

import webapp2

#Necessary Imports
from pages import Form
from pages import Results
from library import TvSize

class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = Form()
        r = Results
        
        #Gets the data the user entered from form
        if self.request.GET:
            name = self.request.GET['name']
            email = self.request.GET['email']
            resolution = self.request.GET['resolution']
            distance = self.request.GET['distance']
            self.response.write(f.print_out())


        #Create Instance to send info to library
            lib = TvSize()
            lib.distance = distance
            lib.resolution = resolution
            new_min_size = lib.min_size() #creating a variable min_size
            new_max_size = lib.max_size() #creating a variable max_size
        else:
            self.response.write(f.print_out())







#do not write below this line
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

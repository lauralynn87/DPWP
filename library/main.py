'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Reusable Library (Week 3)
Date: 03/18/15
'''
#

import webapp2

from pages import Form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = Form()

        #Gets the data the user entered from form
        if f.request.GET:
            name = self.request.GET['name']
            email = self.request.GET['email']
            resolution = self.request.GET['resolution']
            distance = self.request.GET['distance']

    lib = TvSize()
        lib.distance = distance
        lib.resolution = resolution



#do not write below this line
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

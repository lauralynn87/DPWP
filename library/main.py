'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Reusable Library (Week 3)
Date: 03/18/15
'''
#

import webapp2

class MainHandler(webapp2.RequestHandler):


    """
        if self.request.GET:
            name = self.request.GET['name']
            email = self.request.GET['email']
            resolution = self.request.GET['resolution']
            distance = self.request.GET['distance']
    """



#do not write below this line
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

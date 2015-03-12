'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Simple Form (Week 2)
Date: 03/12/15
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

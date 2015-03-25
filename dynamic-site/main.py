'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Dynamic Website (Week 4)
Date: 03/25/15
'''

#DO NOT TOUCH
import webapp2

#Necessary Imports
from pages import Page, ContentPage
from data import Portfolio

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        c = ContentPage()
        f = Portfolio()

        #















#DO NOT WRITE BELOW THIS LINE - needed for google app engine launcher
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

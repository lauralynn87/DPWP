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
from data import Portfolio, Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        c = ContentPage()
        f = Portfolio()

        #the if/else function telling the browser what to load based on what the user clicks
        if  self.request.GET:
            portolio_filter = Portfolio()
            portolio_filter = self.request.GET['portfolio_filter']

            if portolio_filter == "show_all":
                portolio_filter = show_all

            elif portolio_filter == "logos":
                portolio_filter = logos

            elif portolio_filter == "websites":
                portolio_filter = websites

            elif portolio_filter == "print-designs":
                portolio_filter = print_designs

            elif portolio_filter == "package-designs":
                portolio_filter = package_designs

        else:
            self.response.write(c.print_out())















#DO NOT WRITE BELOW THIS LINE - needed for google app engine launcher
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

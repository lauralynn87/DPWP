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
        if self.request.GET:
            portfolio_filter = Portfolio()
            portfolio_filter = self.request.GET['portfolio-filter']

            if portfolio_filter == "show-all":
                portfolio_filter = show_all

            elif portfolio_filter == "logos":
                portfolio_filter = logos

            elif portfolio_filter == "websites":
                portfolio_filter = websites

            elif portfolio_filter == "print-designs":
                portfolio_filter = print_designs

            elif portfolio_filter == "package-designs":
                portfolio_filter = package_designs

        else:
            self.response.write(c.print_out())















#DO NOT WRITE BELOW THIS LINE - needed for google app engine launcher
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

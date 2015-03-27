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
        d = Data()

        #the if/else function telling the browser what to load based on what the user clicks
        if self.request.GET:
            portfolio_filter = self.request.GET['filters']

            if portfolio_filter == "show-all":
                c.item1 = d.filters[0].item1
                c.item2 = d.filters[0].item2
                c.item3 = d.filters[0].item3
                c.title1 = d.filters[0].title1
                c.title2 = d.filters[0].title2
                c.title3 = d.filters[0].title3
                c.project1 = d.filters[0].project1
                c.project2 = d.filters[0].project2
                c.project3 = d.filters[0].project3
                c.desc1 = d.filters[0].desc1
                c.desc2 = d.filters[0].desc2
                c.desc3 = d.filters[0].desc3

            elif portfolio_filter == "logos":
                c.item1 = d.filters[1].item1
                c.item2 = d.filters[1].item2
                c.item3 = d.filters[1].item3
                c.title1 = d.filters[1].title1
                c.title2 = d.filters[1].title2
                c.title3 = d.filters[1].title3
                c.project1 = d.filters[1].project1
                c.project2 = d.filters[1].project2
                c.project3 = d.filters[1].project3
                c.desc1 = d.filters[1].desc1
                c.desc2 = d.filters[1].desc2
                c.desc3 = d.filters[1].desc3

            elif portfolio_filter == "websites":
                c.item1 = d.filters[2].item1
                c.item2 = d.filters[2].item2
                c.item3 = d.filters[2].item3
                c.title1 = d.filters[2].title1
                c.title2 = d.filters[2].title2
                c.title3 = d.filters[2].title3
                c.project1 = d.filters[2].project1
                c.project2 = d.filters[2].project2
                c.project3 = d.filters[2].project3
                c.desc1 = d.filters[2].desc1
                c.desc2 = d.filters[2].desc2
                c.desc3 = d.filters[2].desc3

            elif portfolio_filter == "print-designs":
                c.item1 = d.filters[3].item1
                c.item2 = d.filters[3].item2
                c.item3 = d.filters[3].item3
                c.title1 = d.filters[3].title1
                c.title2 = d.filters[3].title2
                c.title3 = d.filters[3].title3
                c.project1 = d.filters[3].project1
                c.project2 = d.filters[3].project2
                c.project3 = d.filters[3].project3
                c.desc1 = d.filters[3].desc1
                c.desc2 = d.filters[3].desc2
                c.desc3 = d.filters[3].desc3

            elif portfolio_filter == "package-designs":
                c.item1 = d.filters[4].item1
                c.item2 = d.filters[4].item2
                c.item3 = d.filters[4].item3
                c.title1 = d.filters[4].title1
                c.title2 = d.filters[4].title2
                c.title3 = d.filters[4].title3
                c.project1 = d.filters[4].project1
                c.project2 = d.filters[4].project2
                c.project3 = d.filters[4].project3
                c.desc1 = d.filters[4].desc1
                c.desc2 = d.filters[4].desc2
                c.desc3 = d.filters[4].desc3

            self.response.write(c.print_out())

        else:
            self.response.write(p.print_out())



#DO NOT WRITE BELOW THIS LINE - needed for google app engine launcher
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

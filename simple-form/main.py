'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Simple Form (Week 2)
Date: 03/12/15
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')

        #page_head variable to hold HTML Header Portion
        page_head = '''



        '''
        #Holds HTML FORM
        page_form = '''



        '''

        #Holds HTML Closing Statements
         page_close = '''



        '''




#DO NOT REMOVE - NEEDED FOR GOOGLE APP ENGINE LAUNCHER
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

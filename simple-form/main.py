'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Simple Form (Week 2)
Date: 03/12/15
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #page_head variable to hold HTML Header Portion
        page_head = '''

        '''

        #Holds HTML Form
        page_form = '''
        '''

        #Holds HTML Closing Statements
        page_close = '''

        '''

        #Shows Thank You message upon form submission
        form_thankyou_open = '''
         '''

        # IF form is filled out:
        if self.request.GET:
            #INFO RECEIVED FROM FORM STORES HERE
            first_name = self.request.GET['first_name']
            email = self.request.GET['email']
            subject = self.request.GET['subject']
            project = self.request.GET['project']
            add_ons = self.request.get_all('add_ons')

            form_addons = '''
            '''

            #Loops through checked values
            for i in range(len(add_ons)):
                addon = add_ons[i]
                form_addons += "<li>" + addon + ", " + "</li>"










#DO NOT REMOVE - NEEDED FOR GOOGLE APP ENGINE LAUNCHER
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

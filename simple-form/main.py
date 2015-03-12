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

        #Shows confirmation of information entered
        form_confirm_open = '''
         '''

        #Closing of Confirmation Area
        form_confirm_close = '''
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

            #Formats form variables
            form_confirm_open = form_confirm_open.format(**locals())
            form_confirm_close = form_confirm_close.format(**locals())

            #Holds full form
            form_submitted = form_confirm_open + form_addons + form_confirm_close

            #Prints page with form data
            self.response.write(page_head + form_submitted + page_close)

            #ELSE Print the form
        else:
            self.response.write(page_head + page_form + page_close)


#DO NOT REMOVE - NEEDED FOR GOOGLE APP ENGINE LAUNCHER
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

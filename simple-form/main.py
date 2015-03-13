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

        <!DOCTYPE html>
        <html>
        <head>
	        <link href="css/style.css" rel="stylesheet" type="text/css">
	        <title>Hire Me.</title>
        </head>
        <body>

        '''

        #Holds HTML Form
        page_form = '''

        '''

        #Holds HTML Closing Statements
        page_close = '''
            <footer>
		        <p>&copy;Copyright 2015 - All Rights Reserved.</p>
	        </footer>
        </div> <!-- ENDS FORM CONTAINER -->
        </body>
        </html>
        '''

        #Shows confirmation of information entered
        form_confirm_open = '''
        <h2>Your Request has been submitted!</h2>
           <p>Please review the details you submitted below. If you need to make any changes please simply resubmit a new form by pressing <a href="javascript:history.back()">back</a></p>
           <div id="confirm">
               <ul>
                   <li><strong>Name: </strong>{first_name}</li>
                   <li><strong>Email: </strong>{email}</li>
                   <li><strong>Subject: </strong>{subject}</li>
                   <li><strong>Project Type: </strong>{project}</li>
                   <li><strong>Optional Add-Ons: </strong>
                        <ul>
         '''

        #Closing of Confirmation Area
        form_confirm_close = '''
                        </ul>
                   </li>
                   <li><strong>Project Details:</strong>{details}</li>
               </ul><!-- End main list -->
            </div><!-- End DIV 'confirm' -->
        '''

        # IF form is filled out:
        if self.request.GET:
            #INFO RECEIVED FROM FORM STORES HERE
            first_name = self.request.GET['first_name']
            email = self.request.GET['email']
            subject = self.request.GET['subject']
            project = self.request.GET['project']
            add_ons = self.request.get_all('add_ons')
            details = self.request.GET['details']

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

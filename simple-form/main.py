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
	        <link href="CSS/style.css" rel="stylesheet" type="text/css">
	        <title>Hire Me.</title>
        </head>
        <body>

        '''

        #Holds HTML Form
        page_form = '''
        <div class="container">
  	    <h1>Hire Me</h1>

	    <form method="GET" action="">

	    	<label>Name:</label>
	       	<input class="textfield" type="text" name="first_name" placeholder="Name">
	       	<label>Email:</label>
	       	<input class="textfield" type="email" name="email" input="email" placeholder="Email">
	       	<label>Subject:</label>
	       	<input class="textfield" type="text" name="subject" placeholder="Subject">
	       	<label>Choose Project Type:</label>
	       	<select name="project" id="project">
	            <option value="One Page Website">One Page Website</option>
	            <option value="Multi-Page Website">Multi-Page Website</option>
	            <option value="E-Commerce Website">E-Commerce Website</option>
	       	</select>
	       	<label>Optional Add-Ons:</label>
            <label class="checkbox_label"><input type="checkbox" name="add_ons" value="SEO">SEO</label>
            <label class="checkbox_label"><input type="checkbox" name="add_ons" value="Social Media Setup">Social Media Setup</label>
            <label class="checkbox_label"><input type="checkbox" name="add_ons" value="Logo Design">Logo Design</label>
  			<label class="details">Project Details:</label>
			<textarea class="message-box" name="details" placeholder="Project Details"></textarea>
	       <input type="submit" value="Submit" id="Submit">

    	</form>
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
        <div class="container">
	        <h2>Your Request has been submitted!</h2>
            <p>Please review the details you submitted below. If you need to make any changes please simply resubmit a new form by pressing <a href="javascript:history.back()">back</a></p>
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
                </li>
                   <li><strong>Project Details:</strong>{details}</li> <!-- This is from a 'text area' meaning the message could be a paragraph.-->
               </ul>

            <footer>
                    <p>&copy;Copyright 2015 - All Rights Reserved.</p>
            </footer>
        </div>
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

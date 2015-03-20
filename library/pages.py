'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Reusable Library (Week 3)
Date: 03/18/15
'''

class Form(object):
    def __init__(self):
        self.css = "css/styles.css"
        self.head = """
        <!DOCTYPE HTML>
        <html>
            <head>
                <title></title>
                <link href="{self.css}" rel="stylesheet" type="text/css" />
            </head>
                <body>
                """

        self.body = """

            <h1>Determine My TV Size </h1>
            <h3>Fill out the form below to learn more!</h3>

            <form method="GET" action="">

            <label for="name">Name</label><input type="text" name="name" id="name"/></div>

            <label for="email">Email</label><input type="text" name="email" id="email"/></div>

            <label for="number">viewing distance</label><input type="number" name="distance" id="distance"/></div>

            <label for="Resolution">Resolution</label>
                <select id="resolution" name="resolution">
                 <option value="480p">480p</option>
                 <option value="720p">720p</option>
                 <option value="1080p">1080p</option>
                 <option value="4K Ultra">4K Ultra</option>
             </select>
             <input id="submit" type="submit"/><input type="reset" />
            </form>
        """
        self.close = """
                </body>
            </html>
            """

    #Function to print out the form to the browser
    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

class Results(object):
    def __init__(self):
        self.css = "css/styles.css"
        self.head = """
        <!DOCTYPE HTML>
        <html>
            <head>
                <title></title>
                <link href="{self.css}" rel="stylesheet" type="text/css" />
            </head>
                <body>
                """
        self.body = """
         <h2>Thank you for your submission!</h2>
            <p>Please review your results below:</p>
               <ul>
                 <li><strong>Minimum TV Size:</strong>{new_min_size}</li>
                 <li><strong>Maximum TV Size: </strong>{new_max_size}</li>
                 <li><strong>Resolution Check:</strong>{resolution}</li>
                <ul>
            </br>
            <p>These results were based on your viewing distance of {distance} inches.</p>
            """
        self.close = """
                </body>
            </html>
            """

    #Function to print results in the browser
    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all
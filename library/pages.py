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
         <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
             <title>Determine My TV Size</title>
             <link rel="stylesheet" type="text/css" href="{self.css}" media="screen"/>

        </head>
        <body>
        <div class="container">
                """

        self.body = """

                   <div class="row header">
                <h1>Determine My TV Size </h1>
                 <h3>Fill out the form below to learn more!</h3>
                </div>

            <div class="row body">
            <form class='pure-form pure-form-stacked' id='info' method='POST'>
             <fieldset>
                <div class='input-container'>
                    <label>Name</label>
                    <input id='name' name='name' placeholder='name' type='text'>
                </div>
                <div class='input-container'>
                    <label>Email</label>
                    <input id='email' name='email' placeholder='Email' type='email'>
                </div>
                <div class='input-container'>
                    <label>Distance From your TV(inches)</label>
                    <input id='distance' name='distance' placeholder='distance' type='text'>
                </div>
                <div>
                    <label for="howfound">Preferred Resolution</label>
                        <select id="notrequiredselect" name="resolution" class="select">
                            <option value="480p">480p</option>
                            <option value="720p">720p</option>
                            <option value="720p">1080p</option>
                            <option value="720p">4K Ultra</option>
                        </select>
                </div>

            <button class='pure-button notice' id='submit' type='submit'>Submit</button>
         </fieldset>

            </form></div>

            """
        self.close = """
            </div>
        </body>
        </html>

            """
    #Function to print results in the browser
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
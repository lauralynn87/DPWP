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
            <form class="pure-form pure-form-stacked" id="info" method="GET">
             <fieldset>
                <div class="input-container">
                    <label>Name</label>
                    <input id="name" name="name" placeholder="name" type="text">
                </div>
                <div class="input-container">
                    <label>Email</label>
                    <input id="email" name="email" placeholder="Email" type="email">
                </div>
                <div class="input-container">
                    <label>Distance From your TV(inches)</label>
                    <input id="distance" name="distance" placeholder="distance" type="text">
                </div>
                <div>
                    <label for="howfound">Preferred Resolution</label>
                        <select  name="resolution" class="select">
                            <option value="480p" name="480p">480p</option>
                            <option value="720p" name="720p">720p</option>
                            <option value="1080p" name="1080p">1080p</option>
                            <option value="4K Ultra" name="4K Ultra">4K Ultra</option>
                        </select>
                </div>

            <button class="pure-button notice" id="submit" type="submit">Submit</button>
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
            </div>
            <div class="row body">
            <h3>Thank you {name}! Your Results are below. </h3>

            <p>The Minimum TV size you should have is: <span>result here</span></p>

            <p>The Maximum TV Size you can have is:<span>result here</span></p>

            <p>Resolution Check:<span>{resolution}</span></p>

            <p>This information is based on the viewing distance of <span>{distance}</> inches.</p>

            <p class="happy">Happy Shopping!</p>
            </div>

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
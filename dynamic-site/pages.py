'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Dynamic Website (Week 4)
Date: 03/25/15
'''


class Page(object):
    def __init__(self):
        self.css = "css/styles.css"
        #Meta Tags
        self.head = """

        <!DOCTYPE>
<html>
<head>
	<link href='http://fonts.googleapis.com/css?family=Lato:400,700,300' rel='stylesheet' type='text/css'>
	<link href='http://fonts.googleapis.com/css?family=PT+Sans' rel='stylesheet' type='text/css'>
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<title>LauraLynn Designs</title>
</head>
<body>
                """
        #opening containers go here
        self.body = """
        <section class="hero">
</section>
<!-- end of hero section -->
<div class="quote"><div><p>Just build websites ~ CHRIS COYIER</p>
</div></div>
                """
        #Footer and Closing DIVS
        self.close = """
                """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

#Will Hold
class ContentPage(object):
    def __init__(self):
        super(Page, self)._init_()

        #Welcome Section here
        self.welcome = """
        """

        #About Me Section Here
        self.about_me = """
        """

        #Portfolio Section Here
        self.portfolio = """
        """


    #Polymorphism - method overriding
    def print_out(self):
        all = self.head + self.body + self.welcome + self.about_me + self.portfolio + self.close
        all = all.format(**locals())
        return all
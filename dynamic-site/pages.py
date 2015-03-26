'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Dynamic Website (Week 4)
Date: 03/25/15
'''


class Page(object):
    def __init__(self):
        self.css = "css/styles.css"
        #Opening HTML
        self.head = """

        <!DOCTYPE>
        <html>
        <head>
            <link href='http://fonts.googleapis.com/css?family=Lato:400,700,300' rel='stylesheet' type='text/css'>
            <link href='http://fonts.googleapis.com/css?family=PT+Sans' rel='stylesheet' type='text/css'>
            <link rel="stylesheet" type="text/css" href="{self.css}">
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

        <section class="welcome">
        <div class="container">
            <div class="cl-4"><img src="images/1.png" alt=""></div>
            <div class="cl-8">
                <h3>I'm Laura - A UI / UX Designer</h3>
                <h4>With every line of code and pixel, I strive to make the web a beautiful place</h4>
                <p>I have created different awesome print and web designs. I have designed for a number of different clients with all kinds of projects. And I will continue to do so because designing is my passion. I breathe, eat, and live design. The experiences I had with those projects have only fueled my desire for designing, which is why I am currently majoring in Web Design & Development at Full Sail University Online. I plan to graduate with a Bachelor's degree (graduated Associate's degree in Graphic Design last 2008) in 2015. I believe that designing is beautifully intricate and I want to keep on enhancing my skills. Designing is a lifetime of learning, together with my clients.</p>
        </div>
        </section> <!-- end of welcome section -->

        <section class="about">
        <div class="container">
            <div class="cl-8"><img src="images/code.png" alt=""></div>
            <div class="cl-4"><img src="images/2.png" alt=""></div>
        </div>
        </section> <!-- end of about section -->

                 <section class="portfolio">
        <div class="container">
        <div class="cl-4"><img src="images/3.png" alt=""></div>
        <div class="cl-8">
            <ul class="filters">
                <li class="active"><a href="?filters=show-all" title="" name="show-all">SHOW ALL</a></li>
                <li><a href="?filters=logos" title="" name="logos">LOGOS</a></li>
                <li><a href="?filters=websites" title="" name="websites">WEBSITES</a></li>
                <li><a href="?filters=print-designs" title="" name="print-designs">PRINT DESIGNS</a></li>
                <li><a href="?filters=package-designs" title="" name="package-designs">PACKAGE DESIGNS</a></li>
            </ul>
        </div>
        </div>

        <div class="container">
            <div class="rw">
                <div class="cl-3">
                    <img src="images/img-4.jpg" alt="">
                    <h3>Title 1</h3>
                    <p>Illustration</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
                </div>
                <div class="cl-3">
                    <img src="images/img-5.jpg" alt="">
                    <h3>Title 2</h3>
                    <p>Design</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
                </div>
                <div class="cl-3">
                    <img src="images/img-6.jpg" alt="">
                    <h3>Title 3</h3>
                    <p>Art</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
                </div>
            </div>
        </div>


                """
        #Footer and Closing DIVS
        self.close = """
        <section class="contact"><div class="container">
        <div class="copyright cl-8"><p>The entirety of the site is protected by the copyright 2015 - LauraLynn Design</p> </div>
        <div class="social cl-4">

        <a class="twitter" href="#" title=""></a>
        <a class="linkedin" href="#" title=""></a>
        <a class="dribbble" href="#" title=""></a>
        <a class="behance" href="#" title=""></a>
        <a class="pinterest" href="#" title=""></a>

         </div>
        </div></section><!-- end of contact section -->
        </body>
        </html>

                """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

#Will Hold Content for this page
class ContentPage(Page):
    def __init__(self):
        Page.__init__(self)

       #Portfolio Attributes
        self.item1 = ""
        self.title1 = ""
        self.project1 = ""
        self.desc1 = "" #description

        self.item2 = ""
        self.title2 = ""
        self.project2 = ""
        self.desc2 = "" #description

        self.item3 = ""
        self.title3 = ""
        self.project3 = ""
        self.desc3 = "" #description

        #Portfolio Navigation Section Here
        self.filter = """
         <section class="portfolio">
        <div class="container">
        <div class="cl-4"><img src="images/3.png" alt=""></div>
        <div class="cl-8">
            <ul class="filters">
                <li class="active"><a href="?filters=show-all" title="" name="show-all">SHOW ALL</a></li>
                <li><a href="?filters=logos" title="" name="logos">LOGOS</a></li>
                <li><a href="?filters=websites" title="" name="websites">WEBSITES</a></li>
                <li><a href="?filters=print-designs" title="" name="print-designs">PRINT DESIGNS</a></li>
                <li><a href="?filters=package-designs" title="" name="package-designs">PACKAGE DESIGNS</a></li>
            </ul>
        </div>
        </div>

        <div class="container">
            <div class="rw">
                <div class="cl-3">
                    <img src="{self.item1}" alt="">
                    <h3>{self.title1}</h3>
                    <p>{self.project1}</p>
                    <p>{self.desc1}</p>
                </div>
                <div class="cl-3">
                    <img src="{self.item2}" alt="">
                    <h3>{self.title2}</h3>
                    <p>{self.project2}</p>
                    <p>{self.desc2}</p>
                </div>
                <div class="cl-3">
                    <img src="{self.item3}" alt="">
                    <h3>{self.title3}</h3>
                    <p>{self.project3}</p>
                    <p>{self.desc3}</p>
                </div>
            </div>
        </div>

        """

    #Polymorphism - method overriding
    def print_out(self):
        all = self.head + self.body + self.filter + self.close
        all = all.format(**locals())
        return all


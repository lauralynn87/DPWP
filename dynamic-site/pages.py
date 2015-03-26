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

#Will Hold
class ContentPage(object):
    def __init__(self):
        super(Page, self)._init_()

        #Welcome Section here
        self.welcome = """
        <section class="welcome">
<div class="container">
	<div class="cl-4"><img src="images/1.png" alt=""></div>
	<div class="cl-8">
		<h3>I'm Laura - A UI / UX Designer</h3>
		<h4>With every line of code and pixel, I strive to make the web a beautiful place</h4>
		<p>I have created different awesome print and web designs. I have designed for a number of different clients with all kinds of projects. And I will continue to do so because designing is my passion. I breathe, eat, and live design. The experiences I had with those projects have only fueled my desire for designing, which is why I am currently majoring in Web Design & Development at Full Sail University Online. I plan to graduate with a Bachelor’s degree (graduated Associate’s degree in Graphic Design last 2008) in 2015. I believe that designing is beautifully intricate and I want to keep on enhancing my skills. Designing is a lifetime of learning, together with my clients.</p>
</div>
</section> <!-- end of welcome section -->
        """

        #About Me Section Here
        self.about = """
        <section class="about">
<div class="container">
	<div class="cl-8"><img src="images/code.png" alt=""></div>
	<div class="cl-4"><img src="images/2.png" alt=""></div>
</div>
</section> <!-- end of about section -->
        """

        #Portfolio Navigation Section Here
        self.portfolio = """
        <section class="portfolio">
<div class="container">
	<div class="cl-4"><img src="images/3.png" alt=""></div>
	<div class="cl-8">
		<ul class="filters">
			<li id="show-all" class="active"><a href="#" title="" name="show-all">SHOW ALL</a></li>
			<li id="logos"><a href="#" title="" name="logos">LOGOS</a></li>
			<li id="websites"><a href="#" title="" name="websites">WEBSITES</a></li>
			<li id="print-designs"><a href="#" title="" name="print">PRINT DESIGNS</a></li>
			<li id="package-designs"><a href="#" title="" name="page-design">PACKAGE DESIGNS</a></li>
		</ul>
	</div>
</div>
        """


    #Polymorphism - method overriding
    def print_out(self):
        all = self.head + self.body + self.welcome + self.about + self.portfolio + self.close
        all = all.format(**locals())
        return all
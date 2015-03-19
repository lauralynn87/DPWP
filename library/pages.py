'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Reusable Library (Week 3)
Date: 03/18/15
'''

class Form():
    def __init__(self):
        self.css = "css/styles.css"
        self.__head = '''

        <!DOCTYPE HTML>
        <html>
            <head>
                <title></title>
                <link href="{self.css}" rel="stylesheet" type="text/css" />
            </head>
                <body>
                '''

        self.body = '''

            <h1>Determine My TV Size </h1>
            <h3>Fill out the form below to learn more!</h3>

            <form method="GET" action="">

            <label for="name">Name</label><input type="text" name="name" id="firstname"/></div>

   <label for="email">Email</label><input type="text" name="email" id="email"/></div>

    <label for="number">viewing distance</label><input type="number" name="distance" id="distance"/></div>

      <label for="Resolution">Resolution</label>
      <select id="resolution" name="resolution">
        <option value="">[select an option]</option>
        <option value="480p">480p</option>
        <option value="720p">720p</option>
        <option value="1080p">1080p</option>
        <option value="4K Ultra">4K Ultra</option>
      </select>


    <input id="submit" type="submit"/><input type="reset" />
  </form>



        '''
        self.__close = '''

                </body>
            </html>
            '''


class Results():
    def __init__(self):
        self.body = """



        """



    def print_out(self):
        all = self.__head + self.body + self.__close
        return all
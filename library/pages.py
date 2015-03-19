'''
Name: Laura Moser
Class: Design Patterns for Web Programming
Assignment: Reusable Library (Week 3)
Date: 03/18/15
'''

class Form():
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/styles.css"
        self.__head = '''

        <!DOCTYPE HTML>
        <html>
            <head>
                <title>Find your TV Size</title>
                <link href="css/styles.css" rel="stylesheet" type="text/css" />
            </head>
                <body>
                '''

        self.body = ''' '''
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
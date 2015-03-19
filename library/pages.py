class Page():
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

            self.body = """ """
            self.__close = '''
                </body>
            </html>
            '''

    def print_out(self):
        all = self.__head + self.body + self.__close
        return all
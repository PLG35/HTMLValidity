# -*-coding:Latin-1 -*

# Imports
import urllib.request
import html.parser

# Class parsing the feedback of the web tool validating the syntax
class FindErrors(html.parser.HTMLParser):
    def __init__(self, *args, **kwargs):
        super(FindErrors, self).__init__(*args, **kwargs)
        self.errors = []
        self.test = False
        self.description = ""
        self.location = ""
        self.extract = ""
        self.type = ""

    def handle_starttag(self, tag, attrs):
        if(tag == "li"):
            self.test = True
        if(tag == "p" and self.test):
            if len(attrs) > 0:
                if attrs[0][1] == "location":
                    self.type = "location"
                elif attrs[0][1] == "extract":
                    self.type = "extract"
            else:
                self.type = "description"

    def handle_endtag(self, tag):
        if(tag == "li"):
            self.errors.append([self.description, self.location, self.extract])
            self.test = False
            self.description = ""
            self.location = ""
            self.extract = ""
            self.type = ""

    def handle_data(self, data):
        if self.test and self.type != "":
            if self.type == "location":
                self.location = self.location + data
            if self.type == "extract":
                self.extract = self.extract + data
            if self.type == "description":
                self.description = self.description + data

# Main class of the library
class Validator:

    def __init__(self):
        # Path of the web tool validating HTML syntax
        self.basisURL = "https://validator.w3.org/nu/?doc="

    def testURL(self, url):
        # Define the URL to test
        testURL = self.basisURL + url

        # Get the html of the webpage
        urlOpened = urllib.request.urlopen(testURL) # In python 2.7, urllib.request should be replaced by urllib
        htmlContent = urlOpened.read()
        self.strHtml = str(htmlContent)

        # Parse HTML content
        self.myParser = FindErrors()
        self.myParser.feed(self.strHtml)

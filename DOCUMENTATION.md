# TestHTMLValidity
Tool lauching a validation of the HTML code of a webpage by the page https://validator.w3.org/nu/.

## Dependencies
The code is made to run on Python 3. In python 2.7, urllib.request should be replaced by urllib.

The library libCartography.py has the following dependencies :
- urllib.request
- html.parser

## Input
The only input is the URL of the web page to test.

## Output
The object Validator contains an implementation MyParser of the object FindErrors, which contains a list of syntax errors in the HTML code.

These errors are lists of three data :
1. The description of the error,
2. The location of the error in the HTML code,
3. An extract of the HTML code around the error itself.
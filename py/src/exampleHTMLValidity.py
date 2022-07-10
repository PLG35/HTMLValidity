# -*-coding:Latin-1 -*

# Imports
import libHTMLValidity

# Initialisation
urls = ["http://plgdev.fr:1234/index"]
myValidator = libHTMLValidity.Validator()

# Loop on the urls
for url in urls:
    print("URL : " + url)
    print("")
    myValidator.testURL(url)

    # Loop on the errors found
    for error in myValidator.myParser.errors:
        print("Error : " + error[0])
        print("Location : " + error[1])
        print("Extract : " + error[2])
        print("")

    print("")

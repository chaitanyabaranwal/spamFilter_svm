from bs4 import BeautifulSoup
import re

def cleanString(myString):

    myString = re.sub(r'<(a href).*?</a>', r' httpaddr', myString).lower()
    myString = re.sub(r'http://\S+', r'httpaddr', myString)
    myString = re.sub(r'/(.){1}', r'', myString)
    myString = BeautifulSoup(myString, "lxml").get_text()
    myString = re.sub(r'[0-9]+', r' number', myString)
    myString = re.sub(r'[^A-Za-z]+', r' ', myString)
    return myString
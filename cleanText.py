from bs4 import BeautifulSoup
import re
import nltk

def cleanString(myString):

    # convert text to lowercase
    myString = myString.lower()

    # convert URLs to 'httpaddr'
    myString = re.sub(r'(http|https)://[^\s]*', r' httpaddr ', myString)

    # convert email addresses to 'emailaddr'
    myString = re.sub(r'[^\s]+@[^\s]+[.][^\s]+', r' emailaddr ', myString)
    
    # convert all hyperlinks to 'linktag'
    soup = BeautifulSoup(myString, 'html.parser')
    myString = soup.get_text()
    numberLink = len(soup.find_all('a'))
    numberImg = len(soup.find_all('img'))
    myString = myString + numberLink * " linktag " + numberImg * " imgtag "

    # convert numbers to 'number'
    myString = re.sub(r'[0-9]+', r' number ', myString)

    # convert $, ! and ? to proper words
    myString = re.sub(r'[$]', r' dollar ', myString)
    myString = re.sub(r'[!]', r' exclammark ', myString)
    myString = re.sub(r'[?]', r' questmark ', myString)

    # convert other punctuation to whitespace
    myString = re.sub(r'([^\w\s]+)|([_-]+)', r' ', myString)

    # convert newlines and blanklines to special strings and extra whitespace to single
    myString = re.sub(r'\n', r' newline ', myString)
    myString = re.sub(r'\n\n', r' blankline ', myString)
    myString = re.sub(r'\s+', r' ', myString)
    myString = myString.strip(' ')

    # perform word stemming
    myStringWords = myString.split(' ')
    stemmer = nltk.stem.snowball.SnowballStemmer('english')
    stemWords = [stemmer.stem(word) for word in myStringWords]
    myString = ' '.join(stemWords)

    return myString

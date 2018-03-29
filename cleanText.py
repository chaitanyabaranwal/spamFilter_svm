from bs4 import BeautifulSoup
import re
import nltk

string = """<div class="post-text" itemprop="text">\r\n<p>You can use:<br></p><p>import os.path</p><p>os.path.isfile(fname)<br></p>\r\n\r\n\r\n\r\n<p>if you need to be sure it's a file.</p>\r\n    </div>"""

def cleanString(myString):

    # convert all html tags to 'htmltag' and all hyperlinks to 'linktag'
    soup = BeautifulSoup(myString, 'html.parser')
    myString = soup.get_text()
    numberHtml = len(soup.find_all())
    numberLink = len(soup.find_all('a'))
    myString = myString + numberLink * " linktag "

    # convert text to lowercase
    myString = myString.lower()

    # convert URLs to 'httpaddr'
    myString = re.sub(r'(http|https)://[^\s]*', r' httpaddr ', myString)

    # convert email addresses to 'emailaddr'
    myString = re.sub(r'\b[^\s]+@[^\s]+[.][^\s]+\b', r' emailaddr ', myString)

    # convert numbers to 'number'
    myString = re.sub(r'\b[\d]+\b', r' number ', myString)

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

    # remove all useless stopwords
    myStringWords = myString.split(' ')
    keepWords = [word for word in myStringWords if word not in nltk.corpus.stopwords.words('english')]

    # perform word stemming
    stemmer = nltk.stem.snowball.SnowballStemmer('english')
    stemWords = [stemmer.stem(word) for word in keepWords]
    myString = ' '.join(stemWords)

    return myString

print(cleanString(string))
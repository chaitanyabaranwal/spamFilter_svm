import openpyxl
import numpy as np
from cleanText import cleanString
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix

# Get the original dataset
def store():

    workBookOld = openpyxl.load_workbook('DataSet.xlsx')
    dataSheetOld = workBookOld.get_sheet_by_name('Data set')

    xData = []
    yData = []

    rows = dataSheetOld.max_row

    for i in range(2, rows+1):

        xData.append(cleanString(str(dataSheetOld.cell(row = i+2, column = 1).value)))
        yData.append(str(dataSheetOld.cell(row = i+2, column = 2).value))

    return xData, yData

# make a dictionary of the 3000 most common words
def makeDictionary(xData):

    emails = [mail for mail in xData]
    all_words = []
    
    for mail in emails:

        words = mail.split()
        all_words += words
    
    dictionary = Counter(all_words)
    dictionary = dictionary.most_common(100)
    return dictionary

# construct a 3000-column feature vector for each mail
def extractFeatures(xData, dictionary):
    
    featureMatrix = np.zeros((len(xData), 100))
    emailId = 0

    for mail in xData:
        for word in mail:
            wordId = 0
            for i,d in enumerate(dictionary):
                if (d[0] == word):
                    wordId = i
                    featureMatrix[emailId, wordId] = mail.count(word)
        emailId += 1

    return featureMatrix

# Create training data
xData, yData = store()
dictionary = makeDictionary(xData)

# Create feature vector and matrix for yData and xData

yTrainMatrix = np.zeros(len(yData))
for i in range(len(yData)):
    if (yData[i] == "Spam"):
        yTrainMatrix[i] = 1

xTrainMatrix = extractFeatures(xData, makeDictionary(xData))

# Training SVM and NB classifier
model1 = MultinomialNB()
model2 = LinearSVC()
model1.fit(xTrainMatrix, yTrainMatrix)
model2.fit(xTrainMatrix, yTrainMatrix)

# Test new data for Spam
result1 = model1.predict(xTrainMatrix)
result2 = model2.predict(xTrainMatrix)
print(confusion_matrix(result1, yTrainMatrix))
print(confusion_matrix(result2, yTrainMatrix))
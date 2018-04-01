import openpyxl
import numpy as np
from cleanText import cleanString
from collections import Counter
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split

# Get the original dataset
def store():

    workBookOld = openpyxl.load_workbook('DataSet.xlsx')
    dataSheetOld = workBookOld.get_sheet_by_name('Data set')

    xData = []
    yData = []

    rows = dataSheetOld.max_row

    for i in range(2, rows+1):

        if (str(dataSheetOld.cell(row = i+2, column = 2).value) != 'None'):
            xData.append(cleanString(str(dataSheetOld.cell(row = i+2, column = 1).value)))
            yData.append(str(dataSheetOld.cell(row = i+2, column = 2).value))

    xTrain, xTest, yTrain, yTest = train_test_split(xData, yData, test_size = 0.2)

    return xTrain, xTest, yTrain, yTest

# make a dictionary of the most common words
def makeDictionary(xData):

    all_words = []
    
    for mail in xData:

        words = mail.split()
        all_words.extend(words)
    
    dictionary = Counter(all_words)
    dictionary = dictionary.most_common(10000)
    return dictionary

# construct a feature vector for each mail
def extractFeatures(xData, dictionary):
    
    featureMatrix = np.zeros((len(xData), 10000))
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
xTrain, xTest, yTrain, yTest = store()
trainDictionary = makeDictionary(xTrain)
testDictionary = makeDictionary(xTest)

# Create feature vector and matrix for yData and xData

yTrainMatrix = np.zeros(len(yTrain))
for i in range(len(yTrain)):
    if (yTrain[i] == "Spam"):
        yTrainMatrix[i] = 1

yTestMatrix = np.zeros(len(yTest))

total = 0 # to check the number of spam with predicted
for i in range(len(yTest)):
    if (yTest[i] == "Spam"):
        yTestMatrix[i] = 1
        total += 1

xTrainMatrix = extractFeatures(xTrain, trainDictionary)
xTestMatrix = extractFeatures(xTest, testDictionary)

# Training SVM classifier
model = LinearSVC(C = 0.5, random_state = 200, class_weight = 'balanced')
model.fit(xTrainMatrix, yTrainMatrix)

# Test new data for Spam
result = model.predict(xTestMatrix)
print(confusion_matrix(result, yTestMatrix))
print(total)
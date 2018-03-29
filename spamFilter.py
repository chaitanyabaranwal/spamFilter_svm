import openpyxl
from cleanText import cleanString

# Get the original dataset
workBookOld = openpyxl.load_workbook('DataSet.xlsx')
dataSheetOld = workBookOld.get_sheet_by_name('Data set')

# initializing the required variables
trainPositive = {}
trainNegative = {}
totalPositive = 0.0
totalNegative = 0.0
probSpam = 0.0
probNotSpam = 0.0

# Function to store data
def store():

    xData = []
    yData = []

    rows = dataSheetOld.max_row

    for i in range(2, rows+1):

        xData.append(cleanString(str(dataSheetOld.cell(row = i+2, column = 1).value)))
        yData.append(str(dataSheetOld.cell(row = i+2, column = 2).value))

    return xData, yData


# Function to train from the dataset
def train(xData, yData):

    numSpam = 0.0

    for i in range(len(xData)):

        if (yData[i] == "Spam"):
            numSpam += 1

        processEmail(xData[i], yData[i])

    global probSpam
    probSpam = (float)(numSpam/len(xData))

    global probNotSpam
    probNotSpam = 1 - probSpam
    

# Function to set conditional probability parameters
def processEmail(body, label):

    for word in body:

        if (label == "Spam"):

            global trainPositive
            trainPositive[word] = trainPositive.get(word, 0) + 1

            global totalPositive
            totalPositive += 1

        else:
            global trainNegative
            trainNegative[word] = trainNegative.get(word, 0) + 1

            global totalNegative
            totalNegative += 1

#Function to get conditional probability of a word
def conditionalWord(word, label):

    if (label == "Spam"):
        if (word in trainPositive.keys()):
            return trainPositive[word]/totalPositive
        else:
            return 1.0

    if (label == "Not Spam"):
        if (word in trainNegative.keys()):
            return trainNegative[word]/totalNegative
        else:
            return 1.0

#Function to get conditional probability of an email
def conditionalEmail(body, label):

    result = 1.0
    for word in body:
        result *= conditionalWord(word, label)
    return result

#Function to finally classify email
def classifyEmail(body):

    isSpam = probSpam * conditionalEmail(body, "Spam")
    isNotSpam = probNotSpam * conditionalEmail(body, "Not Spam")

    if (isSpam > isNotSpam):
        return "Spam"
    else:
        return "Not Spam"

# train from the data set
xData, yData = store()
train(xData, yData)

# main function
def main():
    emailBody = str(input("Enter the email body: "))
    emailBody = cleanString(emailBody)
    answer_label = classifyEmail(emailBody)

def calculateAccuracy():

    total = 0
    
    for i in range(2, 926):

        emailBody = cleanString(str(dataSheetOld.cell(row = i, column = 1).value))
        answer_label = classifyEmail(emailBody)

        if (answer_label == str(dataSheetOld.cell(row = i, column = 2).value)):
            total += 1

    print("Accuracy is: " + str(total/9.24))

calculateAccuracy()

import openpyxl
from cleanText import cleanString

# Get the original dataset
workBookOld = openpyxl.load_workbook('DataSet.xlsx')
dataSheetOld = workBookOld.get_sheet_by_name('Data set')

#initializing the required variables
trainPositive = {}
trainNegative = {}
totalPositive = 0.0
totalNegative = 0.0
probSpam = 0.0
probNotSpam = 0.0

# Function to train from the dataset
def train():

    rows = dataSheetOld.max_row
    total = 0.0
    numSpam = 0.0

    for i in range(2, rows+1):

        label = str(dataSheetOld.cell(row = i, column = 2).value)
        body = cleanString(str(dataSheetOld.cell(row = i, column = 1).value))

        if (label == "Spam"):
            numSpam += 1

        processEmail(body, label)
        total += 1

    global probSpam
    probSpam = numSpam/total

    global probNotSpam
    probNotSpam = 1 - probSpam
    

# Function to set conditional probability parameters
def processEmail(body, label):

    for word in body.split(" "):

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
        try:
            return trainPositive[word]/totalPositive
        except KeyError:
            return 1.0

    try:
        return trainNegative[word]/totalNegative
    except KeyError:
        return 1.0


#Function to get conditional probability of an email
def conditionalEmail(body, label):

    result = 1.0
    for word in body.split(" "):
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
train()

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
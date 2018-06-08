# SVM Spam Filter

A Python SVM-based Spam Filter which trains on a dataset using the `LinearSVC` model and `TfidfVectorizer` to predict whether future emails are spam or non-spam. A `TfidfVectorizer` makes handling of imbalanced data more efficient by removing common words and giving more weight to words being used in spam-emails.

## Getting started

Clone to repository to your computer, navigate to the cloned repo and run the program using `python3 spamFilter.py` command. The dataset on which the algorithm trains itself has been provided as an excel file in the repo itself.

### Prerequisites

* **Make sure that Python 3 has been installed on your system**
  * Windows users: Go to https://www.python.org/downloads/ and download the latest source release
  * Linus users: Python usually comes installed in Linux. To check your version of Python 3, type `python3 -V` on the terminal. If Python 3 is not present, use `sudo apt-get update` and then `sudo apt-get install python3` to get it on Linux.
  
* **Libraries required to be installed to run the code**
  * cleanText.py : `BeautifulSoup`, `re` and `nltk`
  * spamFilter.py : `openpyxl`, `numpy`, `scipy`, and `sklearn`
  * `openpyxl` is required to read the `.xlsx` dataset file. If you have data stored in another format/file, make sure you have the necessary library installed, and modify the code in `store()` to store the training data in `xData` and `yData`.
  
  
To install any library on your system, you can use the `pip` or `pip3` command
```
pip3 install sklearn
pip3 install BeautifulSoup
```
Linux users may have to use `sudo` command with `pip` if libraries are being installed directly in the system.

### Test cases used

The code by itself randomly splits the given dataset into an 80-20 ratio for training and testing respectively. 
If one wants to test the learning algorithm, simply add the following lines to the end of the code:
```
fScore, matrix = calcFScore(xTest, yTest, model, vectorizer)
print("F-score is: %s" % fScore)
```
As you'll see, **the learning algorithm gives an F-score, precision and recall of ~0.97**. The F-score is calculated taking non-spam labels (0) as positive and spam labels (1) as negative.


### Applying the algorithm to predict future emails

Since it's better to train on the entire dataset for classifying future emails, the following modifications to the code will ensure that the entire dataset is trained upon and future e-mails can be classified based on their body content:

* Modify `store()` to return the entire dataset
```
def store():
...
# NOTE: ...
return xData, yData
```

* Replace line 67 to `xTrain, yTrain = store()`
* To classify an email, store email content in `emailBody`, and add the following lines to the end of the code:
```
label = predict(emailBody, model, vectorizer)
print("Email is: %s" % label)
```

## Additional Notes

* For more information about the LinearSVC model, its parameters and other SVM models:      
  * http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
  * http://scikit-learn.org/stable/modules/svm.html

* For more information on TF-IDF vectorizer, its working and other feature extractors:
  * http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
  * http://scikit-learn.org/stable/modules/feature_extraction.html
  * https://en.wikipedia.org/wiki/Tf%E2%80%93idf

## Authors

* **Chaitanya Baranwal** (https://github.com/chaitanyabaranwal/)

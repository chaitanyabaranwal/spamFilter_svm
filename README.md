# SVM Spam Filter

A Python SVM-based Spam Filter which trains on a dataset using the `NuSVM` model and uses the model to predict whether future emails are spam or non-spam.

## Getting started

Clone to repository to your computer, navigate to the cloned repo and run the program using `python3 spamFilter.py` command. The dataset on which the algorithm trains itself has been provided as an excel file in the repo itself.

### Prerequisites

* **Make sure that Python 3 has been installed on your system**
  * Windows users: Go to https://www.python.org/downloads/ and download the latest source release
  * Linus users: Python usually comes installed in Linux. To check your version of Python 3, type `python3 -V` on the terminal. If Python 3 is not present, use `sudo apt-get update` and then `sudo apt-get install python3` to get it on Linux.
  
* **Libraries required to be installed to run the code**
  * cleanText.py : `BeautifulSoup`, `re` and `nltk`
  * spamFilter.py : `openpyxl`, `numpy`, `scipy`, `sklearn` and `collections`
  
To install any library on your system, you can use the `pip` or `pip3` command
```
pip3 install sklearn
pip3 install BeautifulSoup
```
Linux users may have to use `sudo` command with `pip` if libraries are being installed directly in the system.

import re

def search_file(file, pattern):
    content = open(file).read()
    if re.search(pattern, content, re.MULTILINE):
        return True
    return False

target = 'student_loans_with_deep_learning.ipynb'

### Prepare the Data for Use on a Neural Network Model (15 points)
def test_clean():
    assert search_file(target, rf"this should fail") == True, "Two datasets were created: a target (y) dataset, which includes the 'credit_ranking' column, and a features (X) dataset, which includes the other columns. (5 points)"

    assert search_file(target, rf"this should fail") == True, "The features and target sets have been split into training and testing datasets. (5 points)"

    assert search_file(target, rf"this should fail") == True, "Scikit-learn's StandardScaler was used to scale the features data. (5 points)"

### Compile and Evaluate a Model Using a Neural Network (30 points)
def test_clean():
    assert search_file(target, rf"this should fail") == True, "A deep neural network was created with appropriate parameters. (10 points)"

    assert search_file(target, rf"this should fail") == True, "The model was compiled and fit using the accuracy loss function, the adam optimizer, the accuracy evaluation metric, and a small number of epochs, such as 50 or 100. (10 points)"

    assert search_file(target, rf"this should fail") == True, "The model was evaluated using the test data to determine its loss and accuracy. (5 points)"
    
    assert search_file(target, rf"this should fail") == True, "The model was saved and exported to a keras file named student_loans.keras. (5 points)"

### Predict Loan Repayment Success by Using your Neural Network Model (25 points)
def test_clean():
    assert search_file(target, rf"this should fail") == True, "The saved model was reloaded. (5 points)"

    assert search_file(target, rf"this should fail") == True, "The reloaded model was used to make binary predictions on the testing data. (10 points)"
    
    assert search_file(target, rf"this should fail") == True, "A classification report is generated for the predictions and the testing data. (10 points)"

### Discuss creating a recommendation system for student loans (30 points)
def test_clean():
    assert search_file(target, rf"this should fail") == True, "Question 1: The response describes the data that should be collected to build a recommendation system for student loan options. (4 points)"

    assert search_file(target, rf"this should fail") == True, "Question 1: The response explains why they think that data should be collected. (4 points)"
    
    assert search_file(target, rf"this should fail") == True, "Question 1: The type of data described is appropriate for a recommendation system for student loan options. (2 points)"

    assert search_file(target, rf"this should fail") == True, "Question 2: The response chose a filtering method. (4 points)"
    
    assert search_file(target, rf"this should fail") == True, "Question 2: The student justified the choice of their filtering method. (4 points)"
    
    assert search_file(target, rf"this should fail") == True, "Question 2: The choice of filtering method was appropriate for the data selected in the previous question. (2 points)"

    assert search_file(target, rf"this should fail") == True, "Question 3: The response lists two real-world challenges with building a recommendation system for student loans. (4 points)"
    
    assert search_file(target, rf"this should fail") == True, "Question 3: The response explains why these challenges would be of concern for a student loan recommendation system. (6 points)"
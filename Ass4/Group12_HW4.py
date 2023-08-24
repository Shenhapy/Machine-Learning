# -*- coding: utf-8 -*-
"""Group12_HW4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LQireG8herqFjH7XFnL_ef7jjN8hhvzi

#Part 2

##In this part, use KDD Cup 1999 dataset

Import the required libraries:
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
import seaborn as sns

"""###a)

Load the dataset:

Which shows 39 columns and 494021 rows.
"""

df = pd.read_csv('KDD.csv')

"""View the dataset:

View the dataset which must show 38 input feature variables and 1 target (marked as target on .csv file provided) variable Obtain input feature variables as X and target variable as Y.
"""

df.info()

df.head()

"""Extract input feature variables (X) and target variable (Y):"""

X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

"""Normalize X using MinMaxScaler:
Normalize X using MinMaxScaler from sklearn library.
"""

scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

X_normalized

"""Compute filter-based feature selection algorithm to reduce the number of feature variables to 10:

Compute filter-based feature selection algorithm on dataset by reducing the
number of feature variables to 10 (i.e. 9 input feature variables + 1 target
variable) from 39 columns and show the first five rows again and name this
dataset as my data comprising 10 feature variables.
"""

selector = SelectKBest(score_func=f_classif, k=9)
X_selected = selector.fit_transform(X_normalized, Y)

"""Create a new DataFrame with the selected features:"""

# Select 10 feature variables (9 input features + 1 target variable)
selector = SelectKBest(score_func=f_classif, k=9)
X_selected = selector.fit_transform(X_normalized, Y)
selected_feature_names = X.columns[selector.get_support()].tolist()
selected_feature_names.append('target')

# Concatenate the target variable with the selected features
target_column = Y.to_frame(name='target')
my_data = pd.DataFrame(np.concatenate([X_selected, target_column], axis=1), columns=selected_feature_names)

"""Show the first five rows of the new dataset (my data):"""

my_data.head()

"""### b)

Split the data into three subsets with different train-test ratios:

Use sklearn to split my data using train test split into three subsets,
for instance, my data 1 with 70% train & 30% test data, my data 2
with 60%train & 40% test data, my data 3 with 50%train & 50%
test data
"""

# my data 1: 70% train & 30% test
X_train1, X_test1, y_train1, y_test1 = train_test_split(my_data.iloc[:, :-1], my_data.iloc[:, -1], test_size=0.3, random_state=42)

# my data 2: 60% train & 40% test
X_train2, X_test2, y_train2, y_test2 = train_test_split(my_data.iloc[:, :-1], my_data.iloc[:, -1], test_size=0.4, random_state=42)

# my data 3: 50% train & 50% test
X_train3, X_test3, y_train3, y_test3 = train_test_split(my_data.iloc[:, :-1], my_data.iloc[:, -1], test_size=0.5, random_state=42)

"""Create and fit a Decision Tree classifier on each subset:

Compute the performance of Decision tree in terms of classification report for each subsets.
"""

# Decision Tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier on my data 1
clf.fit(X_train1, y_train1)

# Make predictions and evaluate performance for my data 1
y_pred1 = clf.predict(X_test1)
report1 = classification_report(y_test1, y_pred1)

# Fit the classifier on my data 2
clf.fit(X_train2, y_train2)

# Make predictions and evaluate performance for my data 2
y_pred2 = clf.predict(X_test2)
report2 = classification_report(y_test2, y_pred2)

# Fit the classifier on my data 3
clf.fit(X_train3, y_train3)

# Make predictions and evaluate performance for my data 3
y_pred3 = clf.predict(X_test3)
report3 = classification_report(y_test3, y_pred3)

"""Print the classification report for each subset:"""

print("Classification Report for my data 1:")
print(report1)

print("\nClassification Report for my data 2:")
print(report2)

print("\nClassification Report for my data 3:")
print(report3)

"""### c)

Visualize the best split of the Decision tree by considering Entropy as a
measure of node impurity and assuming parameters max depth=[4, 6, 8]
for each my data 1 with 70% train, my data 2 with 60%train and
my data 3 with 50%train data as asked in (b).

[NOTE: Make sure to also consider other parameters of Decision Tree which might improve the performance of classification]

Define a function to visualize the Decision Tree:
"""

def visualize_decision_tree(X_train, y_train, max_depth):
    # Create and fit the Decision Tree classifier
    min_samples_split = 10
    min_samples_leaf = 5
    max_features = 0.8
    max_depth = 10
    criterion = 'entropy'
    clf = DecisionTreeClassifier(
    criterion=criterion,
    max_depth=max_depth,
    min_samples_split=min_samples_split,
    min_samples_leaf=min_samples_leaf,
    max_features=max_features
    )
    clf.fit(X_train, y_train)

    # Plot the Decision Tree
    plt.figure(figsize=(12, 8))
    plot_tree(clf, filled=True, rounded=True, feature_names=X_train.columns)
    plt.show()

"""Visualize the Decision Tree for each subset:

Visualize the Decision Tree for my data 1
"""

visualize_decision_tree(X_train1, y_train1, max_depth=4)

visualize_decision_tree(X_train1, y_train1, max_depth=6)

visualize_decision_tree(X_train1, y_train1, max_depth=8)

"""Visualize the Decision Tree for my data 2"""

visualize_decision_tree(X_train2, y_train2, max_depth=4)

visualize_decision_tree(X_train2, y_train2, max_depth=6)

visualize_decision_tree(X_train2, y_train2, max_depth=8)

"""Visualize the Decision Tree for my data 3"""

visualize_decision_tree(X_train3, y_train3, max_depth=4)

visualize_decision_tree(X_train3, y_train3, max_depth=6)

visualize_decision_tree(X_train3, y_train3, max_depth=8)

"""### d)

Compute and compare the classification performance of tuned Decision Tree
in (c) for each test size my data 1: 30% test data, my data 2: 40% test
data, my data 3: 50% test data in (b).

Display the accuracy scores,
classification report, and confusion matrix respectively.

Define a function to evaluate the performance of the Decision Tree:
"""

def plot_confusion_matrix(cm, classes):
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')

    # Add annotations to each cell
    thresh = cm.max() / 2.0
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                     ha="center", va="center",
                     color="white" if cm[i, j] > thresh else "black")

def evaluate_decision_tree(X_train, y_train, X_test, y_test, max_depth):
    # Create and fit the Decision Tree classifier
    min_samples_split = 10
    min_samples_leaf = 5
    max_features = 0.8
    max_depth = 10
    criterion = 'entropy'
    clf = DecisionTreeClassifier(
    criterion=criterion,
    max_depth=max_depth,
    min_samples_split=min_samples_split,
    min_samples_leaf=min_samples_leaf,
    max_features=max_features
    )
    clf.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = clf.predict(X_test)

    # Compute the accuracy score
    accuracy = accuracy_score(y_test, y_pred)

    # Print the accuracy score
    print("Accuracy Score:", accuracy)

    # Print the classification report
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Compute the confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Plot the confusion matrix with annotations
    plot_confusion_matrix(cm, classes=np.unique(y_test))
    plt.show()

"""Evaluate the performance of the Decision Tree for each test size:

Evaluate the Decision Tree for my data 1
"""

evaluate_decision_tree(X_train1, y_train1, X_test1, y_test1, max_depth=4)

evaluate_decision_tree(X_train1, y_train1, X_test1, y_test1, max_depth=6)

evaluate_decision_tree(X_train1, y_train1, X_test1, y_test1, max_depth=8)

"""Evaluate the Decision Tree for my data 2"""

evaluate_decision_tree(X_train2, y_train2, X_test2, y_test2, max_depth=4)

evaluate_decision_tree(X_train2, y_train2, X_test2, y_test2, max_depth=6)

evaluate_decision_tree(X_train2, y_train2, X_test2, y_test2, max_depth=8)

"""Evaluate the Decision Tree for my data 3"""

evaluate_decision_tree(X_train3, y_train3, X_test3, y_test3, max_depth=4)

evaluate_decision_tree(X_train3, y_train3, X_test3, y_test3, max_depth=6)

evaluate_decision_tree(X_train3, y_train3, X_test3, y_test3, max_depth=8)

"""### e)

Train a Decision Tree classifier on my data 1:

Train DecisionTree with parameters of your choice on my data 1 with
70% train & 30% test data in (b) and display the F1 scores for both train
and test data.
"""

# Create the Decision Tree classifier
clf = DecisionTreeClassifier(max_depth=10)

# Train the classifier on my data 1
clf.fit(X_train1, y_train1)

# Make predictions on the train and test sets
y_train_pred = clf.predict(X_train1)
y_test_pred = clf.predict(X_test1)

# Compute the F1 score for train and test data
train_f1_score = f1_score(y_train1, y_train_pred)
test_f1_score = f1_score(y_test1, y_test_pred)

# Print the F1 scores
print("F1 Score for Train Data:", train_f1_score)
print("F1 Score for Test Data:", test_f1_score)

"""####Showcasing an issue of overfitting or overlearning

Apply pre-pruning to address overfitting:

In addition,
apply three mitigation strategies (1- pre-prunning)
to address the problem of overfitting and display the train
and test F1 scores showing an improvement
"""

# Create the Decision Tree classifier with pre-pruning
clf_pre_pruned = DecisionTreeClassifier(max_depth=10, min_samples_leaf=5)

# Train the classifier on my data 1
clf_pre_pruned.fit(X_train1, y_train1)

# Make predictions on the train and test sets
y_train_pred_pre_pruned = clf_pre_pruned.predict(X_train1)
y_test_pred_pre_pruned = clf_pre_pruned.predict(X_test1)

# Compute the F1 score for train and test data with pre-pruning
train_f1_score_pre_pruned = f1_score(y_train1, y_train_pred_pre_pruned)
test_f1_score_pre_pruned = f1_score(y_test1, y_test_pred_pre_pruned)

# Print the F1 scores with pre-pruning
print("\nF1 Score (with Pre-pruning) for Train Data:", train_f1_score_pre_pruned)
print("F1 Score (with Pre-pruning) for Test Data:", test_f1_score_pre_pruned)

"""Apply post-pruning to address overfitting:

In addition,
apply three mitigation strategies (2-post-prunning)
to address the problem of overfitting and display the train
and test F1 scores showing an improvement
"""

# Create the Decision Tree classifier with post-pruning (using cost-complexity pruning)
clf_post_pruned = DecisionTreeClassifier(ccp_alpha=0.01)

# Train the classifier on my data 1
clf_post_pruned.fit(X_train1, y_train1)

# Make predictions on the train and test sets
y_train_pred_post_pruned = clf_post_pruned.predict(X_train1)
y_test_pred_post_pruned = clf_post_pruned.predict(X_test1)

# Compute the F1 score for train and test data with post-pruning
train_f1_score_post_pruned = f1_score(y_train1, y_train_pred_post_pruned)
test_f1_score_post_pruned = f1_score(y_test1, y_test_pred_post_pruned)

# Print the F1 scores with post-pruning
print("\nF1 Score (with Post-pruning) for Train Data:", train_f1_score_post_pruned)
print("F1 Score (with Post-pruning) for Test Data:", test_f1_score_post_pruned)

"""Apply k-fold cross-validation to address overfitting:

In addition,
apply three mitigation strategies (3-k-fold
cross validation)
to address the problem of overfitting and display the train
and test F1 scores showing an improvement
"""

# Create the Decision Tree classifier for cross-validation
clf_cv = DecisionTreeClassifier(max_depth=10)

# Compute the cross-validated F1 scores
cv_scores = cross_val_score(clf_cv, X_train1, y_train1, cv=5, scoring='f1_macro')

# Compute the average F1 score across the cross-validation folds
avg_cv_score = np.mean(cv_scores)

# Print the cross-validated F1 score
print("\nCross-Validated F1 Score:", avg_cv_score)
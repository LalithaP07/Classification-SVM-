# -*- coding: utf-8 -*-
"""SVM IRIS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DeaVbSAYetTziqQrO86cGr9ojFfJCXtx

# **Classification SVM Project**


Team Members - University of South Dakota

1. Lalitha Priya Bijja
2. Uday Kumar Dasari 


---
"""

# importing libraries
import numpy as np # NumPy for numerical computations
import pandas as pd # Pandas for data manipulation
from sklearn import datasets # Scikit-learn's datasets module for loading the Iris dataset
from sklearn.model_selection import train_test_split, cross_val_score # For splitting data and cross-validation
from sklearn.preprocessing import StandardScaler, LabelEncoder # For data preprocessing
from sklearn.svm import SVC # Support Vector Classifier from scikit-learn
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score # For evaluation metrics

"""**Data Exploration & Preparation**"""

# Load the Iris dataset
iris = datasets.load_iris()

# Split the dataset into features (X) and target variable (Y)
X = iris.data # Features
y = iris.target # Target variable (species)

"""Data Preprocessing

Preprocessing the data by handling missing values, scaling features and encoding categorical variables.
"""

# Check for missing values
missing_values = np.sum(np.isnan(X))
print("Missing Values:\n", missing_values)

# Finding the number of rows and columns in the dataset
num_rows = X.shape[0]
num_columns = X.shape[1]
print("Number of rows:", num_rows)
print("Number of columns:", num_columns)

# Print the shape of the dataset
print("Shape of the dataset (X):", X.shape)

# Display the first few rows of the dataset
print("First few rows of the dataset (X):\n", X[:5])  # Assuming you want to display the first 5 rows

# Convert the feature matrix X to a pandas DataFrame
X_df = pd.DataFrame(data=X, columns=iris.feature_names)

# Check for duplicate rows
duplicates = X_df.duplicated()

# Find and print duplicate rows
duplicate_rows = X_df[duplicates]
print("Duplicate Rows:\n", duplicate_rows)

# Display the labels of the columns
print("Labels of the columns:")
print(iris.feature_names)

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler() # Initialize StandardScaler
X_train_scaled = scaler.fit_transform(X_train) # Scale training features
X_test_scaled = scaler.transform(X_test) # Scale testing features

"""**SVM Implementation**"""

# SVM Implementation
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')  # Example parameters; # Initialize SVM classifier
svm_model.fit(X_train_scaled, y_train) # Train SVM model on the training data

"""Experimenting with different SVM kernels and parameters to find the optimal model for task."""

# Importing GridSearchCV from scikit-learn
from sklearn.model_selection import GridSearchCV

# Define parameter grid for hyperparameter tuning
param_grid = {'C': [0.1, 1, 10, 100], # Regularization parameter values
              'gamma': [1, 0.1, 0.01, 0.001], # Kernel coefficient values for 'rbf', 'poly', and 'sigmoid' kernels
              'kernel': ['linear', 'rbf', 'poly', 'sigmoid']} # Kernel types to be tested

# Instantiate SVM classifier
svm = SVC() # Create an instance of the SVC

# Grid search with cross-validation
grid_search = GridSearchCV(svm, param_grid, cv=5, scoring='accuracy') # GridSearchCV performs exhaustive search over specified parameter values
grid_search.fit(X_train_scaled, y_train) # Fit the grid search model to find the best hyperparameters

# Best parameters
best_params = grid_search.best_params_  # Best combination of hyperparameters
print("Best Parameters:", best_params) # Print best parameters found

# Best model
best_model = grid_search.best_estimator_ # Best model with the best hyperparameters

# Evaluation on test set
y_pred = best_model.predict(X_test_scaled) # Predictions on the test set using the best model
accuracy = accuracy_score(y_test, y_pred) # Calculate accuracy
precision = precision_score(y_test, y_pred, average='weighted') # Calculate precision
recall = recall_score(y_test, y_pred, average='weighted') # Calculate recall
f1 = f1_score(y_test, y_pred, average='weighted') # Calculate F1 score

# Print evaluation metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

"""**K-fold Cross-Validation**"""

# K-fold Cross-Validation
k = 5  # Number of folds
cv_scores = cross_val_score(svm_model, X_train_scaled, y_train, cv=k) # Perform K-fold cross-validation
print("Cross-Validation Scores:", cv_scores) # Print cross-validation scores
print("Mean CV Accuracy:", np.mean(cv_scores)) # Print mean cross-validation accuracy

from sklearn.model_selection import KFold, cross_val_score

# Define the number of folds (e.g., 5 or 10)
k = 5

# Initialize KFold cross-validation
kf = KFold(n_splits=k, shuffle=True, random_state=42)

# Lists to store cross-validation scores
cv_scores = []

# Perform K-fold cross-validation
for train_index, val_index in kf.split(X_train_scaled):
    X_train_fold, X_val_fold = X_train_scaled[train_index], X_train_scaled[val_index]
    y_train_fold, y_val_fold = y_train[train_index], y_train[val_index]

    # Train SVM model on the training fold
    svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
    svm_model.fit(X_train_fold, y_train_fold)

    # Evaluate on the validation fold
    val_score = svm_model.score(X_val_fold, y_val_fold)
    cv_scores.append(val_score)

# Calculate mean cross-validation score
mean_cv_score = np.mean(cv_scores)
print("Mean Cross-Validation Accuracy (Manual):", mean_cv_score)

# Using cross_val_score function
cv_scores_cross_val = cross_val_score(svm_model, X_train_scaled, y_train, cv=k)
mean_cv_score_cross_val = np.mean(cv_scores_cross_val)
print("Mean Cross-Validation Accuracy (cross_val_score):", mean_cv_score_cross_val)

"""**Evaluation Metrics**

Found the accuarcy, precision, recall and F1- score
"""

# Evaluation Metrics
y_pred = svm_model.predict(X_test_scaled) # Predictions on the test set
accuracy = accuracy_score(y_test, y_pred) # Calculate accuracy
precision = precision_score(y_test, y_pred, average='weighted') # Calculate precision
recall = recall_score(y_test, y_pred, average='weighted') # Calculate recall
f1 = f1_score(y_test, y_pred, average='weighted') # Calculate F1 score

# Print evaluation metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

"""**Visualizing the results**

Decision Boundary
"""

# Define a meshgrid of points covering the feature space
x_min, x_max = X_train_pca[:, 0].min() - 1, X_train_pca[:, 0].max() + 1
y_min, y_max = X_train_pca[:, 1].min() - 1, X_train_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

# Make predictions for each point in the meshgrid
Z = svm_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundary and data points
plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=y_train, cmap=plt.cm.coolwarm)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Decision Boundary of SVM on Iris Dataset (PCA)')
plt.show()

"""Confusion Matrix"""

from sklearn.metrics import confusion_matrix  # Import confusion_matrix from sklearn.metrics
import seaborn as sns  # Import seaborn for visualization

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Calculate percentages
conf_matrix_percent = conf_matrix / conf_matrix.sum(axis=1)[:, np.newaxis] * 100

# Plot confusion matrix with percentages
plt.figure(figsize=(8, 6))  # Set figure size for the plot
sns.heatmap(conf_matrix_percent, annot=True, fmt='.2f', cmap='Blues', cbar=False)  # Plot heatmap of the confusion matrix with percentages
plt.title('Confusion Matrix (Percentages)')  # Set title of the plot
plt.xlabel('Predicted Label')  # Set x-axis label
plt.ylabel('True Label')  # Set y-axis label
plt.show()  # Display the plot

"""ROC Curve"""

from sklearn.metrics import roc_curve, auc, precision_recall_curve
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier

# Convert y_test and y_pred to binary format
y_test_bin = label_binarize(y_test, classes=[0, 1, 2])
y_pred_bin = label_binarize(y_pred, classes=[0, 1, 2])

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(len(iris.target_names)):
    fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, i], y_pred_bin[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Plot ROC curve
plt.figure(figsize=(8, 6))
for i in range(len(iris.target_names)):
    plt.plot(fpr[i], tpr[i], lw=2, label='ROC curve (AUC = %0.2f) for class %s' % (roc_auc[i], iris.target_names[i]))

plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

# Compute precision-recall curve for each class
precision = dict()
recall = dict()
for i in range(len(iris.target_names)):
    precision[i], recall[i], _ = precision_recall_curve(y_test_bin[:, i], y_pred_bin[:, i])

# Plot precision-recall curve
plt.figure(figsize=(8, 6))
for i in range(len(iris.target_names)):
    plt.plot(recall[i], precision[i], lw=2, label='Precision-Recall curve for class %s' % iris.target_names[i])

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='lower left')
plt.show()

"""Learning Curve"""

# Import learning curve
from sklearn.model_selection import learning_curve

#Compute learning curve
train_sizes, train_scores, test_scores = learning_curve(
    svm_model, X_train_scaled, y_train, cv=5, n_jobs=-1, train_sizes=np.linspace(.1, 1.0, 5))

# Compute mean and standard deviation of training and test scores across cross-validation folds
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

#Plot learning curve
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, 'o-', color="r", label="Training score")
plt.plot(train_sizes, test_mean, 'o-', color="g", label="Cross-validation score")
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1, color="r")
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.1, color="g")
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.title("Learning Curve")
plt.legend(loc="best")
plt.show()

"""Plotting accuracy"""

import numpy as np

# Calculate accuracy for each class
class_accuracy = []
for i in range(len(iris.target_names)):
    correct_preds = np.sum((y_test == i) & (y_pred == i))
    total_samples = np.sum(y_test == i)
    accuracy = correct_preds / total_samples
    class_accuracy.append(accuracy)

# Plot accuracy for each class
plt.figure(figsize=(8, 6))
plt.bar(iris.target_names, class_accuracy, color='skyblue', edgecolor='black')
plt.title('Accuracy for Each Class')
plt.xlabel('Class')
plt.ylabel('Accuracy')
plt.ylim(0, 1)  # Limit y-axis to range [0, 1]
plt.show()

report = """
Report Summary:
- Explored and prepared the Iris dataset.
- Implemented SVM classifier with rbf kernel.
- Applied K-fold cross-validation with k=5.
- Evaluated model performance using accuracy, precision, recall, and F1-score.
- Found SVM to perform well on Iris dataset with default parameters.

1. Data Exploration and Preprocessing: The Iris dataset was explored to understand its structure and features. Preprocessing steps included handling missing values, scaling features, encoding categorical variables, and checking for duplicate rows.
   There were no missing values, number of rows were = 150, number of columns were = 4
2. SVM Implementation: An SVM classifier was implemented using different kernels and parameters. Grid search with cross-validation was employed to find the optimal hyperparameters for the SVM model, resulting in improved performance.
   The best parameters were
   Best Parameters: {'C': 100, 'gamma': 0.01, 'kernel': 'rbf'}
   Accuracy: 0.9666666666666667
   Precision: 0.9694444444444444
   Recall: 0.9666666666666667
   F1 Score: 0.9664109121909632
3. Applied K-fold cross validation with k=5
   The cross-validation score is
    Mean Cross-Validation Accuracy (Manual): 0.95
    Mean Cross-Validation Accuracy (cross_val_score): 0.95
4. Model Evaluation: The performance of the SVM model was evaluated using metrics such as accuracy, precision, recall, and F1-score. The model demonstrated high accuracy and balanced performance across different classes.
   The results are :
   Accuracy: 1.0
   Precision: 1.0
   Recall: 1.0
   F1 Score: 1.0
5. Visualization: Visualizations such as confusion matrix, ROC curve, precision-recall curve, and learning curve were used to analyze the model's performance and understand its behavior. These visualizations provided valuable insights into the model's strengths and weaknesses.
GitHub Repository Link:
"""
# Print or save the report
print(report)

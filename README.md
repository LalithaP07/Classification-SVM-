# Classification-SVM-
Project Summary:
The project involved building a classification model to predict the species of iris flowers based on their sepal and petal measurements. We utilized the Iris dataset, which contains measurements for three species of iris flowers: Setosa, Versicolor, and Virginica. The classification model was implemented using Support Vector Machine (SVM) and evaluated using various evaluation metrics and techniques such as cross-validation.

Key Findings and Insights:

Explored and prepared the Iris dataset.
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

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Load the data
data = pd.read_csv('flood_data.csv')

# Preprocess the data
# Handle missing values, remove outliers, and normalize/scale features if needed
# ...

# Split the data into features (X) and target variable (y)
X = data[['rainfall_amount', 'rainfall_rate']]  # Add or remove features as needed
y = data['flood_occurrence']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model (Logistic Regression in this example)
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc_roc = roc_auc_score(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1-score: {f1:.2f}')
print(f'AUC-ROC: {auc_roc:.2f}')

# Make predictions on new data
new_data = pd.DataFrame({'rainfall_amount': [100, 50], 'rainfall_rate': [10, 5]})
new_predictions = model.predict_proba(new_data)
print(new_predictions)
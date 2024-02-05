# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

# Create a sample dataset
# data = {
#     'Node': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
#     'Time': [8, 12, 16, 20, 10, 14, 18, 22],
#     'CarCount': [20, 30, 15, 25, 18, 28, 12, 22],
#     'BikeCount': [5, 10, 8, 15, 3, 12, 7, 11],
#     'TruckCount': [2, 5, 3, 6, 1, 4, 2, 3],
#     'TrafficSituation': ['Heavy', 'Moderate', 'Light', 'Moderate', 'Moderate', 'Heavy', 'Light', 'Moderate']
# }

data=pd.read_csv("Traffic.csv")
df = pd.DataFrame(data)

# Convert categorical 'Node' variable to numerical using label encoding
le = LabelEncoder()
df['Node'] = le.fit_transform(df['Node'])

# Separate features (X) and target variable (y)
X = df[['Node', 'Time', 'CarCount', 'BikeCount', 'TruckCount']]
y = df['TrafficSituation']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the decision tree classifier
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
class_report = classification_report(y_test, predictions)

print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')

import pandas as pd
import pickle

# STEP 1: Load dataset
data = pd.read_csv("KDDTrain+_20Percent.txt", header=None)

# STEP 2: Remove last column (difficulty)
data = data.iloc[:, :-1]

# STEP 3: Rename label
data.rename(columns={data.columns[-1]: "label"}, inplace=True)

# STEP 4: Convert label to binary
data['label'] = data['label'].apply(lambda x: 0 if x == "normal" else 1)

# STEP 5: Encoding
data = pd.get_dummies(data)
data.columns = data.columns.astype(str)

# STEP 6: Split X and y
X = data.drop("label", axis=1)
y = data["label"]

# STEP 7: Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# STEP 8: Train model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# STEP 9: Evaluation
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# STEP 10: Save model + columns
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(X.columns, open("columns.pkl", "wb"))

print("Model and columns saved successfully!")
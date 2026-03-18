import pandas as pd

# Step 1: Load dataset
data = pd.read_csv("KDDTrain+_20Percent.txt", header=None)

# Step 2: Remove last column (difficulty)
data = data.iloc[:, :-1]

# Step 3: Rename last column as label
data.rename(columns={data.columns[-1]: "label"}, inplace=True)

# Step 4: Convert label to binary
data['label'] = data['label'].apply(lambda x: 0 if x == "normal" else 1)

# Step 5: Convert categorical to numerical
data = pd.get_dummies(data)

# Step 6: Split features and label
X = data.drop("label", axis=1)
y = data["label"]

print(X.shape)
print(y.shape)
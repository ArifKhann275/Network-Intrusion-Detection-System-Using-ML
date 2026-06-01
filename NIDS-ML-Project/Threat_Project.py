//Write full code

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


files = [
    "Benign-Monday-no-metadata.parquet",
    "Botnet-Friday-no-metadata.parquet",
    "Bruteforce-Tuesday-no-metadata.parquet",
    "DDoS-Friday-no-metadata.parquet"
]
                                       
df_list = []

for file in files:
    temp = pd.read_parquet(file)
    df_list.append(temp)

data = pd.concat(df_list, ignore_index=True)

print(data['Label'].value_counts())



data['Label'] = data['Label'].apply(lambda x: 0 if x == 'Benign' else 1)

print(data['Label'].value_counts())



benign = data[data['Label'] == 0]
attack = data[data['Label'] == 1]

# Benign থেকে equal sample নেওয়া
benign_sample = benign.sample(n=len(attack), random_state=42)

balanced_data = pd.concat([benign_sample, attack])

# shuffle
balanced_data = balanced_data.sample(frac=1, random_state=42)
balanced_data = balanced_data.sample(n=50000, random_state=42)
print(balanced_data['Label'].value_counts())




X = balanced_data.drop('Label', axis=1)
y = balanced_data['Label']
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))



cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

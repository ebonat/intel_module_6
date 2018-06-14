
# A Beginner’s Guide to Neural Networks in Python and SciKit Learn 0.18
# https://www.springboard.com/blog/beginners-guide-neural-network-in-python-scikit-learn-0-18/

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

data_file = "wine_data.csv"

df_wine = pd.read_csv(data_file, names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", 
                                             "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])
# df_wine.info()

df_wine.describe()

df_wine.shape

X = df_wine.drop('Cultivator',axis=1)
y = df_wine['Cultivator']

X_train, X_test, y_train, y_test = train_test_split(X, y)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(13,13,13), max_iter=500)

mlp.fit(X_train,y_train)

predictions = mlp.predict(X_test)

print("Confusion Matrix")
print(confusion_matrix(y_test, predictions))
print()

print("Classification Report")
print(classification_report(y_test, predictions))
print()


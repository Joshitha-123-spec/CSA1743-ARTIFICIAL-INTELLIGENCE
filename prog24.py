from sklearn import tree

# Dataset: [Height, Weight]
X = [[180, 80], [170, 65], [160, 50], [165, 55]]
Y = ["Male", "Male", "Female", "Female"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# Prediction
prediction = clf.predict([[172, 68]])
print("Predicted class:", prediction[0])

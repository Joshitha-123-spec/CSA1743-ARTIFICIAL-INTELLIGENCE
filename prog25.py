import numpy as np

# Sigmoid activation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input data
X = np.array([[0,0],[0,1],[1,0],[1,1]])  # AND Gate
Y = np.array([[0],[0],[0],[1]])

# Initialize weights & bias
np.random.seed(1)
weights = np.random.rand(2,1)
bias = np.random.rand(1)

# Forward pass
for x in X:
    z = np.dot(x, weights) + bias
    output = sigmoid(z)
    print("Input:", x, " Output:", round(float(output),2))

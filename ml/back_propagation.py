import math
import random

# Training Data (XOR)
data = [
  ([0, 0], 0),
  ([0, 1], 1),
  ([1, 0], 1),
  ([1, 1], 0),
]

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def train(data, epochs=50000, lr=0.5):
  w1 = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(2)]
  w2 = [random.uniform(-1, 1) for _ in range(2)]

  b1 = [random.uniform(-1, 1) for _ in range(2)]
  b2 = random.uniform(-1, 1)

  for _ in range(epochs):
    for inputs, target in data:

      h1 = sigmoid(inputs[0] * w1[0][0] + inputs[1] * w1[1][0] + b1[0])
      h2 = sigmoid(inputs[0] * w1[0][1] + inputs[1] * w1[1][1] + b1[1])
      output = sigmoid(h1 * w2[0] + h2 * w2[1] + b2)

      # Backward
      error = target - output
      output_delta = error * output * (1-output)
      h1_delta = h1 * (1-h1) * w2[0] * output_delta
      h2_delta = h2 * (1-h2) * w2[1] * output_delta

      # Update Output
      w2[0] += lr * output_delta * h1
      w2[1] += lr * output_delta * h2
      b2 += lr * output_delta

      # Update Hidden
      w1[0][0] += lr * h1_delta * inputs[0]
      w1[1][0] += lr * h1_delta * inputs[1]

      w1[0][1] += lr * h2_delta * inputs[0]
      w1[1][1] += lr * h2_delta * inputs[1]

      b1[0] += lr * h1_delta
      b1[1] += lr * h2_delta
  return w1, w2, b1, b2

w1, w2, b1, b2 = train(data)

# Testing
print("XOR Predictions: ")
for inputs, target in data:
  h = [
    sigmoid(inputs[0] * w1[0][0] + inputs[1] * w1[1][0] + b1[0]),
    sigmoid(inputs[0] * w1[0][1] + inputs[1] * w1[1][1] + b1[1]),
  ]
  prediction = sigmoid(h[0] * w2[0] + h[1] * w2[1] + b2)
  print(inputs, "-> Predicted: ", round(prediction, 3), "| Expected: ", target)

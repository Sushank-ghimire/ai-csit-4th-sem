import math
import random
import pandas as pd
import numpy as np

def encode_class(mydata):
  classes = []
  for row in mydata:
    if row[-1] not in classes:
      classes.append(row[-1])
  for row in mydata:
    row[-1] = classes.index(row[-1])
  return mydata, classes

def splitting(mydata, ratio):
  train_num = int(len(mydata) * ratio)
  train = []
  test = list(mydata)

  while len(train) < train_num:
    index = random.randrange(len(test))
    train.append(test.pop(index))
  return train, test

def groupUnderClass(mydata):
  data_dict = {}
  for row in mydata:
    class_value = row[-1]
    if class_value not in data_dict:
        data_dict[class_value] = []
    data_dict[class_value].append(row)
  return data_dict

def MeanAndStdDev(numbers):
  avg = np.mean(numbers)
  stddev = np.std(numbers)
  return avg, stddev

def MeanAndStdDevForClass(mydata):
  info = {}
  data_dict = groupUnderClass(mydata)
  for classValue, instances in data_dict.items():
    # Exclude the last column because it is the class label.
    features = [row[:-1] for row in instances]

    info[classValue] = [
      MeanAndStdDev(attribute)
      for attribute in zip(*features)
    ]

  return info

def calculateGaussianProbability(x, mean, stdev):
  epsilon = 1e-10
  exponent = math.exp(-( math.pow(x - mean, 2)/(2 * math.pow(stdev + epsilon, 2))))
  return (1/(math.sqrt(2 * math.pi) * (stdev + epsilon))) * exponent

def calculateClassProbabilities(info, test):
  probabilities = {}
  for classValue, classSummaries in info.items():
    probabilities[classValue] = 1.0
    # Only use the four features
    for i in range(len(classSummaries)):
      mean, std_dev = classSummaries[i]
      x = test[i]
      probabilities[classValue] *= (calculateGaussianProbability(x, mean,std_dev))
    # Normalize probabilities
    total = sum(probabilities.values())
    if total > 0:
      for classValue in probabilities:
        probabilities[classValue] /= total
    return probabilities

def predict(info, test):
    probabilities = calculateClassProbabilities(info,test)
    bestLabel = max(probabilities, key=probabilities.get)
    return bestLabel, probabilities

def accuracy_rate(test, predictions):
  correct = sum(1 for i in range(len(test)) if test[i][-1] == predictions[i])
  return (correct / float(len(test))) * 100.0

# Load Iris dataset
df = pd.read_csv("Iris.csv")

# Remove Id column
if "Id" in df.columns:
  df = df.drop("Id", axis=1)


# Convert DataFrame to list
data = df.values.tolist()

# Encode species
data, class_names = encode_class(data)

# Reproducible split
random.seed(42)

# 80% training, 20% testing
train, test = splitting(data, 0.80)

# Train Gaussian Naive Bayes
info = MeanAndStdDevForClass(train)

# Make predictions
predictions = []
prediction_probabilities = []

for row in test:
  predicted, probabilities = predict(info, row)
  predictions.append(predicted)
  prediction_probabilities.append(probabilities)


# Calculate accuracy
accuracy = accuracy_rate(test, predictions)

print()
print("Gaussian Naive Bayes - Iris Dataset")

print("Total Samples :", len(data))
print("Training      :", len(train))
print("Testing       :", len(test))
print("Accuracy      :", round(accuracy, 2), "%")

print()
print("First 2 test predictions: ")


for i in range(min(2, len(test))):
  actual = test[i][-1]
  predicted = predictions[i]
  probabilities = prediction_probabilities[i]
  actual_name = class_names[actual]
  predicted_name = class_names[predicted]
  status = ("Correct" if actual == predicted else "Wrong")
  print()
  print(f"Test Sample {i + 1}")
  print(f"Sepal Length : {test[i][0]:.2f}")
  print(f"Sepal Width  : {test[i][1]:.2f}")
  print(f"Petal Length : {test[i][2]:.2f}")
  print(f"Petal Width  : {test[i][3]:.2f}")
  print()
  print("Actual Class    :", actual_name)
  print("Predicted Class :", predicted_name)
  print("Status          :", status)
  print()
  print("Prediction Probabilities:")
  for class_id in sorted(probabilities.keys()):
    print(f"{class_names[class_id]:<20}", f": {probabilities[class_id] * 100:.2f}%")


print()
print("Final Accuracy :", round(accuracy, 2), "%")

# Simple dataset
data = [
    ['Sunny', 'Hot', 'No'],
    ['Sunny', 'Mild', 'No'],
    ['Overcast', 'Cool', 'Yes'],
    ['Rain', 'Mild', 'Yes']
]

# -------------------------
# GINI INDEX
# -------------------------

def gini_index(groups, classes):
    total = sum(len(group) for group in groups)
    gini = 0.0

    for group in groups:
        size = len(group)
        if size == 0:
            continue

        score = 0.0
        labels = [row[-1] for row in group]

        for c in classes:
            p = labels.count(c) / size
            score += p * p

        gini += (1 - score) * (size / total)

    return gini


# -------------------------
# ENTROPY (for ID3)
# -------------------------

import math

def entropy(dataset):
    labels = [row[-1] for row in dataset]
    total = len(labels)
    ent = 0

    for value in set(labels):
        p = labels.count(value) / total
        ent -= p * math.log2(p)

    return ent


# -------------------------
# INFORMATION GAIN
# -------------------------

def information_gain(parent, left, right):
    total = len(parent)
    weight_left = len(left) / total
    weight_right = len(right) / total

    gain = entropy(parent) - (weight_left * entropy(left) + weight_right * entropy(right))
    return gain


# Example split
left = data[:2]
right = data[2:]

classes = ['Yes', 'No']

print("Gini Index:", gini_index([left, right], classes))
print("Entropy:", entropy(data))
print("Information Gain:", information_gain(data, left, right))
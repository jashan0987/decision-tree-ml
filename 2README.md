# Decision Tree From Scratch

This project shows a simple implementation of a **Decision Tree** algorithm in Python without using any machine learning libraries.

The aim of this project is to understand how a decision tree works internally.

## Concept

A Decision Tree is a supervised learning algorithm used for **classification problems**.
It splits the dataset into smaller parts based on feature values and makes decisions step by step.

The algorithm chooses the best feature for splitting using:

- Entropy
- Information Gain (ID3)
- Gini Index

## Entropy

Entropy measures the randomness or impurity in the dataset.

Entropy = − Σ p(x) log₂ p(x)

## Gini Index

Gini Index measures how pure a node is.

Gini = 1 − Σ p(x)²

Lower Gini value means better classification.

## Project Structure

decision-tree-ml/
│
├── decision_tree.py
└── README.md

## Language

Python
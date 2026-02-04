# Linear Regression From Scratch

This project demonstrates a simple implementation of Linear Regression without using any machine learning libraries.  
The goal is to understand how linear regression works internally by implementing it step by step using NumPy.

---

## Concept Overview

Linear Regression models the relationship between input and output using a straight line equation:

y = mx + b

Where:
- m is the slope
- b is the intercept

The parameters are updated using **Gradient Descent**, which minimizes the error between predicted and actual values.

---

## Loss Function

The model minimizes the **Mean Squared Error (MSE)**:

MSE = (1 / n) Σ (y − ŷ)²

---

## Project Structure

```text
manchine-learning/
│
├── linear_regression.py   # Linear Regression implementation from scratch
├── README.md              # Project documentation
```

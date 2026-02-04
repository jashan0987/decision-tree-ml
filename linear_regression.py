import numpy as np

class LinearRegression:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.m = 0
        self.b = 0

    def fit(self, X, y):
        n = len(X)

        for _ in range(self.epochs):
            y_pred = self.m * X + self.b

            dm = (-2 / n) * np.sum(X * (y - y_pred))
            db = (-2 / n) * np.sum(y - y_pred)

            self.m -= self.lr * dm
            self.b -= self.lr * db

    def predict(self, X):
        return self.m * X + self.b


if __name__ == "__main__":
    X = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])

    model = LinearRegression()
    model.fit(X, y)

    print("Slope (m):", model.m)
    print("Intercept (b):", model.b)
    print("Prediction for x=6:", model.predict(6))

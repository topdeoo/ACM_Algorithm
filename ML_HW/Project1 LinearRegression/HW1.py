import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
programming on Sept.21/2021
'''


class LinerRegression(object):
    def __init__(self, _alpha=0.001, _cnt=50):
        self.alpha = _alpha
        self.cnt = _cnt
        self.cost_ = []
        self.b = 0
        self.k = 0

    def calc_error(self, X, Y):
        error = 0
        for i in range(len(X)):
            error += (Y[i] - (self.k * X[i] + self.b)) ** 2
        self.cost_.append(error / len(X) / 2 + self.k ** 2 + self.b ** 2)
        return error / len(X) / 2 + self.k ** 2 + self.b ** 2

    def gradient_descent(self, X, Y):
        m = float(len(X))
        for i in range(self.cnt):
            b_temp = 0
            k_temp = 0
            for j in range(len(X)):
                b_temp += (self.k * X[j] + self.b) - Y[j]
                k_temp += ((self.k * X[j] + self.b) - Y[j]) * X[j]
            self.k -= self.alpha * (k_temp / m + 2 * self.k)
            self.b -= self.alpha * (b_temp / m + 2 * self.b)
            self.calc_error(X, Y)

    def show_regression(self, X, Y):
        self.gradient_descent(X, Y)
        # print(self.b, self.k)
        plt.plot(X, Y, 'b.')
        plt.plot(X, self.k * X + self.b, 'r')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

    def show_train_loss(self):
        sns.reset_orig()
        plt.plot(range(1, self.cnt + 1), self.cost_)
        plt.ylabel('cost')
        plt.xlabel('cnt')
        plt.show()

    def show_test_loss(self, X):
        sns.reset_orig()
        plt.plot(range(1, len(X) + 1), self.cost_)
        plt.ylabel("COST")
        plt.xlabel("X")
        plt.show()

    def show_predict(self, X, Y):
        plt.plot(X, Y, 'b.')
        plt.plot(X, self.k * X + self.b, 'r')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

    def show_test(self, X, Y):
        self.cost_.clear()
        for i in range(len(X)):
            self.calc_error(X, Y)
        self.show_test_loss(X)
        self.show_predict(X, Y)


df = np.loadtxt('housing(1).csv', dtype=float, usecols=(2, 13))
'''
??????????????????
'''

train_x = np.array(df[0:400, 0:1])
train_y = np.array(df[0:400, 1:2])
train_x = train_x.flatten()
train_y = train_y.flatten()
print('Input alpha and cnt')
alpha = float(input())
cnt = int(input())
lr = LinerRegression(alpha, cnt)
lr.show_regression(train_x, train_y)
lr.show_train_loss()
'''
???????????????????????????
'''

test_x = np.array(df[400:, 0:1])
test_y = np.array(df[400:, 1:])
test_x = test_x.flatten()
test_y = test_y.flatten()
lr.show_test(test_x, test_y)

'''
???????????????
>1  alpha = 0.001   cnt = 200
>2  alpha = 0.002   cnt = 300
>3  alpha = 0.001   cnt = 1000
>4  alpha = 0.005   cnt = 300
>5  alpha = 0.0025   cnt = 100000

1,3??????????????????alpha????????????????????????????????????????????????
2,4?????????????????????????????????????????????????????????????????????????????????????????????2??????????????????Loss???4???????????????Loss??????
5?????????????????????????????????????????????Loss?????????2???Loss
'''

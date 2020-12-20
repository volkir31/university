# import random
# import matplotlib.pyplot as plt

class Regrietion:
    weight1 = 0
    weight2 = 0
    learning_rate = 0.01
    count_iter = 1500
    cost_list = []
    weight1_list = []
    weight2_list = []

    def hypothesis(self, x):
        return self.weight1 + self.weight2 * x

    def cost(self, weight1, weight2):
        with open('regression.txt') as f:
            count_str = 0
            cost = 0
            for line in f:
                count_str += 1
                population = float(line.split(',')[0])
                profit = float(line.split(',')[1])
                hypothesis = float(weight1) + float(weight2) * population
                cost += (hypothesis - profit) ** 2
        return cost / (2 * count_str)

    def cost_func(self):
        with open('regression.txt') as f:
            count_str = 0
            cost1 = 0
            cost2 = 0
            for line in f:
                count_str += 1
                population = float(line.split(',')[0])
                profit = float(line.split(',')[1])
                hypothesis = self.hypothesis(population)
                cost1 += (hypothesis - profit)
                cost2 += (hypothesis - profit) * population
        return cost1 / count_str, cost2 / count_str

    def gradient_descent(self):
        descent = self.cost_func()
        self.weight1 = self.weight1 - self.learning_rate * descent[0]
        self.weight2 = self.weight2 - self.learning_rate * descent[1]
        self.weight1_list.append(self.weight1)
        self.weight2_list.append(self.weight2)

    def regration(self):
        for i in range(self.count_iter):
            self.gradient_descent()
        print(round(self.weight1, 4), round(self.weight2, 4))
        print(round(self.cost(self.weight1_list[-3], self.weight2_list[-3]), 8),
            round(self.cost(self.weight1_list[-2], self.weight2_list[-2]), 8),
            round(self.cost(float(self.weight1_list[-1]), self.weight2_list[-1]), 8))
        # plt.plot(self.weight1_list)
        # plt.plot(self.weight2_list)
        # plt.show()


def main():
    r = Regrietion()
    l = r.regration()



if __name__ == '__main__':
    main()

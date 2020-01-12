currentCost = 7.556
currentAmount = 3400

transPrice = 6.08
transAmount = 3400


def getCommission(transPrice, transAmount):
    return max(5, transAmount * transPrice * 0.0003)


def calTransCost(transPrice, transAmount, currentCost, currentAmount):
    return (currentCost * currentAmount + getCommission(transPrice, transAmount) + transAmount * transPrice) / (
            currentAmount + transAmount)


transCost = calTransCost(transPrice, transAmount, currentCost, currentAmount)
print("成交价格：" + transPrice.__str__() + " 成交量 " + transAmount.__str__() + " 成本价变为 " + transCost.__str__())

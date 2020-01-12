currentCost = 7.556
currentAmount = 3400

transPrice = 6.08
transAmount = 2100


def get_commission(trans_price, trans_amount):
    return max(5, trans_amount * trans_price * 0.0003)


def cal_trans_cost(trans_price, trans_amount, current_cost, current_amount):
    return (current_cost * current_amount + get_commission(trans_price, trans_amount) + trans_amount * trans_price) / (
            current_amount + trans_amount)


transCost = cal_trans_cost(transPrice, transAmount, currentCost, currentAmount)
print("成交价格：" + transPrice.__str__() + " 成交量 " + transAmount.__str__() + " 成本价变为 " + transCost.__str__())

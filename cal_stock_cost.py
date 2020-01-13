currentCost = 7.0
currentAmount = 3500

transPrice = 5.00
transAmount = 2500


# 根据成交价与成交量计算交易成本价
def cal_trans_cost(trans_price, trans_amount, current_cost, current_amount):
    return (current_cost * current_amount + max(5,
                                                trans_amount * trans_price * 0.0003) + trans_amount * trans_price) / (
                   current_amount + trans_amount)


transCost = cal_trans_cost(transPrice, transAmount, currentCost, currentAmount)
print("成交价格：" + transPrice.__str__() + " 成交量 " + transAmount.__str__() + " 成本价变为 " + transCost.__str__())



# 根据目标成本价和成交价来计算成交量

targetCost = 6.1675


# current_cost * current_amount + max(5,target_amount * trans_price * 0.0003) + target_amount * trans_price = target_cost*(current_amount + target_amount)
# fee=max(5,target_amount * trans_price * 0.0003)
# if target_amount * trans_price * 0.0003>=5

# 暂时假设手续费为5元 因为手续费取最大 则算出两种交易量 也取最大的一个
def cal_target_amount(trans_price, target_cost, current_cost, current_amount):
    return max((current_cost * current_amount + 5 - target_cost * current_amount) - (target_cost - trans_price),
               (current_cost * current_amount - target_cost * current_amount) / (target_cost - trans_price * 1.0003))


targetAmount = cal_target_amount(transPrice, targetCost, currentCost, currentAmount)

print(
    "成交价格：" + transPrice.__str__() + " 目标成本 " + targetCost.__str__() + " 目标交易量 " + targetAmount.__str__() + " 手续费 " + max(
        5, targetAmount * transPrice * 0.0003).__str__())



# pythonStock
Python练习


current_cost * current_amount + max(5,target_amount * trans_price * 0.0003) + target_amount * trans_price = target_cost*(current_amount + target_amount)

情况1：当target_amount * trans_price * 0.0003<5时
此时：
current_cost * current_amount + 5 + target_amount * trans_price = target_cost*(current_amount + target_amount)

current_cost * current_amount + 5 + target_amount * trans_price = target_cost*current_amount + target_cost*target_amount

current_cost * current_amount + 5 -target_cost*current_amount = target_amount(target_cost-  trans_price )

(current_cost * current_amount + 5 -target_cost*current_amount)-(target_cost-  trans_price ) = target_amount

情况2：当当target_amount * trans_price * 0.0003>=5时

current_cost * current_amount + target_amount * trans_price * 0.0003 + target_amount * trans_price = target_cost*(current_amount + target_amount)

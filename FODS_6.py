items_price=[6,5,10,2]
quantites=[3,2,4,1]
discount=10
tax=8
total=sum(price*quantity for price,quantity in zip(items_price,quantites))
discount_amt=(discount/100)*total
total_after_dis=total-discount_amt
tax_amt=(tax/100)*total_after_dis
total_after_tax=total_after_dis+tax_amt
print(total_after_tax)
print(total_after_dis)

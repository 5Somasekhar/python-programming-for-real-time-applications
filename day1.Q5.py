fresh=int(input("Enter the number of fresh loaves purchased"))
old=int(input("Enter the number of day old loaves purchased"))
print("Regular price: Rs.185.00")
fresh_amount = 185.00*float(fresh)
old_amount = (185*0.4)*float(old)
Total = fresh_amount + old_amount
print("Amount of new loaves: Rs", fresh_amount)
print("Amount of day old loaves: Rs", old_amount)
print("Total amount: Rs",Total)

age=int(input("enter your age:"))
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
else:
    price=15
print("your admission price $"+str(price)+"")
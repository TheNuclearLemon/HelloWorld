age=int(input("Age: "))
if age>18:
    print("Your age is above 18")
elif age<0:
    print("Your age below 0")
elif age==18:
    print("Your age is 18")
else:
    print("Your age is less 18")

print("Your age is 18") if age==18 else print("Your age isn't 18")

print("Your age is 18") if age==18 and age<19 and age>17 else print("Your age isn't 18")
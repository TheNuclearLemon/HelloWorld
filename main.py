# break
while True:
    name=input("Your name: ")
    if name!="":
        break

# continue
phone_number="132-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i,end="")

#pass
for i in range(1,21):
    if i ==13:
        pass
    else:
        print(i)
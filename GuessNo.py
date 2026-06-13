Num = 200
n = int(input("Enter a num:"))
count = 1
while n!=Num:
    if n<Num:
      print("Num is low")
        
    elif n>Num:
      print("Num is High")
    count = count + 1
    n = int(input("Enter a num:"))
print("No of Attemps:",count)
print("You win")

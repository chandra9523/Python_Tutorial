#python program to check a number is odd or even

n = int(input("enter a number = "))

if n % 2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")


#Compact way of writing the above program

message = "Number is even" if n % 2 == 0 else "Number is odd"
print(message)

#working with AND and or using if else

num = int(input("enter a number = "))

if num>10 and num % 2 == 0:
    print("Yay!")
else:
    print("No")

if num > 10 or num % 2==0:
    print("Yay!")
else:
    print("No")


#if else program on various cuisine

indian = ["samosa", "daal", "naan"]
chinese = ["Egg Roll","fried rice","pot sticker"]
italian = ["pizza", "pasta","rosotto"]

dish = input("enter a dish name = ")

if dish in indian:
    print(f"{dish} is an indian dish")
elif dish in chinese:
    print(f"{dish} is chinese dish")
elif dish in italian:
    print(f"{dish} is italian dish")
else:
    print("I dont know which cuisine is this")

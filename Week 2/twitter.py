str = input("Input:")
str=str.replace(" ",",")
str = str.translate({ord(i): None for i in 'aeiouAEIOU'})
print(str.replace(","," "))


print("Welcome to the temperature convertor!")
mytemp = str(input("For which degree would you like to convert?\nA)Farenheit to Celcius. \nB)Celcious to Farenheit.\n "))
if mytemp == "A" or 'a':
    farenheit_degree = float(input('Just insert the number please: '))
    p = str((farenheit_degree-32) * (5/9)) + " ºC"
    print(p)
    
elif mytemp == "B" or 'b':
    Celcius_degree = float(input('Just insert the number please: '))
    h = str(Celcius_degree * (9/5) + 32) + " ºF"
    print(h)
else:
    print("Not valid")
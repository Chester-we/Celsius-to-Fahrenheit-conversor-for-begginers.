
print("Welcome to temperature converter!")
#The '\n' function is used to separate the lines and avoid misunderstanding while printing the text
my_temperature = str(input("For which degree would you like to convert?\n A)Farenheit to celcius\n B)Celcius to Farenheit\n"))

#It's stating the condiction if the user types in It's big for or small as well
if my_temperature == "A" or my_temperature == 'a':
    Farenheit_degree = float(input("Just insert the number please: "))
    convrsion = str((Farenheit_degree - 32)*(5/9)) + ' ºC'
    print(convrsion)

elif my_temperature == "B" or my_temperature == 'b':
   Celcius_degree = float(input("Just insert the number please: ")) 
   conversion2 = str((9/5)* Celcius_degree+32) + ' ºF'
   print(conversion2)

else:
    print('Not valid')

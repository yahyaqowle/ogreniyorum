# Day1 #26/7/22
# Eng/ variable # Som/ doorsoome/wax-matale

print("hello World")
print("im Qowle")
print(" I will use for my comments both English and Somali")

first_name = "dost"
last_name = "ayse"
full_name = first_name +" "+ last_name
print("Hello "+full_name)
#to check the type
# print(type(full_name))

age = 29
age += 1
print("Your age is: "+str(age))
print(type(age))

height = 56.98
print('Your height is: '+str(height)+'meter')
# print(type(height))

weight = 500
print('Your weight is: '+str(weight)+"kg/lbs")

human = True
animal = True
Alien = False
earth = human + animal
print("Are you a human: "+str(human))
print('Are Aliens Real: '+str(Alien))
print("Who lives on earth: "+str(earth))

#3.str #Day2 27/7/22
#multiple assignments = allows us to assign multiple variables at the same time in line of code
#dhowr shaqood = wuxuu kuu ogolaan inaad koox doorsamayaal/matalayaal(variables) ah aad badasho.

name2 = "Beerlula2"
age2 = 43
attractive2 = True
print(name2)
print(age2)
print(attractive2)

#example 2 of Beerlula2 #tusaale 2aad'ka Beerlula2
name3, age3, attractive3 = "Beerlula3", 46, True
print(name3, age3, attractive3)

#instead of writing 8lines of code u can reduce to 2 lines of code and is done by multiple assignment
#halkii aad 8 sadar oo kood ah qori laheed waxaa kusoo gaabin karta 2 sadar adoo isticmaalya dhowr-shaqood
Spongebob = 685
Patrick = 685
Sandy = 685
Squidgame = 685

print(Spongebob)
print(Patrick)
print(Sandy)
print(Squidgame)
#example 2 of Spongebob's
Spongebob1 = Patrick1 = Sandy1 = Squidgame1 = 35
print(Spongebob1, Patrick1, Sandy1, Squidgame1)

#4.string method #Day2 27/7/22
#print(len()) it shows the length within variable eg. Jaamac consist of 6 letters
#print(len()) waxaa loo isticmaala si uu kuu tusiyo inta xaraf ee ku jira matalahaaga(variable)
name4 = "Jaamac Diiriye waa nin wanaagsan"
name5 = "743934"
name6 = "Libaax"
print(len(name4))
print(name4.find("J"))
print(name5.isdigit())
print(name6.count("a"))
print(name6*3)
# print(name4.find("D"))
# print(name4.capitalize())
# print(name4.upper())
# print(name4.lower())
# print(name4.isdigit())   #it will show True if it's number otherwise False
# print(name6.isalpha())   #it will show False if the is space between the names in variable name4
# print(name6.replace("L","S"))
# print(name6*5)

#5.type cast #Day2 27/7/22
#Eng/type casting = convert the data type of a value to another data type
#Som/Guurash(typecast) = qiyamka nooca xoggeed ayuu badalaa oo uu ku badala nooc kale oo xog ah

x = 1    #int
y = 2.0    #float
z = "3"  #str in string we cannot normally perform math
print(x)
print(y)
print(z)

#converting both y and z into x(integer) using typecast with example2
x2 = 2
y2 = 4.0
z2 = 6

y2 = int(y2) #for making permanent change to change y2 into integer
z2 = int(z2)
#x2

print(x2)
print(y2)       #it's not permanent to convert y2 to x2
print(z2*6)

#example3 changing values of #string and #integer into float(decimal) type

x3 = 3
y3 = 5.0
z3 = "9"


print(x3)
print(y3)
print(z3)










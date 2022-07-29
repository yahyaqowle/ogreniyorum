# Day1 #26/7/22
# Eng/ variable # Som/ doorsoome/wax-matale

# print("hello World")
# print("im Qowle")
# print(" I will use for my comments both English and Somali")

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
#Eng/ type-casting = convert the data type of a value to another data type
#Som/ Guurash(typecast) = qiyamka nooca xoggeed ayuu badalaa oo uu ku badala nooc kale oo xog ah

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

print(x2)
print(y2)       # print(int(y2) it's not permanent to convert y2 to x2
print(z2*6)

#example3 changing values of #string and #integer into float(decimal) type

x3 = 3
y3 = 5.0
z3 = "9"
#ex.4 if you want to convert from float to string just replace float to str and vice versa
x3 = str(x3)
y3 = str(y3)
z3 = str(z3)
print(x3)
print(y3)
print(z3*10)

#example5
x4 = 5    #int
y4 = 6.0  #float
z4 = 11   #str

print("X4 is "+str(x4))
print("Y4 "+str(y4))
print("Z4 "+str(z4))


#Day3 28/7/22 18:57
#6. user input

name6 = input("What is your name?: ")
age6 = int(input("How old are you?: "))
age6 = age6 + 1
height6 = float(input("How tall are you?: "))
#lines below/above shows how to accept user input with different examples like str, int, float
print("Hello "+name6)
print("Boom!!!~ You are "+str(age6)+" years old now") #we have to convert from int(number/math) to string("words")
print("You are "+str(height6)+" cm/ft tall") #we add +str so code accept from float to str to get displays with words



#day3 28/7/22 18:34
#7.math functions
import math

pi7 = 3.14
x7 = 17
y7 = 25
z7 = 36

print(round(pi7))
print(math.ceil(pi7))  #rounding up
print(math.floor(pi7))
print(abs(pi7))          #absolute(abs) value function
print(pow(pi7, 3))       #power in math ex. 3 to the power of 3 is 27
print(math.sqrt(pi7))    #square root of a value its under math module using (math.)
print(math.sqrt(69))     #hehe gotchuu, noice with 420
print(math.sqrt(420))
print(max(x7,y7,z7))
print(min(x7,y7,z7))

#day3 19:59/22:30 28/7/22
#8.string slicing = create a substring by extracting elements from another string
#                 indexing[] or slice()  = to slice string
#                 [start:stop:step]      = slicing these are the 3 optional arguments

#starting with [index]
name8 = "Dudet What"
#start[0] and stop[4]
first_name8 = name8[0:4]  #beginning no[0;4] of index is inclusive nd u can leave blank [;4] it will auto include
last_name8 = name8[5:9]   # its [5:9]exclusive and u can leave it [5:]
#step in index is optional field that we can set value  #funky_name8 = "shush bitc"

funky_name8 = name8[0:9:3] #for shortcut u can leave start nd stop empty
funky_namee8 = name8[::1]  #here is the shortcut
reversed_name8 = name8[::-1] # u can reverse the word Dudet to teduD

print(first_name8)
print(last_name8)
print(funky_name8)
print(funky_namee8)
print(reversed_name8)

#8.1.string slicing
# slice # string slicing consist of 2(index,slice) above we saw index nd examp's

website8 = "htpps://yahyaqowle.me"  #excluding except website name (yahyaqowle)

slice = slice(8,-3)       #its just like indexing except using ',' instead of ':'

print(website8[slice])
# Day3 finish at 23:37 28/7/22


# Day4 start 15:44 29/7/22
# 9.if statement = a bloc of code that will execute if it's condition is true
# if statement, elif statement, else statement

age9 = int(input("How old are you?: "))

if age9 >= 15:
    print("You are an adult!")
if age9 >= 139:
    print("No way")
    print("You are in a deadbed!")
elif age9 == 100:
    print("Congrats you lived a century!")
elif age9 == 50:
    print("You lived half a century!")
elif age9 == 15:
    print("You are an adult under islamic law!")
elif age9 == 18:
    print("You are an adult under western law/constitutions!")
elif age9 < 5:
    print("You are joking right!")
    print("You are can't even count your fingers!")
else:
    print("You are ciyaal!")

# Day4 16:19 29/7/22
# 10.logical operators(and,or,not) = used to check if two or more conditional statements is true

# example using `and` `or` of logical(l) operators
temp10 = int(input("What is the temperature outside?: "))

if temp10 >= 15 and temp10 <= 30:
    print("The temperature is quite nice")
    print("You lazy ass go outside!")
elif temp10 < 10 or temp10 > 35:
    print("Stay inside!")

# logical operators `not` example
temps10 = int(input("Hava durumu nasil?: "))

if not(temps10 >= 50 and temps10 <= 66):
    print("Cay kaynatabilirsin amk")
elif not(temps10 < 25 or temps10 > 45):
    print("Yuzmek icin muazzam")

#Day4 21:13 29/07/22
#Today i learned something while watching Lex Fridman podcast with George Hotz
#It's that you will never learn if you are watching tutorial and not building your own project
#The motto is "Build while learning"
#Tutorial i'm following Bro Code Python = "https://www.youtube.com/watch?v=XKHEtdqhLK8&t=3844s&ab_channel=BroCode"
#Last one i'm going to do of this tutorial is loop

# 11.while loop = a statement that will execute it's block of code,
#                 as long as it's condition remains true

#while 1==1:        #infinite loop
#   print("Help! I'm stuck in a loop!")

name11 = ""

while len(name11) == 0:
    name11 = input("Enter your name: ")

print("Wassup "+name11)

#So yeah that's it, im going to start my project

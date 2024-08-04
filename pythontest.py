# # # # # # # # # # a= 1
# # # # # # # # # b = 1.3
# # # # # # # # # c= 99j

# # # # # # # # # x= float(a)
# # # # # # # # # y= int(b)
# # # # # # # # # z= complex(a)

# # # # # # # # # print(x)
# # # # # # # # # print(y)
# # # # # # # # # print(z)


# # # # # # # # # print(type(x))
# # # # # # # # # print(type(y))
# # # # # # # # # print(type(z))

# # # # # # # # # import random
# # # # # # # # # print(random.randrange(1,10))

# # # # # # # # # x= int(3.8)
# # # # # # # # # y= float(98)
# # # # # # # # # z= str(3)
# # # # # # # # # print (x,y,z)

# # # # # # # # # d= "jqwedf"
# # # # # # # # # print(d[3])

# # # # # # # # # for x in "banana":
# # # # # # # # #     print(x)

# # # # # # # # # a= "sachin tendulkar"
# # # # # # # # # print(len(a))
# # # # # # # # # print("ten" in a)
# # # # # # # # # if "ten" in a:
# # # # # # # # #     print("Yes, you are right")
# # # # # # # # # print ("ten" not in a)
# # # # # # # # # if "ten" not in a:
# # # # # # # # #     print("Yes, it is not present")
# # # # # # # # # else:
# # # # # # # # #     print("You are wrong, it is there.")

# # # # # # # # # print (a[3:8]) #8th character is not included
# # # # # # # # # print(a[:8])
# # # # # # # # # print(a[8:])

# # # # # # # # # b = "Hello, World!"
# # # # # # # # # print(a[-5:-2])
# # # # # # # # # print(a.upper())
# # # # # # # # # print(a.lower())
# # # # # # # # # print(a.strip())
# # # # # # # # # print(a.replace('s', 'l'))

# # # # # # # # # c= a+" "+b
# # # # # # # # # print(c)
# # # # # # # # # txt= f"He is the best player in cricket. His name is {a}. \n Market value of his bungalow is ${33*400}m.\n \"Goat\". "
# # # # # # # # # print(txt)

# # # # # # # # # x= "Hellp"
# # # # # # # # # y = 99
# # # # # # # # # print(bool(x))
# # # # # # # # # print (bool(y))

# # # # # # # # # class myclass():
# # # # # # # # #   def __len__(self):
# # # # # # # # #     return 0

# # # # # # # # # myobj = myclass()
# # # # # # # # # print(bool(myobj))

# # # # # # # # # mylist= ["dodge", "opel", "honda", "audi", "bmw", "ford"]
# # # # # # # # # print(mylist)

# # # # # # # # # mylist[2:3]= ["merc", "tata"]
# # # # # # # # # print(mylist)

# # # # # # # # # print(mylist[2:4])
# # # # # # # # # mylist.insert(5, "bajaj")
# # # # # # # # # print(mylist)
# # # # # # # # # mylist.append("porsche")
# # # # # # # # # print(mylist)
# # # # # # # # # mylist2 = ["buggati", "Mclaren", "VW", "Jeep", "Lotus"]
# # # # # # # # # print(mylist2)

# # # # # # # # # mylist.extend(mylist2)
# # # # # # # # # print(mylist)

# # # # # # # # # mylist.remove('opel')
# # # # # # # # # print(mylist)
# # # # # # # # # mylist.pop(1)
# # # # # # # # # print(mylist)
# # # # # # # # # mylist.pop()
# # # # # # # # # print(mylist)
# # # # # # # # # del mylist[2]
# # # # # # # # # print(mylist)
# # # # # # # # # print(" \nBreak.\n\n\n New results below. \n Take a break when needed.\n Okay. \n\n")


# # # # # # # # # for x in mylist:
# # # # # # # # #    print(x)
# # # # # # # # # print(len(mylist))

# # # # # # # # # for i in range(len(mylist)):
# # # # # # # # #    print(i)


# # # # # # # # # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # # # # # # # # newlist = []

# # # # # # # # # for x in fruits:
# # # # # # # # #   if "a" in x:
# # # # # # # # #     newlist.append(x)

# # # # # # # # # print(newlist)


# # # # # # # # # firstname = "SJ"
# # # # # # # # # lastname = "PR"
# # # # # # # # # Full_name= firstname +" "+ lastname
# # # # # # # # # print (Full_name)

# # # # # # # # # age = 34
# # # # # # # # # #age = age + 1
# # # # # # # # # age +=1
# # # # # # # # # print(age)
# # # # # # # # # print("His age is : " + str(age))

# # # # # # # # # height = 230.87
# # # # # # # # # print(type(height))
# # # # # # # # # print("Your height is: "+ str(height) + "cm")

# # # # # # # # # human = True
# # # # # # # # # print(type(human))
# # # # # # # # # print("Are you a human? " + (str(human)))

# # # # # # # # # name= "bro Code"
# # # # # # # # # print(name.capitalize())
# # # # # # # # # print(name.find("o"))
# # # # # # # # # print(name.upper())
# # # # # # # # # print(name.lower())
# # # # # # # # # print(name.__len__())
# # # # # # # # # print(len(name))
# # # # # # # # # print(name.count("o"))
# # # # # # # # # print(name.isdigit())
# # # # # # # # # print(name.isalpha())
# # # # # # # # # print(name.isdecimal())
# # # # # # # # # print(name.replace("o","v"))


# # # # # # # # # name = input("What is your name? - ")
# # # # # # # # # age = input("How old are you? - ")
# # # # # # # # # height = input("How tall are you? - ")

# # # # # # # # # print("Hello, " +(name))
# # # # # # # # # print("You are "+ str(age) + "years old")
# # # # # # # # # print("Your height is "+ str(height) + "cm.")

# # # # # # # # import math
# # # # # # # # pi= -4.54

# # # # # # # # x=9
# # # # # # # # y=4
# # # # # # # # z=14

# # # # # # # # # print(round(pi))
# # # # # # # # # #print(math.sqrt(pi ))
# # # # # # # # # print(pow(pi,2))
# # # # # # # # # print(math.ceil(pi))
# # # # # # # # # print(math.floor(pi))
# # # # # # # # # print(abs(pi))

# # # # # # # # # print(max(x,y,z))
# # # # # # # # # print(min(x,y,z))

# # # # # # # # #slicing or indexing
# # # # # # # # #[start:stop:step]
# # # # # # # # name = "Program Kumar"
# # # # # # # # first_name = name[:7]
# # # # # # # # print(first_name)
# # # # # # # # second_name= name[8:]
# # # # # # # # print(second_name)

# # # # # # # # abstract_name = name[::3]
# # # # # # # # print(abstract_name)

# # # # # # # # website1 = "http://google.com"
# # # # # # # # website2 = "http://wikipedia.com"

# # # # # # # # slice= slice(7,-4)
# # # # # # # # print(website1[slice])
# # # # # # # # print(website2[slice])
# # # # # # # # print(website1[slice].upper()+" & "+website2[slice].upper()+ " "+"are a good site to vist.".capitalize())



# # # # # # # age= int(input("How old are you? : "))
# # # # # # # print("Your age is: "+" "+ str(age))

# # # # # # # if age>50:
# # # # # # #     print("You are doing great. Good to have you back here, thanks.")
# # # # # # # elif age>0<=50:
# # # # # # #     print("You are an adult")
# # # # # # # elif age<0:
# # # # # # # #     print("You are not born yet. Go back to sleep.")
# # # # # # # # else:
# # # # # # # #     print("You are not ready for this.")

# # # # # # # temp = int(input("What's the temperature?: "))
# # # # # # # if not(temp > 12 and temp < 30):
# # # # # # #     print("Temp. is good.")
# # # # # # #     print("Go outside!")
# # # # # # # elif temp < 12 or temp > 30:
# # # # # # #     print("Weather is bad outside, \nstay inside.")

# # # # # # # else:
# # # # # # #     print("Wish you luck.")

# # # # # # # name=""
# # # # # # # while len(name) == 0:
# # # # # # #     name = input("What is your name?:")
# # # # # # # print("Your name is "+ name)

# # # # # # name = None
# # # # # # while not name:
# # # # # #     name = input("What's your name?")
# # # # # # print("Your name is good and that is "+ name)



# # # # # # for i in range(10+1):
# # # # # #     print(i)

# # # # # # for i in range(20, 100+1, 2):
# # # # # #     print(i)

# # # # # # for i in "Statesman":
# # # # # #     print(i)

# # # # # # countdown timer

# # # # # # #import time

# # # # # # for i in range(10, 0, -1):
# # # # # #     print(i)  
# # # # # #     #time.sleep(1)

# # # # # # #print("Happy Birthday!") 
# # # # # # 

# # # # # print("hello    ") 

# # # # #print("Hello")

# # # # # import time
# # # # # for i in range(10,0,-1):
# # # # #     print(i)
# # # # #     time.sleep(1)
# # # # # print("HAPPY BIRTHDAY!")

# # # # #make a rectangle

# # # # # Rows = int(input("How many row do you want?:"))
# # # # # Columns = int(input("How many columns do you need?:"))
# # # # # Symbols = input("Which symbol do you want in your design?:")

# # # # # for i in range(Rows):
# # # # #     for j in range(Columns):
# # # # #         print(Symbols, end="")
# # # # #     print(Symbols)

# # # # # loop control statements: break, continue, and pass

# # # # phone_number = "123-456-789"
# # # # for i in phone_number:
# # # #     if i == "-":
# # # #         continue
# # # #     print(i, end="  ")

# # # # #print("Why this sign?")

# # # # phone_number = input("Phone number:")



# # # # for i in range(1, 10):
# # # #     print(i, end="  ")

# # # # for i in range(3):
# # # #     print(3, end="  ")

# # # # print("%")


# # # # phone_number = "908-445-4449"
# # # # for i in phone_number:
# # # #     if i == "-":
# # # #         continue
# # # #     print(i, end="  ")
# # # # print(" ")

# # # # cars = ["Audi", "BMW", "Skoda", "VW", "Mercedes", "Porsche"]

# # # # cars.append("Mclaren")
# # # # cars.pop()
# # # # cars.remove("VW")
# # # # cars.insert(2, "Tata")
# # # # cars.sort()
# # # # cars.clear()

# # # # for i in cars:
# # # #     print(i, end=" ")

# # # #2d lists = a list of list

# # # cars= ["audi", "bmw", "mercedes,", "volvo"]
# # # bikes = ["ducati", "triumph", "tiger", "bmw motarrad"]
# # # truck = ["scania", "volvo", "man", "renault"]

# # # vehicle = [cars, bikes, truck]

# # # print(vehicle[2][3])

# # #tuple = collection which is ordered and unchangedable

# # # student = ("Sjr", 22, "Male", "Engineer")

# # # print(student.count("Sjr"))
# # # print(student.index("Male"))
# # # print((student.index(22)))

# # # for x in student:
# # #     print(x)
# # # if "Male" in student:
# # #     print("That true, he is a male.")

# # #set = collection which is unordered, unindexed, no duplicate values

# # cars = {"Jeep", "G-wagon", "Cayenne", "911", "Ferrari", "BMW"}
# # bikes = {"Ducati", "BMW", "Triumph"}

# # # for x in cars:
# # #     print(x)
# # # for y in bikes:
# # #     print(y)
# # # if x=="B":
# # #     print("True")
# # # else:
# # #     print("False")
# # cars.add("TATA")
# # bikes.add("TATA")
# # cars.add("Audi")
# # cars.remove("Jeep")
# # # bikes.update(cars)

# # # garage= cars.union(bikes)

# # # # for x in garage:
# # # #     print(x)
# # # # # print('Break \n \n')
# # # print(cars.difference(bikes))
# # # print(cars)
# # # print(bikes)
# # # print(bikes.difference(cars))

# # # dictianory = a changeable, unordered collection of unique keys : values pairs

# # capitals = {"USA": "Washington",
# #             "India": "New Delhi"}

# # capitals.update({"Russia": "Moscow"})
# # capitals.pop("USA")

# # # # print(capitals["USA"])
# # # print(capitals.get("India"))
# # # print(capitals.get("UK"))

# # # print(capitals)
# # # print(capitals.keys())
# # # print(capitals.values())
# # # print(capitals.items())

# # # capitals.update({"Germany": "Berlin"})
# # # capitals.update({"India": "Mumbai"})

# # # for key, values in capitals.items():
# # #     print(key, values)

# # mobile = ["Apple", "Samsung", "Blackberry"]

# # print(mobile[0:2])
# # print(mobile[:2])
# # print(mobile[-1:-3])

# name = "tanu booth"

# print(name)
# print(name[2])
# print(name[-3])

# if (name[0:4]).islower:
#     name=name.upper()
# print(name)

# function - is a block of code which is executed only when it is called



# def hello(fname, lname, age): #these are parameters
#     print('Hello there, hope you are doing well' +" "+ first_name +" "+ last_name + ".")
#     print("You are"+" " + str(age) +" "+ "years old.")
#     print("Have a nice day!")



# first_name= "Krish"
# last_name = "Ricky"
# hello(first_name, last_name, 24) #these are arguments


# return statement - function sends python objects/values back to the caller or called as function's return value


# def multiply (no1, no2):
#     x = no1 * no2
#     return x

# y = multiply(4,9)   

# print(str(y)+ " "+ "is your slot, please have a seat there.")


# def multiply (no1, no2):
#     return no1 * no2
     

# y = multiply(4,9)   

# print(str(y)+ " "+ "is your slot, please have a seat there.")

# # keyword arguments - arguments that are preceded by the identifier

# def car (sedan, suv, coupe):
#     sedan = "sclass"
#     suv = "Gls"
#     coupe = "sls"
    
#     print( car ("a", "b", "c"))
# # print(car("a", "b", "c"))

print("Hello")
print("Hello there")
print("Hey  ")
print("hrooo")




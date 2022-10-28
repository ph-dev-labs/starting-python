x = int(input("pick a number"))
if x > 100 :
    y = 20
    z = 40
    print(y, z)


a = int(input("pick a digit"))
if a < 10 : 
    b = 0
    c = 1
    print(b ,c)    

digit = int(input("pick at random"))
if digit < 10 :
    b = 0
    print(b)
else :
    b = 99
    print(b)    


amt1 = int(input("what's the bill"))
amt2 = int(input("what's the second bill"))

if amt1 > 10 and amt2 < 100 :
    if amt1 > amt2 :
        print(amt1)
    else :
        print(amt2)
else :
    print("out of range")


speed = int(input("what's the speed"))
if speed >= 24 and speed < 56 :
    print("speed is normal")  
else : 
    print("speed is abnormal")      

point = int(input("what's the point"))
if point >= 9 and point < 51 :
    print("valid point")  
else : 
    print("invalid point")     
import turtle

if turtle.heading() >= 0 and turtle.heading() <= 45 :
    turtle.penup()


day = int(input("pick a number"))
if day >= 1 and day <= 7 : 
    if day == 1 :
        print("Monday")
    elif day == 2 :
        print("Tuesday")   
    elif day == 3 :
        print("Wednesday")
    elif day == 4 :
        print("Thursday") 
    elif day == 5 :
        print("Friday")
    elif day == 6 :
        print("Saturday") 
    else :
        print("Sunday")
else :
    print("out of range")                                      


length1 = int(input("what is the length of rectangle 1"))
width1 =   int(input("what is the width of rectangle 1")) 

length2 = int(input("what is the length of rectangle 2"))
width2 =   int(input("what is the width of rectangle 2")) 

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2 :
    print(f"area1 is greater an area of {area1 : ,.2f}") 
elif area1 < area2 :
        print(f"area2 is greater an area of {area2 : ,.2f}")
else :
    print(f"area1 and area 2 are the same {area2: ,.2f} {area1 : ,.2f}")        

age = int(input("what's the age"))
if age <= 1 :
    print("alaye is still an infant")
elif age > 1 and age < 13 :
    print("alaye is still a child")
elif age > 13 and age < 20 :
    print("alaye is still a teenager")
else : 
    print("alaye is an ancestor")                



roman = int(input("pick a number"))
if roman >= 1 and roman <= 10 : 
    if roman == 1 :
        print("I")
    elif roman == 2 :
        print("II")   
    elif roman == 3 :
        print("III")
    elif roman == 4 :
        print("IV") 
    elif roman == 5 :
        print("V")
    elif roman == 6 :
        print("VI") 
    elif roman == 7 :
        print("VII")
    elif roman == 8 :
        print("VIII")
    elif roman == 9 :
        print("IX")               
    else :
        print("X")
else :
    print("out of range")                                      


mass = int(input("what's the mass of the object"))
weight = mass * 9.8

if weight > 500 : 
    print("object is too heavy")
elif weight < 100 :
    print("object is too light")
else :
    print("object is normal")        
    
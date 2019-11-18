# import datetime 

year_birth = int(input("what year were you born?"))
# month = input("what month?")
# day = input("what day?")
year_current = int(input("what is the current year?"))
age = year_current - year_birth
candels = int(list(str(age))[-1])


top_c = "i"*candels
happy = "H:a:p:p:y:"
birthday = "B:i:r:t:h:d:a:y:"
mid = ("_"*3+"|" +"_"*22+"|"+"_"*3)
bottom = "~" * 30
top= top_c.center(24,"_")

print(top.center(30))
print(" "*3+"|"+" "*6+happy+" "*6+"|"+" "*3)
print(mid)
print("|"+"^"*28+"|")
print("|"+" "*6+birthday+" "*6+"|")
print("|"+" "*28+"|")
print(bottom)
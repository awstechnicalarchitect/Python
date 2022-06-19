age = int(input("Please Enter your age: "))

if age > 18 and age <=100:
    print ("You are eligible for the License")
   
elif age >7 and age < 18:
    print("Please meet in physical, we will then decide")

elif age == 18:
    print ("You are not eligible fand the License")     
else:
    print("Please provide a valid age")    
# input()

#input("Placeholder")
# input takes every input as string either its integer float or boolean so you need to type cast as per your requiredments

name = input("Enter your Name: ")
print(f"Hi {name}")

age = input("Enter your age: ")
print(f"Your age is: {age}")

# ageAdd = age+1 #Error can only concatenate str (not "int") to str
ageAdd = int(age)+1
print(ageAdd)
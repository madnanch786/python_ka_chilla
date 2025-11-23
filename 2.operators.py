# Operators
'''
Arithmetic Operators: (+,-,*,/,//,**,%)
Logical Operator:(<,>,<=,>=,==,!=)
'''
no1=55
no2=63
print("Arithmatic Operators:")
print("Sum:",no1+no2)
print("Difference:",no1-no2)
print("Product:",no1*no2)
print("Division:",no1/no2)
print("Floor Division:",no1//no2)
print("Exponent:",no1**no2)

#Comparison Operator:(<,>,<=,>=,==,!=) The result of these statements will be false/true, yes/no and 0/1
print("Comparison Operators:")
print(no1<no2)
print(no1>no2)
print(no1<=no2)
print(no1>=no2)
print(no1==no2)
print(no1!=no2)

# Logical Operator (and , or , not)
print("Logical Operators:")
print(no1<no2 and no2==no1) # Return True When both statements are tue
print(no1<no2 or no2==no1)  # Return True When anyone statement is tue
print(not(no1<no2 and no2==no1)) # will reverse the result
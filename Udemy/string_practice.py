mixed_case = "A Song of Ice and Fire"
print (mixed_case.isupper())
print (mixed_case.islower())
print (mixed_case.upper())
print (mixed_case.lower())
print (mixed_case.title())

title_case = (mixed_case.title())
print (title_case)

print ("mixed_case".startswith("mixed_case"))
print ("mixed_case".endswith("mixed_case"))

words = mixed_case.split()
print(words)

print("".join(words).isalpha())  

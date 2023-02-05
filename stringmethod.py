str1 = "My Name is Anant !"

print(str1.upper())   # MY NAME IS ANANT !
print(str1.lower())   #my name is anant !
print(str1.rstrip("!"))  # My Name is Anant
print(str1.replace("!","?"))  # My Name is Anant ?
print(str1.split(" "))  # ['My', 'Name', 'is', 'Anant', '!']
print(str1.capitalize())  # My name is anant !
print(str1.count("a"))  #2
print(str1.endswith("!"))  # True
print(str1.find("is")) #8
print(str1.index("Anant"))  #11
print(str1.isalnum()) # False
print(str1.isalpha()) #False
print(str1.islower()) #False
print(str1.isprintable()) #True
print(str1.isspace()) #False
print(str1.istitle())   #False
print(str1.swapcase())   #mY nAME IS aNANT !
print(str1.title())  #My Name Is Anant !






singular = input()
if singular[-1] in ["s","x"]  or \
    singular[len(singular)-2:] == "ch" :
    print(singular +"es")
elif singular[-1] == "y" and \
    singular[-2] not in ["a","e","i","o","u"] :
    print(singular[:-1] + "ies")
else :
    print(singular + "s") 

import string

def no_lowercase(t) :
    for i in range(len(t)) :
        if t[i] in string.ascii_lowercase :
            return False
    return True

def no_uppercase(t) :
    for i in t :
        if i in string.ascii_uppercase :
            return False
    return True

def no_number(t) :
    for i in t :
        if i in string.digits :
            return False
    return True

def no_symbol(t) :
    for i in t :
        if i in string.punctuation :
            return False
    return True

def character_repetition(t) :
    for i in range(len(t)-3) :
        if t[i] == t[i+1] :
            if t[i+1] == t[i+2] :
                if t[i+2] == t[i+3]:
                    return True
    return False

def number_sequence(t) :
    number_all = "012345678901234567890"
    x = number_all[::-1]
    for i in range(len(t)-3) :
        if t[i:i+4] in number_all or t[i:i+4] in x :
            return True
    return False

def letter_sequence(t) :
    letter = string.ascii_lowercase
    x = letter[::-1]
    t = t.lower()
    for i in range(len(t)-3) :
        if t[i:i+4] in letter or t[i:i+4] in x :
            return True
    return False

def keyboard_pattern(t) :
    punctuation = "!@#$%^&*()_+"
    letter1 = "qwertyuiop"
    letter2 = "asdfghjkl"
    letter3 = "zxcvbnm"
    t = t.lower()
    for i in range(len(t)-3) :
        if t[i:i+4] in punctuation or t[i:i+4] in punctuation[::-1]:
            return True
        elif t[i:i+4] in letter1 or t[i:i+4] in letter1[::-1] :
            return True
        elif t[i:i+4] in letter2 or t[i:i+4] in letter2[::-1] :
            return True
        elif t[i:i+4] in letter3 or t[i:i+4] in letter3[::-1] :
            return True
        else : pass
    return False

password = input().strip()
errors = []
if len(password) < 8 :
    errors.append("Less than 8 characters")
if no_lowercase(password) :
    errors.append("No lowercase letters")
if no_uppercase(password) :
    errors.append("No uppercase letters")
if no_number(password) :
    errors.append("No numbers")
if no_symbol(password) :
    errors.append("No symbols")
if character_repetition(password) :
    errors.append("Character repetition")
if number_sequence(password) :
    errors.append("Number sequence")
if letter_sequence(password) :
    errors.append("Letter sequence")
if keyboard_pattern(password) :
    errors.append("Keyboard pattern")
if len(errors) == 0 :
    print("OK")
else :
    for i in range(len(errors)) :
        print(errors[i])

        
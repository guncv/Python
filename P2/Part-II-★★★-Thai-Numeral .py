def to_Thai(N) :
    dict_number = {"0":"","1":"neung","2":"song","3":"sam"\
        ,"4":"si","5":"ha","6":"hok","7":"chet","8":"paet","9":"kao"}
    out = ""
    m = str(N)
    if N >= 1000 : out += dict_number[m[0]]+" pun "
    if N >= 100 :
        if len(m) == 4 and m[1] == "0" : pass
        else : 
            if len(m) == 4 : out+= dict_number[m[1]]+" roi "
            else : out += dict_number[m[0]] + " roi "
    if N >= 10 :
        if len(m)==4 and m[2] == "0" : pass
        elif len(m) == 3 and m[1] == "0" : pass
        elif len(m)==4 and m[2] == "2" : 
            out += "yi sip "
        elif len(m) == 3 and m[1] == "2" :
            out += "yi sip "
        elif len(m) == 2 and m[0] == "2" :
            out += "yi sip "
        elif len(m) == 4 and m[2] == "1" : out += "sip "
        elif len(m) == 3 and m[1] == "1" : out += "sip "
        elif len(m) == 2 and m[0] == "1" : out += "sip "
        else : 
            if len(m) == 4 : out += dict_number[m[2]] + " sip "
            elif len(m) == 3 : out += dict_number[m[1]] + " sip "
            else : out += dict_number[m[0]] + " sip "
    else : pass
    if m == "0" : out = "soon"
    elif len(m) >1 and m[-1] == "1" : out += "et"
    else : out += dict_number[m[-1]]
    return out

exec(input().strip())
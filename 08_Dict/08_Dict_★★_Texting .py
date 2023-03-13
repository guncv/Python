import string
def text2keys(text) :
    count = {"a":2,"b":22,"c":222,"d":3,"e":33,"f":333, \
        "g":4,"h":44,"i":444,"j":5,"k":55,"l":555,"m":6,\
            "n":66,"o":666,"p":7,"q":77,"r":777,"s":7777,\
                "t":8,"u":88,"v":888,"w":9,"x":99,"y" :\
                    999,"z":9999}
    texts = text.lower()
    key = ""
    for i in texts :
        if i in string.punctuation : pass
        elif i == " " : key += "0" + " "
        else : key += str(count[i]) + " "
    return key.strip(" ")

def  keys2text(keys) :
    count = {"a":2,"b":22,"c":222,"d":3,"e":33,"f":333, \
        "g":4,"h":44,"i":444,"j":5,"k":55,"l":555,"m":6,\
            "n":66,"o":666,"p":7,"q":77,"r":777,"s":7777,\
                "t":8,"u":88,"v":888,"w":9,"x":99,"y" :\
                    999,"z":9999}
    count_new = {}
    for i in count :
        count_new[count[i]] = i
    text = ""
    for i in keys.split(" ") :
        if i == "0" :
            text += " "
        else : text += count_new[int(i)]
    return text
            

exec(input().strip())
        

    
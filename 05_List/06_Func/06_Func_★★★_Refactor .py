def read_date() :
    mname = ["Jan", "Feb","Mar","Apr",\
        "May","Jun","Jul","Aug",\
        "Sep","Oct","Nov","Dec"]
    date1 = input().split()
    d1 = int(date1[0])
    m1 = mname.index(date1[1][:3]) + 1
    y1 = int(date1[2])
    return [d1,m1,y1]

def zodiac(d1,m1) :
    if d1 >= 22 and m1==3 or d1 <=21 and m1==4 : z1 = "Aries"
    elif d1 >= 22 and m1==4 or d1 <=21 and m1==5 : z1 = "Taurus"
    elif d1 >= 22 and m1==5 or d1 <=21 and m1==6 : z1 = "Gemini"
    elif d1 >= 22 and m1==6 or d1 <=21 and m1==7 : z1 = "Cancer"
    elif d1 >= 22 and m1==7 or d1 <=21 and m1==8 : z1 = "Leo"
    elif d1 >= 22 and m1==8 or d1 <=21 and m1==9 : z1 = "Virgo"
    elif d1 >= 22 and m1==9 or d1 <=21 and m1==10 : z1 = "Libra"
    elif d1 >= 22 and m1==10 or d1 <=21 and m1==11 : z1 = "Scorpio"
    elif d1 >= 22 and m1==11 or d1 <=21 and m1==12 : z1 = "Sagittarius"
    elif d1 >= 22 and m1==12 or d1 <=20 and m1==1 : z1 = "Capricorn"
    elif d1 >= 21 and m1==1 or d1 <=20 and m1==2 : z1 = "Aquarius"
    elif d1 >= 21 and m1==2 or d1 <=21 and m1==3 : z1 = "Pisces"
    return z1

def days_in_feb(y) :
    day_feb = 28
    if y % 400 == 0 or y % 100 != 0 and y%4 == 0 :
        day_feb = 29
    return day_feb

def days_in_month(m,y) :
    mname = [1,2,3,4,5,6,7,8,9,10,11,12]
    day_in_month = [31,28,31,30,31,30,31,\
        31,30,31,30,31]
    in_dex = mname.index(m)
    number_of_day = day_in_month[in_dex]
    if number_of_day == 28 :
        if y % 400 == 0 or y % 100 != 0 and y%4 == 0 :
            number_of_day = 29
    return number_of_day

def days_in_between(d1,m1,y1,d2,m2,y2):
    days_in_feb1 = 28
    if y1 % 400 == 0 or y1 % 100 != 0 and y1%4 == 0 :
            days_in_feb1 = 29
    days_in_feb2 = 28
    if y2 % 400 == 0 or y2 % 100 != 0 and y2%4 == 0 :
            days_in_feb2 = 29
    days_in_m1 = days_in_month(m1,y1)
    days_in_m2 = days_in_month(m2,y2)
    days = 0
    if m1 < 12 : days += 31
    if m1 < 11 : days += 30
    if m1 < 10 : days += 31
    if m1 < 9 : days += 30
    if m1 < 8 : days += 31
    if m1 < 7 : days += 31
    if m1 < 6 : days += 30
    if m1 < 5 : days += 31
    if m1 < 4 : days += 30
    if m1 < 3 : days += 31
    if m1 < 2 : days += days_in_feb1
    if m2 > 1 : days += 31
    if m2 > 2 : days += days_in_feb2
    if m2 > 3 : days += 31
    if m2 > 4 : days += 30
    if m2 > 5 : days += 31
    if m2 > 6 : days += 30
    if m2 > 7 : days += 31
    if m2 > 8 : days += 31
    if m2 > 9 : days += 30
    if m2 > 10 : days += 31
    if m2 > 11 : days += 30
    days += (days_in_m1 - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return days

def main() :
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date() 
    print(zodiac(d1,m1),zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))


exec(input().strip())
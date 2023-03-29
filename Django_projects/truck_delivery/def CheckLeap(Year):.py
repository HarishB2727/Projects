def CheckLeap(Year):  
  if((Year % 400 == 0) or  (Year % 100 != 0) and  (Year % 4 == 0)):   
    return True 
  else:  
    return False

def count_sundays(year1,year2,start_day):
    start_date = start_day
    count_days = 0
    Normal_year= {1:2,2:2,3:1,4:3,5:1,6:1,7:2}
    leap_year= {1:2,2:1,3:2,4:1,5:1,6:1,7:3}
    for i in range(year1,year2+1):
        if CheckLeap(i):
            count_days += leap_year[start_date]
            start_date = (366 - (7-start_date))%7 + 1
        else:
            count_days += Normal_year[start_date]
            start_date = (365 - (7-start_date))%7 + 1
    
    return count_days
            
            
print(count_sundays(1901,2000,2))  
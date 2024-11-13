def date_between(date1,date2):
    if date1>date2:
        date1,date2=date2,date1
    for i in range(date1+1,date2):
        print(i)


date_between(1,5)


def date_of_birth(ssn):
    cen = 1800
    if ssn[6]=='-': cen =1900
    elif ssn[6]=='A': cen = 2000
    return (cen +int(ssn[4:6]), int(ssn[2:4]),int(ssn[:2]))


print(date_of_birth('140598+abcd'))

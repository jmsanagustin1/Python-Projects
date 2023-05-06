def jm():
    
    n1=int(input('ENTER FIRST NUMBER: '))
    n2=int(input('ENTER SECOND NUMBER: '))
    print()
    if n1 == n2:
        print ("EQUAL")
    elif n1 < n2:
        sum=n1+n2
        print ("SUM", str(sum))
        print ('NOT EQUAL')
        
    elif n1 > n2:
        dif=n1-n2
        print("DIFFERENCE", str(dif))
        print ('NOT EQUAL')
jm()

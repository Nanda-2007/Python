def sd(name,usn,m1,m2,m3):
    t=m1+m2+m3
    p=t/3
    print('Student Details')
    print('Name:',name)
    print('USN:',usn)
    print('Total:',t)
    print(f'Percentage:{p:.2f}')
n=(input('Enter Name:'))
u=(input('Enter USN:'))
m1,m2,m3=map(int,input('Enter 3 sub Marks:').split())
sd(n,u,m1,m2,m3)

    
    
    

def gcd(a,b):
    if(a>b):
        temp=b
    else:
        temp=a;
    for i in range(1,temp+1):
        if(a%i==0 and b%i==0):
            result=i;
    return result

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
value=gcd(a,b)
print(value)


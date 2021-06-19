#Program to Convert Decimal to Binary, Octal and Hexadecimal

n=int(input("Enter the decimal number:"))
def binarynum(n):
    binary=[]
    while(n>0):
        dig=n%2
        binary.append(dig)
        n=n//2
    binary.reverse()
    print("Binary Number: ")
    for i in binary:
        print(i,end="")

def octalnum(n):
    octal=[]
    while(n>0):
        dig=n%8
        octal.append(dig)
        n=n//8
    octal.reverse()
    print("Octal Number: ")
    for i in octal:
        print(i,end="")

def hexadecnum(n):
    hexa=[]
    while(n>0):
        dig=n%16
        if(dig<10):
            hexa.append(dig)
        elif(dig==10):
            hexa.append('A')
        elif(dig==11):
            hexa.append('B')
        elif(dig==12):
            hexa.append('C')
        elif(dig==13):
            hexa.append('D')
        elif(dig==14):
            hexa.append('E')
        else:
            hexa.append('F')
        n=n//16
        hexa.reverse()
        print("Hexadecimal Number: ")
        for i in hexa:
            print(i,end="")


binarynum(n)
print()
octalnum(n)
print()
hexadecnum(n)

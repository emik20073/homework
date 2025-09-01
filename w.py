number=int(input("enter a number: "))
a=number%10
b=(number//10)%10
c=(number//100)%10
d=(number//1000)%10
e=number//10000

print(a,b,c,d,e,sep="")
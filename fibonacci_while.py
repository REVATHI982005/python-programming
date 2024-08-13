print("Fibonacci Sequence")
num=int(input("Enter length of series :"))
a=0
b=1
print("Fibonacci sequence using for loop")
print("{}\n{}".format(a,b))
for i in range(num-2):
    sum=a+b
    print(sum)
    a=b
    b=sum
    

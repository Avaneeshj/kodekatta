a=int(input())
if a>1:
    for i in range(2,a//2):
        if(a%i==0):
            print("no")
            break
        else:
            print("yes")

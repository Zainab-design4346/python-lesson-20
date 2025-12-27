def pal(tup):
    end=len(tup)-1
    start=0
    while start<end:
        if tup[start]!=tup[end]:
            return False
        start+=1
        end-=1
    return True


tup=(1,2,3,3,2,1)
if pal(tup):
    print("palindrome")
else:
    print("Not palindrome")

def avgfun(num):
    list1=list(num)
    sum=0
    for x in list1:
        sum=sum+x
    return sum

n=(12,34,56,23,56,78,90,65,8,9)
print("Tuple:",n)
print("Average:",avgfun(n)/len(n))
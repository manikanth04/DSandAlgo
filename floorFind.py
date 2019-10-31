
def floorFindAdhocScan(n,x):
    if x > n[len(n)-1]:
        return n[len(n)-1]
    for i in range(len(n)):
        if n[i] < x:
            continue
        else:
            floorVal=n[i-1]
            return floorVal
def floorFindDP(n,x):
    l=0
    r=len(n)-1
    m=0

    while l < r:
        m=int(l+(r-l)/2)
        if n[m] == x:
            print("In first if")
            return n[m]
        if l==m:
            return n[r]
        if n[m] < x :
            l=m
        else:
            r=m-1
    return n[r]
if __name__=='__main__':
    n=[5,8,10,15,18,23,25]
    x=6
    print(floorFindAdhocScan(n,x))
    print(floorFindDP(n,x))

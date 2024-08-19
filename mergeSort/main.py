def MergeSort(a,p,r):
    if(p<r):
        q=(p+r)//2
        MergeSort(a,p,q)
        MergeSort(a,q+1,r)
        Merge(a,p,q,r)

def Merge(a,p,q,r):
    L=[]
    R=[]
    for i in range (p,q+1):
        L.append(a[i])
    L.append(1000000000000000000000000)
    
    for j in range (q+1,r+1):
        R.append(a[j])
    R.append(1000000000000000000000000)
    
    i=0
    j=0
    
    for k in range (p,r+1):
        if(L[i]<R[j]):
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1


a=[12,183,-85,-78,65,15,8]
MergeSort(a,0,len(a)-1)
print(a)

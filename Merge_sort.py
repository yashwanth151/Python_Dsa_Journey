def merge_sort(arr):
    helper(arr,0,len(arr)-1)
    return arr

def helper(A,start,end):
    #base case
    if start ==end:
        return
    #internal node
    mid=(start+end)//2
    helper(A,start,mid)
    helper(A,mid+1,end)
    i=start
    j=mid+1
    aux=[]
    while i<=mid and j<=end:
        if A[i]<=A[j]:
            aux.append(A[i])
            i+=1
        else:
            aux.append(A[j])
            j+=1
    while i<=mid:
        aux.append(A[i])
        i+=1
    while j<=end:
        aux.append(A[j])
        j+=1
    A[start:end+1]=aux
    return

A=[7,5,1,34,9,33,00,12,3,77,8,90,3,5,99]
print(merge_sort(A))
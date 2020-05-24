https://www.linkedin.com/in/mohammad-taukir-ansari-734008179

def prefix(arr_list,n):
    if(n==0):
        return ""
    if n==1:
        return arr_list[0]
    copy = sorted(arr_list)
    min_str = min(len(copy[0]),len(copy[n-1]))

    i=0
    while(i<min_str and copy[0][i]==copy[n-1][i]):
        i+=1
    return copy[0][:i]

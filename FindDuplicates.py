def duplicate(st):
    d={}
    for i in st:
        if d.get(i,0):
            d[i]+=1
        else:
            d[i]=1
    for key,value in d.items():
        if d[key]>1:
            print(key)
        


st="ashish"
duplicate(st)

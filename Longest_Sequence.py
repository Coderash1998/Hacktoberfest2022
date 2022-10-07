word="hackerrank"
k=0|0


def longstring(word,k):
    res=""
    maxstring=""
    res+=word[0]
    for i in range(len(word)-1):
        if (abs(ord(word[i])-ord(word[i+1]))<=k):
            res+=word[i+1]
        else:
            if (len(res)>len(maxstring)):
                maxstring=res
            res=""
            res+=word[i+1]

    if maxstring=="":
        return res
    else:
        return maxstring
    
print(longstring(word,k))

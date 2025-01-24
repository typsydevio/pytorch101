def returnSubstring(s):
    substringArr = []
    for idx in range(0,len(s)):
        tempStr = s[idx]
        for i in range(idx+1, len(s)):
            if s[i] in tempStr:
                substringArr.append(tempStr)
                break
            else:
                tempStr += s[i]
    
    tempVal = substringArr[0]
    for i in  substringArr:
        if len(i) > len(tempVal):
            tempVal = i
    
    return [len(tempVal), tempVal]

print(returnSubstring('bbbbbb'))
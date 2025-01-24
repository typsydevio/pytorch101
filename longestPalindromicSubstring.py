def palindromicString(s):
    """
    return longest palindromic substring

    Approach 1: 2 use cases

    1. traversing string left to right, we look for palindromes
    2. traversing string from endpoints towards median

    Final approach:

    traverse script from left to right but each time up the primary search index by 1.

    For example, if input string is "babad", the first search should start from index 0 i.e 'b'
    the internal search should start looking for palindromic substrings from this character all the way towards the end
    any strings found should be appended in an array
    now, update the index to previdx + 1, and repeat.

    This can also be done using an idx pointer and a recursive function.

    """

    palindromeList = []
    for idx in range(0,len(s)):
        for i in range(idx, len(s)+1):
            tempstr = s[idx:i]
            if tempstr[::-1] in s:
                palindromeList.append(tempstr)
    
    tempVal = palindromeList[0]
    for i in palindromeList:
        if len(i) > len(tempVal):
            tempVal = i

    return tempVal

print(palindromicString('abc123321pqr567765rqp'))
def first_non_repeating_char(stream):
    freq={}
    for i in stream:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in stream:
        if freq[i]==1:
            return i
    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )

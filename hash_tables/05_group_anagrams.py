def group_anagrams(words):
    groups={}
    for word in words:
        keys=" ".join(sorted(word))
        if keys not in groups:
            groups[keys]=[]
        groups[keys].append(word)
    return list(groups.values())

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    
    result = ""
    base = strs[0]

    for i in range(len(base)):
        for word in strs[1:]:
            if len(word) == i or word[i] != base[i]:
                return result
        
        result += base[i]
    
    return result


n = int(input("How many string do you want to enter? "))
strs = []

for i in range(n):
    item = input(f"Enter string {i+1}: ")
    strs.append(item)

print(strs)

print(longestCommonPrefix(strs))
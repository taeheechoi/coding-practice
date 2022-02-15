
l1 = [1, 2, 4, 6, 11]
l2 = [3, 4, 5, 10, 25]


def sortTwoArrays(l1, l2):
    print(sorted(l1 + l2))
    i, j = 0, 0 
    result = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            result.append(l2[j])
            j += 1
        else:
            i +=1
            j +=1
    
    if len(l1) == i:
        result += l2[j:]
    if len(l2) == j:
        result += l1[i:]
    print(result)
    
    

sortTwoArrays(l1, l2)
# How do you find all pairs of an integer array whose sum is equal to a given number? (solution)

def find_pairs_with_sum(lst,target):
    result =[]

    for element in lst:
        complement = target-element
        if complement in lst:
            result.append((complement,element))
    return result
lst = [1,2,3,4,5,6,7,8,]
target = 4
print(find_pairs_with_sum(lst,target))
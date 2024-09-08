def laba1(lst):
    n = len(lst)
    for i in range(n-2):
        if sorted(lst[i:i+3]) == [1, 2, 3]:
            return True
    return False

lst = [4, 2, 1, 2, 5, 5, 6, 3, 2, 2]
print(laba1(lst))
from collections import Counter

def most_frequent_element(lst):
    if not lst:
        return None
    count = Counter(lst)
    return count.most_common(1)[0][0]

print(most_frequent_element([1, 3, 2, 1, 4, 1, 3]))  
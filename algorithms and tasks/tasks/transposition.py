"""General tasks"""
import collections

"String 1 is transposition of string 2"
# O(n * logN)
string_1 = 'abcd'
string_2 = 'acdb'
print(sorted(string_2) == sorted(string_1))


# O(n)
def same_permutation(a, b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.values())


print(same_permutation(string_1, string_2))

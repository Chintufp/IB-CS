def find_all(s, sub):
    result = []
    start = 0
    while (x := s.find(sub, start)) != -1:
        result.append(x)
        start = x + 1
    return result

s = 'ababab'

print(find_all(s, 'aba'))
print(find_all(s, 'ab'))
print(find_all(s, 'b'))
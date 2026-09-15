def dashyfy_substring(s, sub):
    i = s.find(sub)
    if len(sub) == 0:
        return s
    return s.replace(sub, f"-{sub}-", 1)

print(dashyfy_substring("foo", "o")) 
print(dashyfy_substring("foobar", "oba")) 
print(dashyfy_substring("foobar", "f")) 
print(dashyfy_substring("foobar", "bar")) 
print(dashyfy_substring("foobar", "")) 



def file_type(s):
     i = s.rfind('.')
     return s[i+1:]

print(file_type("foo.doc"))
print(file_type("foo."))
print(file_type(""))
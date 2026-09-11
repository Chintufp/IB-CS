txt = 'foo.bar.what.txt'
def lastDotKept(s):
    new = s.replace('.','-dot-',(s.count('.')-1))
    return new

print(lastDotKept(txt))
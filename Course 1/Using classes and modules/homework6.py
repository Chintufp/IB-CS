def max_chat_rep(s):
    if not s:
        return 0
    max_count = 1
    current_count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1
    return max(max_count, current_count)

print(max_chat_rep('abcd'))
print(max_chat_rep('abbbcdd'))
print(max_chat_rep('abbbcddddd'))
print(max_chat_rep(''))
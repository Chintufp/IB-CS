import time
def read_words_from_url(url):
    import requests

    res = requests.get(url, stream=True)
    words = [line.decode('utf-8').strip() for line in res.iter_lines()]

    return words

words = read_words_from_url("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt")

def seq_search(key, array):
    index = 0 
    found = False

    while not found and index < len(array):
        if array[index] == key:
            found = True
        index +=1

    return found

def bin_search(key, array):
    lo = 0
    hi = len(array) -1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = array[mid]
        if key == val: 
            return True
        elif key < val:
            hi = mid -1
        else:
            lo = mid +1
    return False

def time_diff(search_func, key, data):
    start = time.process_time()
    search_func(key, data)
    end = time.process_time()
    return end - start


# 1. 
# print(words[-10:])

# 2.
# print(seq_search("potato", words))
# print(seq_search("shubham", words))

#3
# print(bin_search("potato", words))
# print(bin_search("shbuam", words))

4.
print(time_diff(seq_search, "potato", words))
print(time_diff(seq_search, "shubham", words))
print()
print(time_diff(bin_search, "potato", words))
print(time_diff(bin_search, "shubham", words))
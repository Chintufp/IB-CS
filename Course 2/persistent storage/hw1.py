import random, pathlib, pickle
#10000 random ints
ints = [random.randint(0, 10000) for _ in range(10000)]

file_path = pathlib.Path('data') / 'ints.txt'
# save as list if file does not exist
if not file_path.exists(): 
    f = open(file_path, 'w') # open file for writing 
    for i in ints: print(i, file=f) # write each int to file
    f.close() # close file 
     
# read
with open(file_path) as f: 
    ints_read = [int(line) for line in f] # read each line and convert to int

# 4. 
file_path = pathlib.Path('data') / 'ints.ser'
f = open(file_path, 'wb') # open file for writing binary data
pickle.dump(ints, f) # save into da file
f.close() # close da file

#read
f = open(file_path, 'rb') # open file for reading binary data
ints_read = pickle.load(f) # read da file
f.close() # close da file

print(ints_read[:10]) # print first 10 ints
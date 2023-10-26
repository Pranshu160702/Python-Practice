f = open('myFile.txt', 'r')
# r for read, w for write and a for append .. R is default if given nothing
# t for text file and b for binary like jpg etc. (rt,rb,etc.)
print(f)

msg = f.read()
print(msg)
f.close()

f = open('myFile.txt', 'w')
f.write("This is the next message")
f.close()

f = open('myFile.txt', 'a')
f.write("\nThis is appending a message")
f.close()

f = open('myFile.txt', 'r')
new_msg = f.read()
print(new_msg)
f.close
print()

# If you dont wanna type f.close again and again do this instead

with open('myFile.txt', 'r') as f:
    msg = f.read()
    print("This is using with command : " + msg)

# Read line by line
with open('myFile.txt', 'r') as f:
    i = 1
    while True:
        line = f.readline()
        if not line:
            break
        print("This is line " + str(i) + " : " + line)
        i += 1
        
# f.seek(10) -> Used to seek to the speicified index
# print(f.tell()) -> Used to tell till what index we have seeked already
# f.truncate(5) -> Only upto index 5 the text is kept besides all is erased
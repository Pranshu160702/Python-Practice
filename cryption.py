msg = str(input("Enter A Message : "))
random1 = "cia"
random2 = "una"
# Encoding

# letters = []
# for letter in msg:
#     letters.append(letter)

if(len(msg) > 2):
    # a = letters[0]
    # letters.reverse()
    # letters.pop()
    # letters.reverse()
    # letters.append(a)
    encoded_msg = random1 + msg[1:] + msg[0] + random2
else:
    encoded_msg = msg[::-1]
    
print("Encoded Msg : " + encoded_msg)

# Decoding 

if(len(msg) <=2):
    decoded_msg = encoded_msg[::-1]
else:
    enc_list = []
    for letter in encoded_msg[3:-3]:
        enc_list.append(letter)
    a = enc_list[len(enc_list) - 1]
    enc_list.pop()
    enc_list.reverse()
    enc_list.append(a)
    enc_list.reverse()
    
    # print(enc_list)
    decoded_msg = ""
    for chr in enc_list:
        decoded_msg = decoded_msg + chr
    
print("Decoded Msg : " + decoded_msg)
    
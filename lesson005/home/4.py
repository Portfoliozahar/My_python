
def rle_enc(data):
    enc = ''
    a = ''
    c = 1

    if not data: return ''
    for i in data:  
        if i != a:    
            if a:
                enc += str(c) + a
            c = 1
            a = i
        else: 
            c += 1
    else:
        enc += str(c) + a
        return enc
    
    
    
def rle_dec(data):
    dec = ''
    c = ''
    for i in data:
        if i.isdigit():     
            c += i
        else:  
            dec += i * int(c)
            c = ''
    return dec    

with open('RLE.txt') as data:
    for rle in data:
        print (rle)

encoded_val = rle_enc(rle)
print(encoded_val)
decoded_val = rle_dec(rle)
print(decoded_val)


#
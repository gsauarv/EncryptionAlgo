from string import printable as letters 

def encrypt(message="Hello",key=3):
    cipher=[]
    for i in message:
        index=letters.find(i)
        new_index=(index+key)%len(letters)
        cipher_char=letters[new_index]
        cipher.append(cipher_char)
    return cipher   
        
def decrypt(en="khoor",key=3):
    plain=[]
    for i in en:
        index=letters.find(i)
        new_index=(index-key)%len(letters)
        plain_char=letters[new_index]
        plain.append(plain_char)
    return plain


print(encrypt(message="Hello",key=3))
print(decrypt(en="khoor",key=3))
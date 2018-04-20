import time
n = 21971
e = 131
d = 17867

message = """:H:"""
encrypted_message = ""
decrypted_message = ""

start = time.time()
##Decryption##
for t in encrypted_message:
    numerize = ord(t)
    decrypt = pow(numerize, d, n)
    denumerize = chr(decrypt)
    decrypted_message += denumerize
    
print decrypted_message

end = time.time()

print (end - start)

LUT_encryption = dict()



##Encrypt##
for x in message:
    numerize = ord(x)
    encrypt = pow(numerize, e, n)
    denumerize = unichr(encrypt)
    encrypted_message += denumerize
    
print encrypted_message

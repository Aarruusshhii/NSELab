import hashlib

data = "Hello Security Lab".encode()


hash_val = hashlib.sha256(data).hexdigest()
print("SHA-256 Hash:", hash_val)


data2 = "Hello Security Lab".encode()    
data3 = "Hello Hacked Lab".encode()      

print("Hash match:", hashlib.sha256(data).hexdigest() == hashlib.sha256(data2).hexdigest())
print("Hash match after modification:", hashlib.sha256(data).hexdigest() == hashlib.sha256(data3).hexdigest())


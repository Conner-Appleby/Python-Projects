import hashlib

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

#Example 
password = "testpassword1234"
hashed_password = hash_password(password)
print("Hashed Password:", hashed_password)

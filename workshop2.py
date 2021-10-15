# important hashlib library
import hashlib

# create a variable with a string (data type) to encode
string = "unhashed message"

# encode string - strings must be encoded before using sha256 hash
# I believe this is coverting the data type of your input so it can be hashed. Basically, it is changing the format of the data so that it can be encrypted
encoded = string.encode()

# hash the encoded message (output is in hexadecimal)
result = hashlib.sha256(encoded)

print(string) # unhashed message
print("Hash Value : ", result) # this is the encoded message before it is hashed
print("Hexadecimal equivalent: ",result.hexdigest()) # this is the SHA256 hash value of the message
print("Digest Size :", result.digest_size) # The size of the resulting hash in bytes
print("Block Size :", result.block_size) # The internal block size of the hash algorithm in bytes
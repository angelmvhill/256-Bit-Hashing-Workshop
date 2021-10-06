# #  important hashlib library
import hashlib

# # create a variable with a string (data type) to encode
# string = "unhashed message"

# # encode string - strings must be encoded before using sha256 hash
# encoded = string.encode()

# # hash the encoded message
# result = hashlib.sha256(encoded)
# print(result)
# # print("String : ", end ="")
# # print(string)
# # print("Hash Value : ", end ="")
# # print(result)
# print("Hexadecimal equivalent: ",result.hexdigest())
# # print("Digest Size : ", end ="")
# # print(result.digest_size)
# # print("Block Size : ", end ="")
# # print(result.block_size)

print(hashlib.hexdigest('www'))
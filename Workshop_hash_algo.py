from Crypto.Hash import SHA256

# h = SHA256.new()
h = 'hello world'
# h.update(b'Hello')
print(h.hexdigest())
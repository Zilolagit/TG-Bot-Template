import bcrypt
print(bcrypt.hashpw("123".encode(), salt=bcrypt.gensalt()))
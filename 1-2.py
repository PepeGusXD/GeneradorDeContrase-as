import random
c="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
n=int(input("LONGITUD DE LA CONTRASEÑA: "))
password=""
for i in range(n):
    password = password + random.choice(c)
print("TU CONTRASEÑA ES",password)

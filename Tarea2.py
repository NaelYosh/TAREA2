import random 
digit_passwords = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
longitud = int(input ("¿Cuántos dígitos quieres que tenga tu contraseña?"))
password = ""
for i in range(longitud):
    password += random.choice(digit_passwords)
print (password) 


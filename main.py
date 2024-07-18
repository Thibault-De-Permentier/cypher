from caesarCode import CaesarCode

text = "je suis une carrote qui saute"

print(CaesarCode.crypt(text, 8))
print(CaesarCode.decrypt(CaesarCode.crypt(text,8),8))
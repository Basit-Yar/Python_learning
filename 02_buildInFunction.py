# About abs() --> is absolute method | It always return a non-negative value.
# It also provides the absolute value of complex number
# =============================================================================

x = -45
print(abs(x))
print("========================")
print(abs(-43.456))
print(abs(3.14))
print(abs(-3+2)) # it will only provide the last result in positve.
print("========================")
print(abs(3+2j))
print(abs(3+5j))

print("============================================================================")

# bin() --> is used to convert an integer to its binary representation in the form of a string.
# The resulting string starts with the prefix "0b" to indicate that it's in binary format. 
# ===============================================================================================

print("The binary value of 1 : " + bin(1))
print("The binary value of 2 : " + bin(2))
print("The binary value of 3 : " + bin(3))
print("The binary value of 4 : " + bin(4))
print("The binary value of 5 : " + bin(5))
print("The binary value of 8 : " + bin(8))
print("The binary value of 11 : " + bin(11))
print("The binary value of 111 : " + bin(111))
print("The binary value of 20000 : " + bin(20000))

print("=============================================================================")

# complex() --> is used to create a complex number like 2+3j
# =============================================================

print(complex(2, 4)) # the first arg is for real number and the second one is for imaginary number

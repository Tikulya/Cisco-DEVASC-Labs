

print("=== Data Types ===")
print(type(98))
print(type(98.6))
print(type("Hi!"))
print(type(True))

print("\n=== Variables ===")
x = 3
print("x * 5 =", x * 5)

str1 = "ya"
str2 = "love"
str3 = "tebya"
print(str1, str2, str3)

print("\n=== Lists ===")
hostnames = ["R1", "R2", "R3", "S1", "S2"]
hostnames[0] = "RTR1"
del hostnames[3]
print(hostnames)

print("\n=== Dictionaries ===")
ipAddress = {
    "R1": "10.1.1.1",
    "R2": "10.2.2.1",
    "R3": ["10.3.3.1", "10.3.3.2", "10.3.3.3"],
    "S1": "10.1.1.10"
}
print(ipAddress)

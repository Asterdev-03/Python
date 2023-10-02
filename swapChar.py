str1 = "ZABCZZZDEFZ"
l = list(str1)

print(l)

for i in range(1, len(l), 2):
    l[i] = "@"

str1 = "".join(l)
print(str1)
str2 = ""
for i in range(len(str1)):
    if str1[i] != '@':
        str2 = str2 + str1[i]

print(str2)

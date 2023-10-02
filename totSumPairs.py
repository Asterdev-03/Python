arr = [1, 2, 3, 4, 5]

while len(arr) != 1:
    x = []
    for j in range(len(arr)-1):
        x.append(arr[j] + arr[j+1])
        print(x)
    arr = x


print(arr)

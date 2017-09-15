def arr_min(arr):
    a = arr[0]
    for i in arr:
        if i < a:
            a = i
    return a


def arr_avg(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)

arr1 = [18, 24, 12, 6, 12, 36]

print(arr_min(arr1))
print(arr_avg(arr1))
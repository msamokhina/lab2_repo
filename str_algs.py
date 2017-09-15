def string_reverse(s):
    s1 = ""
    for x in s:
        s1 = x + s1
    return s1

print(string_reverse("hello, world"))

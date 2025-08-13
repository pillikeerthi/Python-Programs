def freq(s):
    temp = {}
    for char in s:
        if char != " ":
            if char in temp:
                temp[char] += 1
            else:
                temp[char] = 1
    return temp

string = input("Enter a String: ")
s = freq(string)
for char, count in s.items():
    print(char, ":", count)
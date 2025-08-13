def alphanum(s):
    temp = ""
    for char in s:
        if char.isalnum():
            if 'A' <= char <= 'Z':
                temp += chr(ord(char) + 32)
            else:
                temp += char
    return temp

string = input("Enter a string: ")
temp = alphanum(string)

revstr = ""
for char in temp:
    revstr = char + revstr
print(f'"{string}" is a palindrome' if temp==revstr else f'"{string}" is not a palindrome')
def remove_spaces(s):
    temp=""
    for char in s:
        if char != " ":
            temp += char
    print(temp)

string = input("Enter a String: ")
s= remove_spaces(string)
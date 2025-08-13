#count of vowels and consonants
def count(s):
    vowels = "aeiouAEIOU"
    vcount = ccount = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vcount += 1
            else:
                ccount += 1
    print(f"Vowels: {vcount}")
    print(f"Consonants: {ccount}")
    
string = input("Enter a string: ")
count(string)
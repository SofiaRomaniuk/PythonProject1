import string
letters = string.ascii_letters

a,b = input().split("-")

start = letters.index(a)
end = letters.index(b)

print(letters[start:end + 1])
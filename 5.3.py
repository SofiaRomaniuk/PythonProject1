import string

text = input()

for symbol in string.punctuation:
    text = text.replace(symbol,"")

words = text.split()
hashtag = "#" + "".join(word.capitalize() for word in words)
print(hashtag[:140])

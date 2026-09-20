def first_word(text):
    """ Пошук першого слова """

    text = text.replace(",", " ")
    text = text.replace(".", " ")

    words = text.split()
    return words[0]

print(("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))
print('OK')
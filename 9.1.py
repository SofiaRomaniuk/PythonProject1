def popular_words (text, words):
    result = {}

    text = text.lower()
    text_words = text.split()


    for word in words:
        lower = word.lower()
        result [lower] = text_words.count(lower)

    return result

text = '''When I was One I had just begun When I was Two I was nearly new '''

print(popular_words(text, ['one', 'two', 'three']))




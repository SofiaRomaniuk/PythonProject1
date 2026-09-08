
def second_index(text:str ,some_str:str):
    first_index = text.find(some_str)

    if first_index == -1:
        return None

    second_index = text.find(some_str, first_index + 1)
    if second_index == -1:
        return None

    return second_index

print(second_index("bob",'b'))
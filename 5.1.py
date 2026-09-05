import keyword
import string

name = input()

if (
    not name [0].isdigit()
    and not  any(char.isupper()for char in name)
    and not any (char in string.punctuation.replace("_","") for char in name)
    and " " not in name
    and "__" not in name
    and name not in keyword.kwlist
):
    print(True)
else:
    print(False)

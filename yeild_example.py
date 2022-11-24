import itertools
import string


# This file is an example of the yeild function, it creates the Excel pattern of column labels

def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(string.ascii_lowercase, repeat=size):
            yield "".join(s)


max_letter = 30

letters_excel = []
for s in iter_all_strings():
    letters_excel.append(s)
    if len(letters_excel) == max_letter + 1:
        break

print(letters_excel)

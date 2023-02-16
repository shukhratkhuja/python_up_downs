dct = {
    'e': [1],
    'l': [2, 3, 10],
    'H': [0],
    'W': [7],
    'o': [4, 8],
    ',': [5],
    ' ': [6],
    'd': [11],
    '!': [12],
    'r': [9]
}

ilist = []
for val in dct.values():
    ilist.extend(val)
    ilist = sorted(ilist)

hw = ''
for i in ilist:
    for key, value in dct.items():
        if i in value:
            hw += key
print(hw)

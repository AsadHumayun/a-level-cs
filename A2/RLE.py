# author: asadhumayun

text = str(input('Enter string to encode in RLE: '))
rle = []
lastChar = ''

for char in list(text):
    if char == lastChar:
        if rle[len(rle) - 1][0] == char:
            rle[len(rle) - 1] = [char, rle[len(rle) - 1][1] + 1]
            lastChar = char

    else:
        rle.append([char, 1])
        lastChar = char


print('\n'.join(map(lambda x: x[0] + ': ' + str(x[1]), rle)))

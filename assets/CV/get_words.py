all_words = []
with open('words.txt') as f:
    for line in f:
        for item in line.split(','):
            if item <> '\n' or item not in all_words:
                all_words.append(item)


with open('final.csv', 'w') as f:
    for item in all_words:
        f.write(item + ',')

f.close()

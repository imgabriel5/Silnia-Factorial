# Ile razy dany wyraz wystąpił w zdaniu.
text = ('jeden jeden jeden jeden dwa dwa trzy trzy trzy')
words = text.split(' ') # Tekst zmienić na listę. .strip() Strip to metoda pobierania treści z pliku.
stats = {}
# Poniższy kod jest dobry, ale można go zapisać krócej.
# for word in words:
#     if word not in stats:
#         stats[word] = 0
#
#     stats[word] += 1
for word in words:
    stats[word] = stats.get(word, 0) + 1
print(stats)

# list comprehension
values = [5, 15, 25, 17, 10]
values_pow = []
# Pierwszy sposób.
# for value in values:
#     values_pow.append(value ** 2)
# Drugi sposób.
values_pow = [value ** 2 for value in values]
print(values, values_pow)

#dict comprehension
text = ('jeden jeden jeden jeden dwa dwa trzy trzy trzy')
words = text.split(' ') # Tekst zmienić na listę. .strip() Strip to metoda pobierania treści z pliku.
stats = {}

for word in words:
    stats[word] = stats.get(word, 0) + 1

stats = {word: text.count(word) for word in text.split(' ')}
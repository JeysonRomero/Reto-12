from collections import Counter
import re

# Leer el archivo
with open('mbox.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Contar vocales
vowels = 'aeiou'
vowel_count = sum(text.lower().count(v) for v in vowels)

# Contar consonantes
consonants = 'bcdfghjklmnpqrstvwxyz'
consonant_count = sum(text.lower().count(c) for c in consonants)

# Contar palabras
words = re.findall(r'\b\w+\b', text.lower())
word_counts = Counter(words)
most_common_words = word_counts.most_common(50)

print(f'Cantidad de vocales: {vowel_count}')
print(f'Cantidad de consonantes: {consonant_count}')
print('Listado de las 50 palabras que más se repiten:')
for word, count in most_common_words:
    print(f'{word}: {count}')

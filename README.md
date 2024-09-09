# Reto-12


### Punto 1 / Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

endswith(sub[, start[, end]])

Descripción: Devuelve True si la cadena termina con el sufijo especificado. Puede opcionalmente limitar la búsqueda a una subcadena delimitada por start y end.

Ejemplo:
```py
text = "Hello, world!"
print(text.endswith("world!"))  # True
print(text.endswith("world", 0, 5))  # False
```

startswith(prefix[, start[, end]])

Descripción: Devuelve True si la cadena comienza con el prefijo especificado. Puede opcionalmente limitar la búsqueda a una subcadena delimitada por start y end.

Ejemplo:
```py
text = "Hello, world!"
print(text.startswith("Hello"))  # True
print(text.startswith("world", 7))  # True
```

isalpha()

Descripción: Devuelve True si todos los caracteres en la cadena son letras y hay al menos un carácter.

Ejemplo:
```py
text = "Hello"
print(text.isalpha())  # True
text = "Hello1"
print(text.isalpha())  # False
```

isalnum()

Descripción: Devuelve True si todos los caracteres en la cadena son alfanuméricos y hay al menos un carácter.

Ejemplo:
```py
text = "Hello123"
print(text.isalnum())  # True
text = "Hello 123"
print(text.isalnum())  # False
```

isdigit()

Descripción: Devuelve True si todos los caracteres en la cadena son dígitos y hay al menos un carácter.

Ejemplo:
```py
text = "12345"
print(text.isdigit())  # True
text = "123a45"
print(text.isdigit())  # False
```

isspace()

Descripción: Devuelve True si todos los caracteres en la cadena son espacios en blanco y hay al menos un carácter.

Ejemplo:
```py
text = "    "
print(text.isspace())  # True
text = "  a "
print(text.isspace())  # False
```

istitle()

Descripción: Devuelve True si la cadena está en formato de título (cada palabra comienza con una letra mayúscula y el resto de las letras son minúsculas).

Ejemplo:
```py
text = "Hello World"
print(text.istitle())  # True
text = "Hello world"
print(text.istitle())  # False
```

islower()

Descripción: Devuelve True si todos los caracteres en la cadena son minúsculas y hay al menos un carácter.

Ejemplo:
```py
text = "hello"
print(text.islower())  # True
text = "Hello"
print(text.islower())  # False
```

isupper()

Descripción: Devuelve True si todos los caracteres en la cadena son mayúsculas y hay al menos un carácter.

Ejemplo:
```py
text = "HELLO"
print(text.isupper())  # True
text = "Hello"
print(text.isupper())  # False
```

### Punto 2 / Procesar el archivo y extraer:

```py
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
```

- Cantidad de vocales
- Cantidad de consonantes
- Listado de las 50 palabras que más se repiten

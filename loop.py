programming_language = ['Rust', 'Java', 'Python', 'C++']
for language in programming_language:
    print(language)

for char in 'code':
    print(char)

categories = ['Fruits', 'vegetable']
foods = ['Apple', 'Banana', 'carrot']

for category in categories:
    for food in foods:
        print(category, food)

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input("Guess the numbers(1-5): "))
    if guess != secret_number:
        print('Wrong! Try again')

print('You got it!')

developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)

developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' conatins the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")

    
for num in range(3):
    print(num)

for num in range(1, 5):
    print(num)

# range(start, stop, step)
for num in range(2, 11, 2):
    print(num)

for num in range(40, 0, -10):
    print(num)

numbers = list(range(2, 11, 2))
print(numbers)

languages = ['Spanish', 'English', 'Russian', 'Chinese']
index = 0
for language in languages:
    print(f'Index {index} and language {language}')
    index += 1


list(enumerate(languages))
[(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')


developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]
list(zip(developers, ids))
[('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')

even_numbers = []
for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words)
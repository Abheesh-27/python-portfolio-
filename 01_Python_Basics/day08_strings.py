print('\n ===== Program 1: Convert to Uppercase =====')
text1 = input('Enter a string: ')

#converting all letters to uppercase
print('Uppercase String: ',text1.upper())


print('\n ===== Program 2: Convert to Lowercase =====')
text2 = input('Enter a string: ')

#converting all letters to lowercase
print('Lowercase String: ', text2.lower())


print('\n ===== Program 3: Replacing a Word =====')

sentence = input('Enter a sentence: ')
old_word = input('\n Enter word to replace: ')
new_word = input('Enter new word: ')

#replacing a word 
new_sentence = sentence.replace(old_word, new_word)
print('\n New Sentence: ', new_sentence)


print('\n ===== Program 4: Find a Character =====')
string = input('Enter a string: ')

search = input('Enter a character or word to find: ')
position = string.find(search)
print()

#find() doesn't give an error but instead it returns -1
if position != -1: 
    print(search, 'found at index', position)
else:
    print(search, ' not found!')


print('\n ===== Program 5: Counting Occurrences =====')
string1 = input('Enter a string: ')

character = input('Enter character or word to count: ')
print()
print(character, 'appears', string1.count(character), 'times.')


print('\n ===== Program 6: Split Sentence =====')
sentence1 = input('Enter a sentence: ')
words = sentence1.split()
print()

#split() converts the string into a list
print('Words in the sentence are: ',words)
print('Total Words: ',len(words))


print('\n ===== Program 7: Join a List into string ===== ')

name = ["Abheesh", 'is', 'a', 'student', 'at', 'IIT', 'Madras.']
print(name)
print()
after_joining = ' '.join(name)

print('After converting into string: ',after_joining)
print()


print('\n ===== Program 8: Email Validator =====')
email = input('Enter email: ')
print()

if '@' in email and '.' in email.split('@')[-1]:
    print('Valid Email.')
else:
    print('Invalid Email!')


print('\n ===== Program 9: Count Vowels =====')
text3 = input('Enter a string: ').lower()

count = 0
for i in text3:
    if i in 'aeiou':
        count += 1
print('Number of Vowels: ', count)


print('\n ===== Program 10: Palindrome Check =====')
text4 = input('Enter a string: ').lower()

if text4 == text4[::-1]:
    print('Given string is a Palindrome.')
else:
    print('Given string is not a Palindrome!')


print('\n ===== Program 11: Reverse Every Word =====')
unreversed_sentence = input('Enter a String: ')
sent = unreversed_sentence.split()
reversed_sentence = []

for word in sent:
    reversed_sentence.append(word[::-1])

new_string = ' '.join(reversed_sentence)
print('After reversing: ', new_string)


print("\n ===== Program 12: Word Frequency Counter =====")

sentence2 = input("Enter a sentence: ").lower()

words_in = sentence2.split()

frequency = {}

for word in words_in:
    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

print("\nWord Frequencies:- ")

for word in sorted(frequency):
    print(word, ":", frequency[word])

print()


print('\n ===== Program 13: Character Frequency Counter =====')

word_a = input('Enter a string: ')
char = {}

for i in word_a:
    if i in char:
        char[i] += 1
    else:
        char[i] = 1
print('\n Character Frequencies: ')

for i in sorted(char):
    print(i,':', char[i])

print()
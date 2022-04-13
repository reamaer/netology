words_array = ['developer', 'settings', 'contributions', 'profile', 'organizations']
letter = "r"


def count_letter(array, letter):
    count = 0
    for word in array:
        print(word)
        char = letter
        if char in word:
            count += 1
    print(f'The number of words with the \"{letter}\" in the list {array} - {count}')


count_letter(words_array, letter)
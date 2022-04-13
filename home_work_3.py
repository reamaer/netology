words_array = ['developer', 'settings', 'contributions', 'profile', 'organizations']


def count_letter(list, letter):
    count = 0
    for word in list:
        if letter in word:
            count += 1
    print(f'The number of words with the \"{letter}\" in the list {list} - {count}')


count_letter(words_array, 'c')

words_array = ['developer', 'settings', 'contributions', 'profile', 'organizations']
letter = 'o'


def count_letter(array):
    for word in array:
        count = 0
        for i in word:
            if i == letter:
                count += 1
        print(count)


count_letter(words_array)

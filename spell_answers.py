def get_words():
    words = []
    with open('words.txt') as f:
        words = f.readlines()
    return words

def get_letters():
    letters = []
    print(' ')
    print('Enter all letters here, leaving the center letter last.')
    print(' ')
    for i in range(7):
        l = input('Letter: ')
        if i == 6:
            center_letter = l
        else:
            letters.append(l)
    return letters, center_letter

def word_checker(words, letters, center_letter):
    banned_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    good_words = []
    for letter in letters:
        banned_letters.remove(letter)
    banned_letters.remove(center_letter)
    for word_num, word in enumerate(words):
        bad_word = False
        if len(word) > 4:
            if center_letter in word:
                for banned_letter in banned_letters:
                    if banned_letter in word:
                        bad_word = True
                if not bad_word:
                    good_words.append(word)
    print(' ')
    print('Possible words: ')
    print(' ')
    for word in good_words:
        print(word)

words = get_words()
letters, center_letter = get_letters()
word_checker(words, letters, center_letter)


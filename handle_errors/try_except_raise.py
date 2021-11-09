def is_palindrome(word):
    return word == word[::-1]


def main():
    try:
        word = input('Enter a word: ')
        if len(word) == 0:
            raise ValueError('Word is empty')
        if is_palindrome(word):
            print('{} is a palindrome'.format(word))
        else:
            print('{} is not a palindrome'.format(word))
    except ValueError as err:
        print('Please enter a word: {}'.format(err))

if __name__ == '__main__':
    main()

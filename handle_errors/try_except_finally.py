def is_palindrome(word):
    return word == word[::-1]


def main():
    try:
        word = input('Enter a word: ')
        if is_palindrome(word):
            print('{} is a palindrome'.format(word))
        else:
            print('{} is not a palindrome'.format(word))
    except:
        print('Please enter a word')
    else:
        print('No exceptions occurred')
    finally:
        print('Done')

if __name__ == '__main__':
    main()

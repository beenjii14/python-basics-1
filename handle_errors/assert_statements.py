def is_palindrome(word):
    # assert word != "", "Word cannot be empty"
    assert len(word) > 0, "Word cannot be empty"
    return word == word[::-1]


def main():
    # example 1
    try:
        print(is_palindrome(""))
    except AssertionError as e:
        print(e)

    # example 2
    try:
        num = input("Enter a number: ")
        assert num.isnumeric(), "Invalid number"
        print(num)
    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    main()

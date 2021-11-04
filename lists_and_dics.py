def main():
    # numbers divisibles by 3 (list)
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)

    # numbers divisibles by 3 (dictionary)
    squares_dict = { i: i**3 for i in range(1,101) if i % 3 != 0 }
    print(squares_dict)

if __name__ == '__main__':
    main()

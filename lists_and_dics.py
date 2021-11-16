def main():
    # numbers divisibles by 3 (list)
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)

    # numbers divisibles by 3 (dictionary)
    squares_dict = { i: i**3 for i in range(1,101) if i % 3 != 0 }
    print(squares_dict)

    # concat two dictionaries
    dic1 = {1:"hola", 2:"adios", 3:"hasta luego"}
    dic2 = {4:"¿Cómo estás?", 5:"¿Te encuentras bien?"}
    result_concat = {**dic1, **dic2} # option one
    print(result_concat)
    # create new dictionary with values of dic1 and dic2
    result_concat = dic1 | dic2 # option two
    print(result_concat)

if __name__ == '__main__':
    main()

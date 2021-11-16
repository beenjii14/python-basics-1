import os


PATH=os.path.dirname(__file__)


def write():
    names = ["John", "Bob", "Alice", "Benjamín"]
    with open(f"{PATH}/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(f"{name}\n")


def read():
    numbers = []
    with open(f"{PATH}/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))

    print(numbers)



def main():
    write()


if __name__ == '__main__':
    main()

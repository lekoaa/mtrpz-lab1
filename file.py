from equation import equation
from re import search


def main(file_name):
    text = validator(file_name)

    if text:
        a, b, c = map(float, text.split())

        if a != 0:
            equation(a, b, c)
        else:
            print("a can't equal 0")
            main(file_name)


def validator(file_name):
    pattern = r'^(-?\d+(\.\d+)?\s){2}-?\d+(\.\d+)?\n$'
    
    try:
        with open(file_name, 'r') as file:
            line = file.read()
    except FileNotFoundError:
        print(f'File {file_name} does not exist')
        return None

    matching = search(pattern, line)
    if matching:
        return matching.group()[:-1]
    else:
        print('Invalid file format')
        return None

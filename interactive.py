from equation import equation

def entry(coefficient):
    try:
        answer = input(f'{coefficient} = ')
        number = float(answer)
        return number
    except:
        print(f'Error. Expected a valid real number, got {answer} instead')
        return entry(coefficient)
    
def main():
    a, b, c = entry('a'), entry('b'), entry('c')
    if a != 0:
        return equation(a, b, c)
    else:
        print("a can't equals 0")
        return main()
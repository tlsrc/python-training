def say_hello(name):
    print("Hello " + name)

def power(x, y):
    return x ** y


def fib(x):
    if x == 0: return 0
    if x == 1: return 1
    return fib(x - 1) + fib(x - 2)


area_codes = {[418,581]:'Québec',
                'Montréal': [438, 514],
                'Banlieue': [450]}

def get_area_codes(region):
    if region in area_codes :
        return area_codes[region]
    return 'Unknown region'

def get_region(area_code):
    for k,v in area_codes.items():
        if area_code in v: return(k)
    return 'Unknown area code'

def words_average_size(text):
    size_sum = 0
    words = text.split()
    for word in words :
        size_sum += len(word)
    return size_sum / len(words)

def divide(x,y):
    try:
        return (x / y)
    except ZeroDivisionError:
        print('! Division par zéro !')
        return float("inf")

def fizz_buzz():
    result = []
    for x in range(0, 101):
        if (x % 15 == 0):
            result.append("FizzBuzz")
        elif(x % 3 == 0) :
            result.append("Fizz")
        elif(x % 5 == 0):
            result.append("Buzz")
        else:
            result.append(x)
    return result

def mine_sweeper(size, content):
    
    # Build grid
    grid = {}
    lines, columns = size
    index = 0
    for x in range(0, lines):
        for y in range(0, columns):
            grid[(x,y)] = content[index]
            index += 1

    # Compute neighbors
    for coordinates in grid:
        if(grid[coordinates] == "*"): continue
        x, y = coordinates
        neighbors = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
                     (x - 1, y),                 (x + 1, y),
                     (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
        number_of_adjacent_mines = 0
        for neighbor in neighbors:
            if (neighbor in grid) and (grid[neighbor] == "*"):
                number_of_adjacent_mines += 1
        grid[coordinates] = number_of_adjacent_mines

    #Build display
    display = ""
    for x in range(0, lines):
        for y in range(0, columns):
            display += str(grid[(x,y)])
        display += "\n"
    return display


if __name__ == "__main__":
    say_hello("guys")
    print(power(2, 3))
    print(get_area_codes('Montréal'))
    print(get_area_codes('New York'))
    print(get_region(438))
    print(get_region(123))
    print(words_average_size("ha ha"))
    print(words_average_size("hi hello"))
    print(divide(1,2))
    print(divide(1,0))
    print(fizz_buzz())
    print(mine_sweeper((3,3), "*.......*"))


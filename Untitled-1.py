def findOdd(min:int, max:int) -> int:
    for i in range(min, max + 1):
        if i % 2 != 0:
            yield i
    return -1
a,b = map(int, input().split())
if a > b:
    a, b = b, a

for i in findOdd(a, b):
    print(i, end=' ')

def findFalseelement(arr:list,a:int,b:int) -> int:
    for i in arr:
        if i < a or i > b:
            yield i
    return -1
arr = list(map(int, input().split()))
a, b = map(int, input().split())
if a > b:
    a, b = b, a
for i in findFalseelement(arr, a, b):
    print(i, end=' ')

def show_line(symbol:str, func:callable[[str],None]) -> None:
    func(symbol)
def print_vline(symbol:str) -> None:
    for i in range(5):
        print(symbol)
def print_hline(symbol:str) -> None:
    for i in range(5):
        print(symbol, end=' ')
symbol = input()
show_line(symbol, print_vline)
show_line(symbol, print_hline)
show_line('-', lambda x: [print(x, end=' ') for i in range(10)])
show_line('|', lambda x: [print(x,end='\n') for i in range(10)])


def timer(func:callable) -> callable:
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        for i in func(*args, **kwargs):
            print(i, end=' ')
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        
    return wrapper
@timer
def countdown() -> int:
    for i in range(0, 100):
        if i %2 == 0:
            yield i
countdown()

@timer
def countdown2(a:int,b:int) -> int:
    for i in range(a, b + 1):
        if i %2 == 0:
            yield i
a, b = map(int, input().split())
if a > b:
    a, b = b, a
countdown2(a, b)
        
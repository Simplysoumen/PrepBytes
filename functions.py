def addition():
    a,b = map(int, input().split())
    print(a+b)

def swap(a,b):
    temp = a
    a = b
    b = temp
    print(a,b)
def main():
    # addition()
    # addition()
    # addition()
    a,b = map(int, input().split())
    swap(a,b)
    print(a,b)

if __name__ == '__main__':
    main()

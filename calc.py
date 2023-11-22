run = 1
while run != 0:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print("1.add\n2.subtract\n3.multiply\n4.divide")
    c = int(input("enter a option: "))
    if c == 1:
        print(f"{a} + {b} = {a+b}")
    elif c == 2:
        print(f"{a} - {b} = {a-b}")
    elif c == 3:
        print(f"{a} * {b} = {a*b}")
    elif c == 4:
        print(f"{a} // {b} = {a//b}")
    else:
        print("invalid operation")
    run = int(input('enter 1 to continue or 0 to exit: '))
    
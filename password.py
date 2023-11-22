import random

run = 1

while run == 1:
    password = ""
    length = int(input("Enter the length of your password: "))
    for i in range(length):
        num = random.randint(1,4)
        if num == 1:
            lim = "abcdefghijklmnopqrstuvwxyz"
            chose = random.randint(0,25)
            let = lim[chose]
            password = password + let

        elif num == 2:
            lim = "0123456789"
            chose = random.randint(0,9)
            let = lim[chose]
            password = password + let

        elif num == 3:
            lim = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            chose = random.randint(0,25)
            let = lim[chose]
            password = password + let

        elif num == 4:
            lim = "@#$_"
            chose = random.randint(0,3)
            let = lim[chose]
            password = password + let
    print(f"Your Password is {password}")

    run = int(input("Enter 1 to Make another password and 0 to exit: "))
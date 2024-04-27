import sys

X = 1080
Y = 1920
screen_X = 405
screen_Y = 720

if len(sys.argv) < 3:
    print("Insufficient arguments provided.")
else:
    try:
        par1 = int(sys.argv[1])
        par2 = int(sys.argv[2])
        print("par1:", par1)
        print("par2:", par2)
        # Rest of your code using par1 and par2
        x = int(X * par1 / screen_X)
        y = int(Y * par2 / screen_Y)
        print("x, y :", x, y)
    except ValueError:
        print("Invalid argument type. Both parameters should be integers.")

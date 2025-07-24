rows = int(input("Enter the number of rows: "))
border = int(input("Enter the border size: "))
center = border // 2

for a in range(border + 1):
    for b in range(border + 1):

        # Border of 0s with center 0
        if a == 0 or a == border or b == 0 or b == border or (a == center and b == center):
            print("0 ", end=" ")

        # Top-left wing
        elif a<=rows and a <= b <= rows:
            num = border // 2 - a - (b - a)
            if num > 0:
                print(f"{num} ", end=" ")
            else:
                print("  ", end=" ")

        # Top-right wing
        elif a<=rows and border - a <= b:
            num = a - (b - (border - a))
            if num > 0:
                print(f"{num} ", end=" ")
            else:
                print("  ", end=" ")

        # Bottom-left wing
        elif border - rows <= a and border - a >= b:
            num = (a - rows) // (border - rows) + b
            if num > 0:
                print(f"{num} ", end=" ")
            else:
                print("  ", end=" ")

        # Bottom-right wing
        elif border - rows <= a and border - rows <= b and b - (border - rows) + 1 <= a - (border - rows) + 1:
            num = b - border // 2
            if num > 0:
                print(f"{num} ", end=" ")
            else:
                print("  ", end=" ")

        else:
            print("  ", end=" ")
    print()
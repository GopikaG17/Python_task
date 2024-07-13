def print_hexagon_pattern(rows, columns):
    for r in range(rows):
        # Top line of hexagons
        for c in range(columns):
            if (c + 1) % 2 != 0:
                print("  ___  ", end="")
            else:
                print("       ", end="")
        print()

        # Upper left and right lines of hexagons
        for c in range(columns):
             if (c + 1) % 2 != 0:
                 print(" /   \ ", end="")
             else:
                print("       ", end="")
        print()

        # Middle line of hexagons with "---" for even columns
        for c in range(columns):
            if (c + 1) % 2 == 0:
                print("   ---   ", end="")
            else:
                print("     ", end="")
        print()

        # Lower left and right lines of hexagons
        for c in range(columns):
            if (c + 1) % 2 != 0:
                print(" \   / ", end="")
            else:
                print("       ", end="")
        print()

    # Bottom line of hexagons
    for c in range(columns):
        if (c + 1) % 2 == 0:
            print("       ", end="")
        else:
            print("  ___  ", end="")
    print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
print_hexagon_pattern(rows, columns)

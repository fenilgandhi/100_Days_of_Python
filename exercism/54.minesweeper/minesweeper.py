def board(input_board_array):
    # Handle null value
    if input_board_array in [[], [""]]:
        return input_board_array

    def set_value(i, j):
        points = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                  (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
        for point in points:
            elem = input_board_array[point[1]][point[0]]
            if (elem == "*") or (elem == "-"):
                continue
            if elem == " ":
                input_board_array[point[1]][point[0]] = 1
            else:
                input_board_array[point[1]][point[0]] += 1

    # Find dimensions of board, Checking input & add padding values then update dimensions
    x, y = len(input_board_array[0]), len(input_board_array)
    for j in range(y):
        if len(input_board_array[j]) != x:
            raise ValueError("Missing Values")
        input_board_array[j] = ["-", *input_board_array[j], "-"]
    x, y = x + 2, y + 2
    input_board_array = [['-'] * x, *input_board_array, ['-'] * x]

    # Loop through each element and add their count
    for j in range(1, y - 1):
        for i in range(1, x - 1):
            try:
                element = input_board_array[j][i]
                if element == '*':
                    set_value(i, j)
                elif (element in ['-', ' ']) or element.__class__ == int:
                    continue
                else:
                    raise IndexError
            except IndexError:
                raise ValueError("Incomplete board")
    return [''.join(map(str, row[1:-1])) for row in input_board_array[1:-1]]

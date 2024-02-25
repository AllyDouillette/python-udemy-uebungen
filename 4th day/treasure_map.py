location = input().upper()

line1 = [ " ", " ", " " ]
line2 = [ " ", " ", " " ]
line3 = [ " ", " ", " " ]

map = [ line1, line2, line3 ]

column = ord(location[0]) - ord("A")
row = int(location[1]) - 1

map[row][column] = "X"

print(f"{line1}\n{line2}\n{line3}")

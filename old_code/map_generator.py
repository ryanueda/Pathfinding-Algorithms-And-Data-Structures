import random

def generate_map():
    map = []
    for i in range(8):
        row = []
        for j in range(12):
            if i == 0 or i == 7 or j == 0 or j == 11:
                row.append('X')
            else:
                rr = random.randint(0, 2)
                if rr == 0:
                    row.append('X')
                else:
                   row.append('.')
        map.append(row)
    s_row = random.randint(1, 6)
    s_col = random.randint(1, 10)
    map[s_row][s_col] = 's'
    e_row = random.randint(1, 6)
    e_col = random.randint(1, 10)
    while (s_row == e_row and s_col == e_col):
        e_row = random.randint(1, 6)
        e_col = random.randint(1, 10)
    map[e_row][e_col] = 'e'
    return map

for i in range(3): # generate 3 maps
    map = generate_map()
    for row in map:
        print(''.join(row))
    print()

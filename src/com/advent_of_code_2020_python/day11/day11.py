seats = [line.rstrip() for line in open("Day_11_2020.txt", "r")]


# Rules:
# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.


def get_adjacent_empty(seats, row, seat):
    empty = 0
    taken = 0
    for i in range(row - 1, row + 2):
        if i < 0 or i >= len(seats):
            empty += 3
        else:
            for j in range(seat - 1, seat + 2):
                if j < 0 or j >= len(seats[i]):
                    empty += 1
                elif row == i and seat == j:
                    pass
                elif seats[i][j] == "L" or seats[i][j] == ".":
                    empty += 1
                elif seats[i][j] == "#":
                    taken += 1
    return empty, taken


def seat_occupancy(seats):
    new_seats = []
    for row in range(0, len(seats)):
        new_row = ""
        for seat in range(0, len(seats[row])):
            if seats[row][seat] == ".":
                new_row += seats[row][seat]
            elif seats[row][seat] == "L":
                if get_adjacent_empty(seats, row, seat)[0] == 8:
                    seat = "#"
                    new_row += seat
                else:
                    new_row += "L"
            elif seats[row][seat] == "#":
                if get_adjacent_empty(seats, row, seat)[1] >= 4:
                    seat = "L"
                    new_row += seat
                else:
                    new_row += "#"
        new_seats.append(new_row)
    return new_seats


new_seats = seat_occupancy(seats)
while seats != new_seats:
    seats = new_seats
    new_seats = seat_occupancy(seats)

count_occupied = 0
for row in seats:
    count_occupied += row.count("#")
print(count_occupied)


def count_occupied2(r, c, grid):
    count = 0
    for i, j in deltas:
        xi, xj = r + i, c + j
        while 0 <= xi < rows and 0 <= xj < cols:
            if grid[xi][xj] == '#':
                count += 1
                break
            elif grid[xi][xj] == 'L':
                break
            xi += i
            xj += j
    return count


def check_occupied2(lines, thresh=5):
    while True:
        valid = True
        temp_grid = [r.copy() for r in lines]
        for i, r in enumerate(temp_grid):
            for j, c in enumerate(r):
                count = count_occupied2(i, j, temp_grid)
                if c == 'L' and count == 0:
                    lines[i][j] = '#'
                elif c == '#' and count >= thresh:
                    lines[i][j] = 'L'
                valid &= (r[j] == lines[i][j])
        if valid:
            break
    ans = 0
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == '#':
                ans += 1
    print(f"There are {ans} valid seats.")


seats = [list(line.rstrip()) for line in open("Day_11_2020.txt", "r")]

rows, cols = len(seats), len(seats[0])
deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

check_occupied2(seats)

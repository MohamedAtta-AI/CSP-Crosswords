from random import choice, randint
from string import ascii_uppercase
from termcolor import colored
# Team leader: Asmaa El-Maghraby


def generate_grid(r, c):
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]


def overlap(insertion_type, used_locs, insertion_loc, w_length):
    # Overlapping words test function
    for i in range(w_length):
        if insertion_type == "Horizontal":
            if (insertion_loc[0], insertion_loc[1] + i) in used_locs:
                return True

        elif insertion_type == "Vertical":
            if (insertion_loc[0] + i, insertion_loc[1]) in used_locs:
                return True

        elif insertion_type == "+ve diagonal":
            if (insertion_loc[0] - i, insertion_loc[1] + i) in used_locs:
                return True

        elif insertion_type == "-ve diagonal":
            if (insertion_loc[0] + i, insertion_loc[1] + i) in used_locs:
                return True

    return False


# Insert words into random locations of the puzzle (horizontally, diagonally, or vertically)
def insert_words(puzzle, words):
    used_locs = set()  # Stores used locations to prevent overlap
    for word in words:
        w_length = len(word)
        insertion_type = randint(0, 3)  # 0,1,2,3 = horizontal, vertical, +ve diagonal, -ve diagonal
        is_reversed = randint(0, 1)  # Determine whether to insert word in reverse
        if is_reversed:
            word = word[::-1]

        if insertion_type == 0:  # Horizontal
            insertion_loc = (randint(0, rows - 1), randint(0, columns - w_length))  # Pick random location for the word
            # Keep looking for new location if overlap will occur
            while overlap("Horizontal", used_locs, insertion_loc, w_length):
                insertion_loc = (randint(0, rows - 1), randint(0, columns - w_length))
            for i in range(w_length):  # Insert word into puzzle and append the used locations
                puzzle[insertion_loc[0]][insertion_loc[1] + i] = word[i]
                used_locs.add((insertion_loc[0], insertion_loc[1] + i))

        elif insertion_type == 1:  # Vertical
            insertion_loc = (randint(0, rows - w_length), randint(0, columns - 1))
            while overlap("Vertical", used_locs, insertion_loc, w_length):
                insertion_loc = (randint(0, rows - w_length), randint(0, columns - 1))
            for i in range(w_length):
                puzzle[insertion_loc[0] + i][insertion_loc[1]] = word[i]
                used_locs.add((insertion_loc[0] + i, insertion_loc[1]))

        elif insertion_type == 2:  # +ve diagonal
            insertion_loc = (randint(w_length - 1, rows - 1), randint(0, columns - w_length))
            while overlap("+ve diagonal", used_locs, insertion_loc, w_length):
                insertion_loc = (randint(w_length - 1, rows - 1), randint(0, columns - w_length))
            for i in range(w_length):
                puzzle[insertion_loc[0] - i][insertion_loc[1] + i] = word[i]
                used_locs.add((insertion_loc[0] - i, insertion_loc[1] + i))

        else:  # -ve diagonal
            insertion_loc = (randint(0, rows - w_length), randint(0, columns - w_length))
            while overlap("-ve diagonal", used_locs, insertion_loc, w_length):
                insertion_loc = (randint(0, rows - w_length), randint(0, columns - w_length))
            for i in range(w_length):
                puzzle[insertion_loc[0] + i][insertion_loc[1] + i] = word[i]
                used_locs.add((insertion_loc[0] + i, insertion_loc[1] + i))


def solve(puzzle, words):
    found = 0
    look_len = 0
    while found < len(words):
        if ''.join([puzzle[i][i] for i in range(look_len)]).find(words[found]) or \
            ''.join([puzzle[i][len(puzzle)-i-1] for i in range(look_len)]).find(words[found]) or \
                ''.join([row for row in puzzle]).find(words[found]) or \
                ''.join([row[i] for i, row in enumerate(puzzle)]):
            print(words[found])
            found += 1

        look_len += 1


def display(puzzle):
    for row in puzzle:
        for ch in row:
            print(colored(f"{ch}", "blue"), end="  ")
        print()


rows, columns = 6, 6
Grid = generate_grid(rows, columns)
Words = ['WALK', 'PLAY', 'CRY', 'ACT']
insert_words(Grid, Words)
display(Grid)
solve(Grid, Words)
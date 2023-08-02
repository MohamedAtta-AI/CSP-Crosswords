from random import choice, randint
from string import ascii_uppercase
from termcolor import colored
# Team leader: Asmaa El-Maghraby


def generate_grid(r, c):
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]


def backtracking_search(assignments):
    """Keeps looking for a random combination of word insertions that satisfy the constraint"""
    used_locs = set()  # Stores used locations to prevent overlap
    solution = {}
    for (word, assignment) in assignments.items():
        w_length = len(word)
        insertion_type = randint(0, 3)  # 0,1,2,3 = horizontal, vertical, +ve diagonal, -ve diagonal
        # Pick random insertion location
        insertion_loc = assignment[insertion_type][randint(0, len(assignment[insertion_type]) - 1)]
        # Keep looking for an insertion location till constraint is satisfied
        while not constraint_satisfied(insertion_type, used_locs, insertion_loc, w_length):
            insertion_loc = assignment[insertion_type][randint(0, len(assignment[insertion_type]) - 1)]

        for i in range(w_length):  # Insert word into puzzle and append the used locations
            if insertion_type == 0:
                Grid[insertion_loc[0]][insertion_loc[1] + i] = word[i]
                used_locs.add((insertion_loc[0], insertion_loc[1] + i))
            elif insertion_type == 1:
                Grid[insertion_loc[0] + i][insertion_loc[1]] = word[i]
                used_locs.add((insertion_loc[0] + i, insertion_loc[1]))
            elif insertion_type == 2:
                Grid[insertion_loc[0] - i][insertion_loc[1] + i] = word[i]
                used_locs.add((insertion_loc[0] - i, insertion_loc[1] + i))
            else:
                Grid[insertion_loc[0] + i][insertion_loc[1] + i] = word[i]
                used_locs.add((insertion_loc[0] + i, insertion_loc[1] + i))
        solution[word] = (insertion_type, insertion_loc)

    return (solution, used_locs)


def constraint_satisfied(insertion_type, used_locs, insertion_loc, w_length):
    # Overlapping words test function
    for i in range(w_length):
        if insertion_type == 0:
            if (insertion_loc[0], insertion_loc[1] + i) in used_locs:
                return False

        elif insertion_type == 1:
            if (insertion_loc[0] + i, insertion_loc[1]) in used_locs:
                return False

        elif insertion_type == 2:
            if (insertion_loc[0] - i, insertion_loc[1] + i) in used_locs:
                return False

        elif insertion_type == 3:
            if (insertion_loc[0] + i, insertion_loc[1] + i) in used_locs:
                return False

    return True


def generate_domain(words):
    domain = {}
    for word in words:
        w_length = len(word)
        is_reversed = randint(0, 1)  # Determine whether to insert word in reverse
        if is_reversed:
            word = word[::-1]

        locs_horizontal = [(x, y) for x in range(rows) for y in range(columns - w_length + 1)]
        locs_vertical = [(x, y) for x in range(rows - w_length + 1) for y in range(columns)]
        locs_pos = [(x, y) for x in range(w_length - 1, rows) for y in range(columns - w_length + 1)]
        locs_neg = [(x, y) for x in range(rows - w_length + 1) for y in range(columns - w_length + 1)]

        domain[word] = [locs_horizontal, locs_vertical, locs_pos, locs_neg]
    return domain


def display(solution):
    for ri, row in enumerate(Grid):
        for chi, ch in enumerate(row):
            if (ri, chi) in solution:
                print(colored(f"{ch}", "red"), end="  ")
            else:
                print(colored(f"{ch}", "blue"), end="  ")
        print()


rows, columns = 15, 15
Grid = generate_grid(rows, columns)
Words = ['WALK', 'PLAY', 'CRY', 'ACT', 'FLY', 'OPPOSE', 'CHARACTERISTIC', 'DOMAIN', 'RANGE']
Domain = generate_domain(Words)
Solution, used_locations = backtracking_search(Domain)
print(Solution)
display(used_locations)
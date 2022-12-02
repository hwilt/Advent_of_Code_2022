

def read_input(isExample=False):
    if isExample:
        return open("example.txt", "r").readlines()
    else:
        return open("input.txt", "r").readlines()


# OPPOENT
# A = ROCK, B = PAPER, C = SCISSORS
# PLAYER
# X = ROCK, Y = PAPER, Z = SCISSORS
# POINTS
# 0 = LOSE, 6 = WIN, 3 = TIE, 1 = Rock, 2 = Paper, 3 = Scissors
def rockPaperScissors(oppoent, player):
    result = 0
    if(oppoent == 'A') and (player == 'X'):
        result = 4 # TIE (3) + ROCK (1)
    elif(oppoent == 'A') and (player == 'Y'):
        result = 8 # WIN (6) + PAPER (2)
    elif(oppoent == 'A') and (player == 'Z'):
        result = 3 # LOSE (0) + SCISSORS (3)
    elif(oppoent == 'B') and (player == 'X'):
        result = 1 # LOSE (0) + ROCK (1)
    elif(oppoent == 'B') and (player == 'Y'):
        result = 5 # TIE (3) + PAPER (2)
    elif(oppoent == 'B') and (player == 'Z'):
        result = 9 # WIN (6) + SCISSORS (3)
    elif(oppoent == 'C') and (player == 'X'):
        result = 7 # WIN (6) + ROCK (1)
    elif(oppoent == 'C') and (player == 'Y'):
        result = 2 # LOSE (0) + PAPER (2)
    elif(oppoent == 'C') and (player == 'Z'):
        result = 6 # TIE (3) + SCISSORS (3)
    return result


def part1():
    inputs = read_input()
    sum_points = 0
    for game in inputs:
        oppoent, player = game.strip().split(" ")
        
        #print(oppoent)
        #print(player)
        sum_points += rockPaperScissors(oppoent, player)
    print(f"Day 1: {sum_points}")


def part2():
    inputs = read_input()
    sum_points = 0
    for game in inputs:
        oppoent, end_game = game.strip().split(" ")
        # X = LOSE, Y = TIE, Z = WIN for end_game
        # A = ROCK, B = PAPER, C = SCISSORS for oppoent
        # X = ROCK, Y = PAPER, Z = SCISSORS for player
        if end_game == 'X' and oppoent == 'A':
            player = 'Z'
        elif end_game == 'X' and oppoent == 'B':
            player = 'X'
        elif end_game == 'X' and oppoent == 'C':
            player = 'Y'
        elif end_game == 'Y' and oppoent == 'A':
            player = 'X'
        elif end_game == 'Y' and oppoent == 'B':
            player = 'Y'
        elif end_game == 'Y' and oppoent == 'C':
            player = 'Z'
        elif end_game == 'Z' and oppoent == 'A':
            player = 'Y'
        elif end_game == 'Z' and oppoent == 'B':
            player = 'Z'
        elif end_game == 'Z' and oppoent == 'C':
            player = 'X'
        
        #print(oppoent)
        #print(player)
        sum_points += rockPaperScissors(oppoent, player)
    print(f"Day 2: {sum_points}")

if __name__ == "__main__":
    part1()
    part2()
    #print(read_input())
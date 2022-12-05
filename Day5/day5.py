import re
from copy import deepcopy

stack1 = ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V']
stack2 = ['S', 'R', 'L', 'M', 'J', 'D', 'Q']
stack3 = ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B']
stack4 = ['R', 'S', 'C', 'L']
stack5 = ['M', 'V', 'T', 'P', 'F', 'B']
stack6 = ['T', 'R', 'Q', 'N', 'C']
stack7 = ['G', 'V', 'R']
stack8 = ['C', 'Z', 'S', 'P', 'D', 'L', 'R']
stack9 = ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']

stack1.reverse()
stack2.reverse()
stack3.reverse()
stack4.reverse()
stack5.reverse()
stack6.reverse()
stack7.reverse()
stack8.reverse()
stack9.reverse()

def readinput(isExample=False):
    if isExample:
        with open("example.txt") as f:
            return f.read().splitlines()[10:]
    else:
        with open("input.txt") as f:
            return f.read().splitlines()[10:]

stacks = {1: stack1, 2: stack2, 3: stack3, 4: stack4, 5: stack5, 6: stack6, 7: stack7, 8: stack8, 9: stack9}
stacks2 = deepcopy(stacks)

def part1(input):
    ans = ''
    for line in input:
        split = line.split(' ')
        crates_move = int(split[1])
        fromStack = int(split[3])
        toStack = int(split[5])
        crane = stacks[fromStack][:crates_move] 
        crane.reverse()
        stacks[toStack][:0] = crane
        del stacks[fromStack][:crates_move]

    x = 1
    for key in stacks.items():
        ans += stacks[x][0]
        x += 1
    print("Part 1: ", ans)


def part2(input):
    ans = ''
    for line in input:
        split = line.split(' ')
        crates_move = int(split[1])
        fromStack = int(split[3])
        toStack = int(split[5])
        crane = stacks2[fromStack][:crates_move] 
        #crane.reverse()
        stacks2[toStack][:0] = crane
        del stacks2[fromStack][:crates_move]

    x = 1
    for key in stacks2.items():
        ans += stacks2[x][0]
        x += 1

    print("Part 2: ", ans)


def main():
    input = readinput()
    part1(input)
    part2(input)


if __name__ == "__main__":
    main()
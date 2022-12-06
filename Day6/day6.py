


def readInput(isExample=False):
    if isExample:
        with open("example.txt", "r") as f:
            return f.read().splitlines()
    else:
        with open("input.txt", "r") as f:
            return f.read().splitlines()

def part1(input):
    ans = 0
    marker = ''
    # How many characters need to be processed before the first start-of-packet marker is detected?
    # start of packet marker is 4 characters long
    # 4 characters are already read in
    # all characters are different to be a correct marker

    for i in range(0, len(input)):
        # check if the marker has been found
        marker = input[i:i+4]
        isValid = False
        x = list(set(marker))
        y = list(marker)
        x.sort()
        y.sort()
        if x == y:
            isValid = True
        if isValid:
            ans = i + 4
            break
                
    print("Part 1: ", ans)

def part2(input):
    ans = 0
    message = ''
    for i in range(0, len(input)):
        message = input[i:i+14]
        isValid = False
        x = list(set(message))
        y = list(message)
        x.sort()
        y.sort()
        if x == y:
            isValid = True
        if isValid:
            ans = i + 14
            break
        


    print("Part 2: ", ans)

def main():
    input = readInput()
    string = input[0]
    part1(string)
    part2(string)

if __name__ == "__main__":
    main()
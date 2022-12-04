

def readInput(isExample=False):
    if isExample:
        with open("example.txt", "r") as f:
            return f.read().splitlines()
    else:
        with open("input.txt", "r") as f:
            return f.read().splitlines()




def part1(input):
    ans = 0
    for pairs in input:
        elf1, elf2 = pairs.split(",")
        elf1 = elf1.split("-")
        elf2 = elf2.split("-")
        elf1 = [int(elf1[0]), int(elf1[1])]
        elf2 = [int(elf2[0]), int(elf2[1])]
        #check if elf1 fully contains elf2
        if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            ans += 1
        #check if elf2 fully contains elf1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            ans += 1
        


    print("Part 1: ", ans)


def part2(input):
    ans = 0
    for pairs in input:
        elf1, elf2 = pairs.split(",")
        elf1 = elf1.split("-")
        elf2 = elf2.split("-")
        elf1 = [int(elf1[0]), int(elf1[1])]
        elf2 = [int(elf2[0]), int(elf2[1])]
        # check if any of the elfs are fully contained
        if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            ans += 1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            ans += 1
        # check if any of the elfs are partially contained
        elif elf1[0] <= elf2[0] and elf1[1] >= elf2[0]:
            ans += 1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[0]:
            ans += 1
            

    print("Part 2: ", ans)


def main():
    input = readInput()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()
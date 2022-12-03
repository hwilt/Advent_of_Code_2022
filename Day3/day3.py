

def readinput(isExample=False):
    if isExample:
        with open("example.txt") as f:
            return f.read().splitlines()
    else:
        with open("input.txt") as f:
            return f.read().splitlines()


def letterToNumber(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38



def part1(input):
    same_letters = []
    for rucksack in input:
        # rucksack is made up of 2 parts, to split them by the length/2
        first_Compartment, second_Compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        #print(first_Compartment, second_Compartment)
        # loop through the first compartment and check if the second compartment also has the same letter
        
        same_letters_in_rucksack = []
        for letter in first_Compartment:
            if letter in second_Compartment:
                if letter not in same_letters_in_rucksack:
                    same_letters_in_rucksack.append(letter)
                #same_letters.append(letter)
        same_letters.append(same_letters_in_rucksack)
    #print(same_letters)
    sum = 0
    for rucksack in same_letters:
        for letter in rucksack:

            # lowercase letters = 1 through 26
            # uppercase letters = 27 through 52
            
            sum += letterToNumber(letter)

    print("part 1: ", sum)


def part2(input):
    groups = []
    for rucksack in input:
        # every 3 rucksacks are a group
        if len(groups) == 0:
            groups.append([rucksack])
        else:
            if len(groups[-1]) == 3:
                groups.append([rucksack])
            else:
                groups[-1].append(rucksack)

    #print(groups)

    # loop through the groups and check if the rucksacks have the same letters
    same_letters = []
    for group in groups:
        same_letter_in_group = []
        for rucksack in group:
            for letter in rucksack:
                if letter in group[0] and letter in group[1] and letter in group[2]:
                    if letter not in same_letter_in_group:
                        same_letter_in_group = letter
        same_letters.append(same_letter_in_group)
    sum = 0
    for letter in same_letters:
        #print(letter)
        sum += letterToNumber(letter)


    print("part 2: ", sum)


def main():
    input = readinput()
    #print(input)
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()
from dataclasses import dataclass

@dataclass
class elf:
    id: int
    calories: int
    counter = 0 

    def __init__(self):
        self.id = elf.counter
        self.calories = 0
        elf.counter += 1


    def get_id(self):
        return self.id
    
    def add_calories(self, calories):
        self.calories += calories

    def get_calories(self):
        return self.calories


def read_input():
    with open("input.txt", "r") as f:
        # make a new elf object when there is a empty line
        elves = [elf()]
        for line in f:
            #print("1 " + line)
            if line == "\n":
                elves.append(elf())
            else:
                # add calories to the last elf
                elves[-1].add_calories(int(line))
    return elves



def day1():
    # read input and find the elf with the most calories
    elves = read_input()
    max_calories = 0
    for elf in elves:
        if elf.get_calories() > max_calories:
            max_calories = elf.get_calories()
    
    # print the elves with the most calories
    print(f"Day 1< Part 1 >: {max_calories} ")


def day2():
    elves = read_input()
    # get the top 3 elves with the most calories
    elves.sort(key=lambda x: x.get_calories(), reverse=True)
    top_3 = elves[:3]
    sum_calories = top_3[0].get_calories() + top_3[1].get_calories() + top_3[2].get_calories()

    print(f"Day 1< Part 2 >: {sum_calories} ")

if __name__ == "__main__":
    day1()
    day2()


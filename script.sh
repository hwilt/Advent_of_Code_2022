#!/bin/bash


# loop make 25 folders named "Day 1" to "Day 25" with a file named "input.txt" and "day{folder day number}.py" in each folder
touch "README.md"
for i in {1..25}
do
    mkdir "Day$i"
    touch "Day$i/input.txt"
    touch "Day$i/day$i.py"
    touch "Day$i/example.txt"
done
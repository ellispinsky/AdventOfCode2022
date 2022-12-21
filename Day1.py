def solution():
    with open('Day1input.txt', 'r') as in_txt: # Open the input file
        seq = in_txt.read().split("\n\n") #split by double newline
        sum_cals = [sum(int(snack_cals) for snack_cals in inventory) for inventory in
                    [line.splitlines() for line in seq]]
        print(max(sum_cals)) #print the max calories
        print(sum(sorted(sum_cals)[-3:]))
solution()